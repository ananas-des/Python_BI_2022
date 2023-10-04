# Parallel Programming :traffic_light:

## Homework12

Here some solutions for Python **Parallel Programming** Tasks using `sklearn`, `numpy`, and some built-in packages for parallel programming in Python, such as `concurrent`, `multiprocessing`, and `threading`.

### System
This code was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.9.13**.

### Files
In this directory there are *five files*: [README.md](./README.md), [hw12_parallel.ipynb](./hw12_parallel.ipynb), [hw12_parallel.py](./hw12_parallel.py), [parallel_map.py](./parallel_map.py) and [requirements.txt](./requirements.txt).

- **README.md**: discriptions for files in this directory 
- **requirements.txt**: .txt file with environment dependencies
- **hw12_parallel.ipynb**: jupyter notebook with Tasks solutions and testings
- **hw12_parallel.py**: .py file with only code from jupyter notebook
- **parallel_map.py**: .py file with class `ParallelMap` to use as module

## Task1. Paralleling custom Random Forest

- parallelize `fit()`, `predict_proba()`, and `predict()` methods for custom implementation of Random Forest Classifier

## Task2. Memory usage decorator

- decorator function `memory_usage()` to limit the memory usage of a target function. The example usage of this decorator function is shown below:

```
@memory_limit(soft_limit="512M", hard_limit="1.5G", poll_interval=0.1)
def memory_increment():
    '''Tesing function
    
    Within a few seconds, memory usage reaches 1.89G, memory consumption and
    accumulation rate can be varied by changing the code
    '''
    
    
    lst = []
    for i in range(50000000):
        if i % 500000 == 0:
            time.sleep(0.1)
        lst.append(i)
    return lst

memory_increment()
```

Warning message is raisen when memory consuption by target function reaches soft limit (e.g., 512M), or target function is shut down if its memory consumption is over hard limit (e.g., 1.5G). The memory consumption is checked every defined seconds (e.g., `poll_interval=0.1`).

## Task3. Custom Parallel mapping

- a class `ParallelMap` that parallelizes the map function using multiprocessing

### Usage of `ParallelMap`

- download [parallel_map.py](./parallel_map.py) script file;

- run your main program and import `ParallelMap` from **parallel_map.py** module

```from parallel_map import ParallelMap```

As an example, there is target function `test_func`:

```
def test_func(x=1, s=2, a=1, b=1, c=1):
    time.sleep(s)
    return a*x**2 + b*x + c
```

To call that function in parallel, initiate the `ParallelMap` instance with arguments for target fuction and run `parallel_map()` method:

```
parl_map = ParallelMap(test_func,
                       args_container=[1, 2, 3],
                       kwargs_container=[{"s": 3}, {"s": 3}, {"s": 3}],
                       n_jobs=3)
parl_map.parallel_map()
```
