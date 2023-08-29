# **Functional Programming** :twisted_rightwards_arrows:
## Homework7

Utility **functional.py** provides some functions for functional programming tasks, such as *sequential_map*, *consensus_filter*, 
*conditional_reduce*, *func_chain*, *multiple_partial*, and *nothing_to_print*. This functions based on bare Python source and built-in `sys` package.
Here some guidelines for how to use this script and how does it work.

### Files
In this directory there are *two files*: [README.md](./README.md) and [functional.py](./functional.py).

- **README.md**: utility description and guidelines for its usage;

- **functional.py**: .py script

### System
Launch of utility **functional.py** was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.10.6**.

### Utility Functions
There are some functions for functional programming tasks:

- `sequential_map()`: applies number of functions to every item in iterable object;

- `consensus_filter()`: applies number of filtering functions to each value in iterable. All functions shoud return bool;

- `conditional_reduce()`: performs fuctional reduction using second function and skipping values that have not been filtered by the first conditional function;

- `func_chain()`: returns function as the result of given functions sequential implementaion;

- `multiple_partial()`: takes an unlimited number of functions and returns list of functions with partially definedts;

- `nothing_to_print()`: is full analogous of python `print()` function created using python `sys` package. By default, this function uses whitespace and new line
symbol as separator and end for line, respectively

### Launch

- download script file

`wget https://github.com/AnasZol/Python_BI_2022/blob/Homework_7/Homework_7/functional.py`

- import **functional.py** as the module in other .py programs:

`import functional as {name}`

OR

- launch **functional.py** as the main program:

`python3 functional.py`
