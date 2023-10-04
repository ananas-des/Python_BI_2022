import multiprocessing
from typing import Dict, List, Tuple, Any


class ParallelMap:
    '''A class that parallelizes the map function using multiprocessing

    Attributes:
        target_func (function): the function to be applied to the data
        args_container (list): a list contained positional arguments for the target function
        kwargs_container (list): a list of dictionaries containing keyword arguments for the target function
        n_jobs (int): the number of CPUs used for multiprocessing
        l (int): the length of the argument containers
        _cont_mask (list): a list indicating the presence of argument containers
    '''
    
    
    
    def __init__(
        self,
        target_func: callable,
        args_container: List[Tuple] = None,
        kwargs_container: List[Dict] = None,
        n_jobs: int = None
    ) -> None:        
        '''Initializes the ParallelMap instance with the target function, positional and keyword arguments,
        and the number of CPUs to be used

        Parameters:
            target_func (function): the function to be applied to the data
            args_container (list): a list contained positional arguments for the target function
            kwargs_container (list): a list of dictionaries containing keyword arguments for the target function
            n_jobs (int): the number of CPUs used for multiprocessing

        Raises:
            ValueError: if the number of positional arguments does not match the number of keyword arguments

        Returns: None
        '''
        
        
        self.target_func = target_func
        self.args_container = args_container
        self.kwargs_container = kwargs_container
        if not n_jobs:
            self.n_jobs = multiprocessing.cpu_count()
        else:
            self.n_jobs = n_jobs
        self.__check_containers()
        self.n_jobs = min(self.n_jobs, self.l)
        
    
    def __check_containers(self) -> None:
        '''Private method that verifies that the argument containers are passed,
        sets the length of the containers, and adjusts the empy containers of required length as needed
        '''
        
        
        self._cont_mask = [bool(cont) for cont in [self.args_container, self.kwargs_container]]
        if self._cont_mask == [True, True]:
            arg_l, kwarg_l = len(self.args_container), len(self.kwargs_container)
            if arg_l != kwarg_l:
                raise ValueError(
                    f"Numbers of positional arguments and keyword arguments do not match: {arg_l} and {kwarg_l}"
                )
            self.l = arg_l
            self.args_container = self.__adj_args(self.args_container)
        elif self._cont_mask == [True, False]:
            self.l = len(self.args_container)
            self.args_container = self.__adj_args(self.args_container)
            self.kwargs_container = self.__adj_kwargs(self.l)
        elif self._cont_mask == [False, True]:
            self.l = len(self.kwargs_container)
            self.args_container = self.__adj_args(cont_l = self.l)
        else:
            self.l = self.n_jobs
            self.args_container = self.__adj_args(cont_l = self.l)
            self.kwargs_container = self.__adj_kwargs(cont_l = self.l)


    def __adj_args(self, cont: List[Any] = None, cont_l: int = None) -> List[Tuple]:
        '''Private method that transforms elements of the positional argument container to tuples,
        if the positional argument container is not passed, creates list of empty tuples with required length

        Parameters:
            cont (list): the positional argument container
            cont_l (int): the length of the positional argument container

        Returns: 
            cont (list):  a list of tuples with the correct format for positional arguments
        '''
        
        
        if not cont_l:
            cont = [tuple([i]) if (type(i) is not tuple) else i for i in cont]
        else:
            cont = [()]*cont_l
        return cont


    def __adj_kwargs(self, cont_l: int) -> List[Dict]:
        '''Private method that adjusts the list of empty dictionaries with required length

        Parameters:
            cont_l (int): the length of the keyword argument container

        Returns: a list of empty dictionaries with the correct format for keyword arguments
        '''
        
        
        return [{}]*cont_l

    
    def process_tasks(
        self,
        task_queue: multiprocessing.Queue,
        result_dict: dict
    ) -> None:
        '''Processes tasks from a multiprocessing queue

        Parameters:
            task_queue (multiprocessing.Queue): The queue of tasks to be processed
            result_dict (multiprocessing.Manager.dict): a shared dictionary to store the results

        Returns: None
        '''
        
        
        while not task_queue.empty():
            i, args, kwargs = task_queue.get()
            result = self.target_func(*args, **kwargs)
            result_dict[i] = result
        return 


    def parallel_map(self) -> list:
        '''Runs the parallel map function using multiple CPUs

        Returns: a list of results from the map function
        '''
        
        
        task_queue = multiprocessing.Queue()
        for i in range(self.l):
            task_queue.put((i, self.args_container[i], self.kwargs_container[i]))
        manager = multiprocessing.Manager()
        result_dict = manager.dict()
        processes = []
        for i in range(self.n_jobs):
            p = multiprocessing.Process(target=self.process_tasks,
                                        args=(task_queue, result_dict))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        return [result_dict[i] for i in sorted(result_dict)]