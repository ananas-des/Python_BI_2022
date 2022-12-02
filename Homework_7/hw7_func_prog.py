#!/usr/bin/env python
# coding: utf-8

# In[27]:


import sys


def sequential_map(*args):
    '''Function sequential_map() applies number of functions to every item of iterable object
    
    Parameters: names of functions for sequential application and iterable object with values
    *args:
    function1, 
    function2, 
    ... , 
    iterable
    
    Returns:
    conteiner (list): the resulted iterable
    '''
    
    *functions, conteiner = args
    combined_function = func_chain(*functions)
    conteiner = list(map(combined_function, conteiner))
    return conteiner


def consensus_filter(*args):
    '''Function consensus_filter() applies number of filtering functions to each value in iterable. 
    All functions shoud return bool
    
    Parameters:
    *args:
    function1,
    function2,
    ...,
    iterable
    
    Returns:
    conteiner (list): the resulted iterable
    '''
    
    *functions, conteiner = args
    for func in functions:
        conteiner = list(filter(func, conteiner))
    return conteiner


def conditional_reduce(boolean_function, appl_function, conteiner):
    '''Function conditional_reduce() performs fuctional reduction using second function and
    skipping values that have not been filtered by the first conditional function
    
    Parameters:
    boolean_function: name of function for filtering values (should return bool)
    appl_function: name of function for application to conteiner
    conteiner: iterable object
    
    Returns:
    element1 (list): the conditional reduction result 
    '''
    
    conteiner = list(filter(boolean_function, conteiner))
    element1 = conteiner[0]
    for index in range(1, len(conteiner)):
        element2 = conteiner[index]
        element1 = appl_function(element1, element2)
    return element1


def func_chain(*functions):
    '''
    Function func_chain() returns function as the result of given functions sequential implementaion
    
    Parameters: names of functions for sequential implementation
    *args:
    function1,
    function2,
    ...
    
    Returns:
    combined function
    '''
    
    def combined_function(value):  # Use nested function in order to assign without execution.
        for function in functions:
            func_result = function(value)
        return func_result
    return combined_function


def multiple_partial(*functions, **kwargs):
    '''Function multiple_partial() takes an unlimited number of functions and 
    returns list of functions with partially defined arguments
    
    Parameters:
    *functions: unlimited number of functions
    function1,
    function2,
    ...
    **kwargs: function parameters to be defined
    
    Returns: list of functions with partially defined arguments
    '''

    part_func = []
    for func in functions:
        def partial_func(value, func=func):
            result = func(value, **kwargs)
            return result
        part_func.append(partial_func)
    return part_func


def nothing_to_print(*args, sep=' ', end= '\n'):
    '''Function nothing_to_print() is full analogous of python print() function created using python sys package
    
    Parameters:
    *args: unlimited number of objects to print
    sep (str): objects separator
    end (str): line end
    
    Returns:
    stdout (str): printed line
    '''
    
    sys.stdout.write(str(args[0]))
    if len(args) > 1:
        for i in args[1:]:
            sys.stdout.write(f'{sep}{str(i)}')
    sys.stdout.write(end)

