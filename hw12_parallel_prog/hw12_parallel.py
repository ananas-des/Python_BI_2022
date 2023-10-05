import random
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from typing import Tuple, Callable, Optional, Dict, List, Tuple, Any
import os
import sys
import psutil
import time
import warnings
from threading import Thread
import _thread
import multiprocessing


# Task1
class RandomForestClassifierCustom(BaseEstimator):
    '''A custom implementation of random forest classifier
    (the most of the description is taken from `sklearn` source code)
    
    Attributes:
        n_estimators (int): a number of decision tree classifiers in forest
        max_depth (int): the maximum depth of the tree
        max_features (int): the number of features to consider when looking for the best split
        random_state (int): controls both the randomness of pseudosampling and feature selection
        feat_ids_by_tree (list): selected features for each tree
        trees (list): fitted trees for forest
    '''
    
    
    def __init__(
        self, n_estimators: int = 10, max_depth: int = None, max_features: int = None, random_state: int = None
    ) -> None:
        '''Constructs all the necessary attributes for the RandomForestClassifierCustom object

        Parameters:
            n_estimators (int): a number of decision tree classifiers in forest
            max_depth (int): the maximum depth of the tree
            max_features (int): the number of features to consider when looking for the best split
            random_state (int): controls both the randomness of pseudosampling and feature selection
            feat_ids_by_tree (list): selected features for each tree
            trees (list): fitted trees for forest       
        
        '''
        
        
        self.n_estimators: int = n_estimators
        self.max_depth: int = max_depth
        self.max_features: int = max_features
        self.random_state: int = random_state

        self.trees: list = []
        self.feat_ids_by_tree: list = []
        
           
    def __check_jobs(self, n_jobs: int, n_estimators: int) -> int:
        '''A private method for checking n_jobs. If n_jobs not defined, it is setted to 1
        
        Parameters:
            n_jobs (int): the number of jobs to run in parallel
            n_estimators (int): a number of trees in forest
            
        Returns: number of jobs (int)
        '''
        
        
        if n_jobs:
            return min(n_jobs, n_estimators)
        elif not n_jobs:
            return 1
        
        
    def __calc_estim_per_job(self, n_estimators: int, n_jobs: int) -> Tuple[np.ndarray, list]:
        '''A private method to split n_estimators for n_jobs. Also calculates "coordinates" to keep seed regardless of n_jobs
        
        Parameters:
            n_jobs (int): the number of jobs to run in parallel
            n_estimators (int): a number of trees in forest
            
        Returns:
            n_estimators_per_job (np.ndarray): array with splitted number of estimators per each job
            seed_coords (list): list with tuples contained start and stop coordinate for building trees and their seeds    
        '''
        
        
        n_estimators_per_job = np.full(n_jobs, n_estimators // n_jobs, dtype=int)
        n_estimators_per_job[: n_estimators % n_jobs] += 1
        
        # some calculations for building the same trees regardless n_jobs
        lst_cumsum = np.insert(np.cumsum(n_estimators_per_job), 0, 0, axis=0)
        # list for start and stop for calculating seeds
        seed_coords = []
        for i in range(1, len(lst_cumsum)):
            seed_coords.append((lst_cumsum[i-1], lst_cumsum[i]))
        return n_estimators_per_job, seed_coords
            
    
    def _build_trees(self, seed_coords: tuple, X: np.ndarray, y: np.ndarray) -> Tuple[list, list]:
        '''Private function used to build a single tree for forest
        
        Parameters:
            seed_coords (tuple): start and stop coordinates for building trees and their seeds
            X (np.ndarray): array with features
            y (np.ndarray): target vector
            
        Returns: None
        '''
        
        
        start, stop = seed_coords
        trees = []
        feat_ids_by_tree = []
        for i in range(start, stop):
            # setting seed
            np.random.seed(self.random_state + i)

            # selecting n random features 
            feat_ids = np.random.choice(X.shape[1], size=self.max_features, replace=False)
            feat_ids_by_tree.append(feat_ids)

            # creating pseudosample using bootstrap
            # random indices for pseudosample
            pseudo_idx = np.random.choice(X.shape[0], size=X.shape[0], replace=True).reshape(X.shape[0], 1)
            pseudo_X = X[pseudo_idx, feat_ids]
            pseudo_y = y[pseudo_idx]

            # creating and fitting model
            dec_tree_class = DecisionTreeClassifier(max_depth=self.max_depth,
                                                    max_features=self.max_features, 
                                                    random_state=self.random_state)
            dec_tree_class.fit(pseudo_X, pseudo_y)
            trees.append(dec_tree_class)
        return feat_ids_by_tree, trees

    
    def __do_parallel(self, func: Callable, n_jobs: int, *args) -> list: # args may contain X or both X and y
        '''Private method for running fit or predict_proba methods in parallel
        
        Parameters:
            func (Callable): function for parallel execution
            n_jobs (int): the number of jobs to run in parallel
            *args may contain X or both X and y
            
        Returns: list with futures (list)            
        '''
        
        
        n_jobs = self.__check_jobs(n_jobs, self.n_estimators)
        n_est_per_job, seed_coords = self.__calc_estim_per_job(self.n_estimators, n_jobs)
        futures = []
        with ThreadPoolExecutor() as pool:
            for i, _ in enumerate(n_est_per_job):
                futures.append(pool.submit(func, seed_coords[i], *args))
        return futures


    def fit(self, X: np.ndarray, y: np.ndarray, n_jobs: int = None) -> object:
        '''Build a forest of trees from the training set (X, y)
        
        Parameters:
            X (np.ndarray) of shape (n_samples, n_features): the training input samples
            y (np.ndarray) of shape (n_samples): target values labels
            n_jobs (int): the number of jobs to run in parallel
        Returns: self object (RandomForestClassifierCustom)
        '''
        
        
        self.classes_ = sorted(np.unique(y))
        futures = self.__do_parallel(self._build_trees, n_jobs, X, y)
        for future in futures:
            self.feat_ids_by_tree.extend(future.result()[0]) 
            self.trees.extend(future.result()[1])
        return self
            
        
    def _parallel_predict_proba(self, seed_coords: tuple, X: np.array) -> list:
        '''Function for running predict_proba using n trees per job
        
        Parameters:
            seed_coords (tuple): start and stop coordinates for using n trees
            X (np.ndarray): array with features
            
        Returns:
            probs (list): the class probabilities of the input samples based on n trees
        '''
        
        
        start, stop = seed_coords
        probs = []
        for i in range(start, stop):
            proba = self.trees[i].predict_proba(X[:, self.feat_ids_by_tree[i]])
            probs.append(proba)
        return probs
        
    
    def predict_proba(self, X: np.ndarray, n_jobs: int = None) -> list:
        '''Predicts class probabilities for X. The predicted class probabilities of an input sample are computed as
        the mean predicted class probabilities of the trees in the forest
        
        Parameters:
            X (np.ndarray) of shape (n_samples, n_features): the testing input samples
            n_jobs (int): the number of jobs to run in parallel
        '''
        
        
        futures = self.__do_parallel(self._parallel_predict_proba, n_jobs, X)
        result = []
        for future in futures:
            result.extend(future.result())
        return np.mean(result, axis=0)
    
    
    def predict(self, X: np.ndarray, n_jobs: int = None) -> np.ndarray:
        '''Predicts class for X. The predicted class of an input sample is a vote by the trees in the forest, 
        weighted by their probability estimates. That is, the predicted class is the one with highest mean probability
        estimate across the trees
        
        Parameters:
            X (np.ndarray) of shape (n_samples, n_features): the testing input samples
            n_jobs (int): the number of jobs to run in parallel
            
        Returns:
            predictions (np.ndarray) of shape (n_samples,): the predicted classes    
        '''
        
        
        probas = self.predict_proba(X, n_jobs)
        predictions = np.argmax(probas, axis=1)
        return predictions

    
# Task2    
class MemoryThread(Thread):
    '''A thread that monitors the memory usage of a process

    Attributes:
        soft_limit (str): the soft memory limit in a human-readable format (e.g., "512M")
        hard_limit (str): the hard memory limit in a human-readable format (e.g., "1.5G")
        poll_interval (float): the time interval (in seconds) for checking memory usage
        _bytes_soft_limit (int): the soft memory limit in bytes
        _bytes_hard_limit (int): the hard memory limit in bytes
        broken_soft (bool): True if the soft memory limit has been exceeded
        memory_usage (str): the current memory usage in a human-readable format (e.g., "100M")
    '''
    
    
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for idx, s in enumerate(symbols):
        prefix[s] = 1 << (idx + 1) * 10
    
    
    def __init__(self, soft_limit, hard_limit, poll_interval) -> None:
        '''
        Initializes a MemoryThread instance

        Parameters:
            soft_limit (str): the soft memory limit in a human-readable format (e.g., "512M").
            hard_limit (str): the hard memory limit in a human-readable format (e.g., "1.5G").
            poll_interval (float): the time interval (in seconds) for checking memory usage

        Returns: None
        '''
        
        
        super().__init__()
        self.soft_limit = soft_limit
        self.hard_limit = hard_limit
        self.poll_interval = poll_interval
        self.broken_soft = False
        if soft_limit:
            self._bytes_soft_limit = self.human_readble_to_bytes(self.soft_limit)
        if hard_limit:
            self._bytes_hard_limit = self.human_readble_to_bytes(self.hard_limit)
                   
        
    def get_memory_usage(self) -> int: # Показывает текущее потребление памяти процессом
        '''Returns the current memory usage of the process in bytes'''
        
        
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss


    def human_readble_to_bytes(self, limit: str) -> int:
        '''Converts a human-readable memory limit (e.g., "512M") to an integer in bytes
        
        Parameters:
            limit (str): a human-readable memory limit to be converted
            
        Returns: memory limit in bytes (int)
        '''
        
        
        for s in MemoryThread.symbols:
            if limit[-1] == s:
                value = int(float(limit[:-1]) * MemoryThread.prefix[s])
                return value
        return int(limit)


    def bytes_to_human_readable(self, n_bytes: int) -> str:
        '''Converts a number of bytes to a human-readable memory size (e.g., "100M")

        Parameters:
            n_bytes (int): the number of bytes

        Returns: a string representing the memory size in a human-readable format (str)
        '''
        
        
        for s in reversed(MemoryThread.symbols):
            if n_bytes >= MemoryThread.prefix[s]:
                value = float(n_bytes) / MemoryThread.prefix[s]
                return f"{value:.2f}{s}"
        return f"{n_bytes}B"

        
    def run(self) -> None:
        '''The main run method of the thread'''
        
        
        while True:
            memory_usage = self.get_memory_usage()
            self.memory_usage = self.bytes_to_human_readable(memory_usage)
            if (not self.broken_soft) and self.soft_limit:
                self.check_soft(memory_usage)
            if self.hard_limit:
                self.check_hard(memory_usage)
            if hasattr(self, 'event'):
                return
            time.sleep(self.poll_interval)
        return
            
                      
    def check_soft(self, memory_usage: int) -> None:
        '''Check if the soft limit has been exceeded

        Parameters:
            memory_usage (int): the current memory usage in bytes

        Returns: None
        '''
        
        
        def custom_formatwarning(msg: str, *args, **kwargs) -> str:
            '''Formats UserWarning message output
            
            Parameters:
                msg (str): message to raise
                *args, **kwargs contains other parameters of UserWarning
                
            Returns: UserWarning message (str)    
            '''
            
            
            # ignore everything except the message
            return  f"Warning! {str(msg)}"
        
        if memory_usage >= self._bytes_soft_limit:
            self.broken_soft = True
            warnings.formatwarning = custom_formatwarning
            warnings.warn(
                f"Soft limit {self.soft_limit} is broken, current memory usage - {self.memory_usage}!", 
                UserWarning
            )
            
            
    def check_hard(self, memory_usage: int) -> None:
        '''Check if the hard limit has been exceeded

        Parameters:
            memory_usage (int): The current memory usage in bytes.

        Returns: None
        '''
        
        
        if memory_usage >= self._bytes_hard_limit:
            _thread.interrupt_main() # I tried to catch KeybordInterrupt error here too
            time.sleep(2)
            # I used it here to restart kernel for cleaning memory
            # for some reason, gc.collect() could not cope with this task 
            os._exit(0)
            
            
class MemLimitException(BaseException):
    '''A custom exception class for raising when memory limit is exceeded'''
    
    
    def __init__(self, obj: MemoryThread) -> None:
        '''Initializes a MemLimitException instance

        Parameters:
            obj (MemoryThread): the instance of MemoryThread where the exception occurred

        Returns: None
        '''
        
        
        self.obj = obj
    
    
    def __str__(self) -> str:
        '''Returns a string representation of the MemLimitException'''
        
        
        return f"Hard limit {self.obj.hard_limit} is broken, current memory usage - {self.obj.memory_usage}!"

            
def memory_limit(
    soft_limit: Optional[str] = "512M",
    hard_limit: Optional[str] = "1.5G",
    poll_interval: float = 0.1
) -> None:
    '''Decorator function to limit the memory usage of a function

    Parameters:
        soft_limit (str): the soft memory limit in a human-readable format (e.g., "512M")
        hard_limit (str): the hard memory limit in a human-readable format (e.g., "1.5G")
        poll_interval (float): the time interval (in seconds) for checking memory usage

    Returns: the decorated function
    '''
    
    
    def decor(func):
        def inner_func(*args, **kwargs):
            thread_started = False
            if soft_limit or hard_limit:
                thread_started = True
                mem_check = MemoryThread(soft_limit, hard_limit, poll_interval)
                mem_check.start()
            try:
                result = func(*args, **kwargs)
                if thread_started:
                    mem_check.event = True
            except KeyboardInterrupt as e: # error is not catched
                raise MemLimitException(mem_check)
            return result
        return inner_func
    return decor


@memory_limit(soft_limit="512M", hard_limit="1.5G", poll_interval=0.1)
def memory_increment():
    """
    Функция для тестирования
    
    В течение нескольких секунд достигает использования памяти 1.89G
    Потребление памяти и скорость накопления можно варьировать, изменяя код
    """
    lst = []
    for i in range(50000000):
        if i % 500000 == 0:
            time.sleep(0.1)
        lst.append(i)
    return lst


# Task3
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