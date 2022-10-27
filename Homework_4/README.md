# **NumPy Challenge** 🔢 @ 🔡
## Homework4

Utility **numpy_challenge.py** provides some functions for dealing with *one and two dimensional matrices* given in `numpy.array` format, 
such as *matrix multiplication*, *multidimensional distance computation*, and *distance matrix generation*. 
This functions is based on Python **NumPy package**. You may use **numpy_challenge.py** functions in other programm 
after importing the utility as module `import numpy_challenge as {name}`. If you run **numpy_challenge.py** as the main program, 
it will also generate **three different numpy.arrays** and put them into *std.output*. Here some guidelines for how to use this script and how does it work.

### Files
In this directory there are *four files*: [README.md](./README.md), [requirements.txt](./requirements.txt), and [numpy_challenge.py](./numpy_challenge.py).

- **README.md**: utility description and guidelines for its usage;

- **requirements.txt**: .txt file with the dependencies for *numpy_challenge.py*;

- **numpy_challenge.py**: .py script

### System
Launch of utility **numpy_challenge.py** was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.10.6**.

### Utility Functions
There are some functions for dealing with *one and two dimensional matrices* given in `numpy.array` format:

- `matrix_multiplication()`: performs matrix multiplication of two 2D matrices using `numpy.matmul()`;

- `multiplication_check()`: determines whether matrices in list can be multiplied in given order;

- `multiply_matrices()`: performs matrix multiplication of matrices in list in given order;

- `compute_multidimensional_distance()`: calculates distance between given multidimensional coordinates using `numpy.linalg.norm()`;

- `compute_2d_distance()`: deals with special case of distance between given multidimensional coordinates, when coordinates for object in 2D. 
For calculations calls function `compute_multidimensional_distance()`;

- `compute_pair_distances(matrix_2D)`: calculates square matrix containing the distances, taken pairwise, between the elements in 2D array 
using numpy's broadcasting rules

Also after running **numpy_challenge.py** as the main program, it will also generate **three different numpy.arrays** and put them into `std.output`. 
Their script under `if __name__ == "__main__":`.

### Launch

Launch **numpy_challenge.py** as the main program:

- create virtual environment

`conda create --name {env name} python=3.10.6`

- activate you virtual environment

`conda activate {env name}`

- install the specified packages using the configuration file **requirements.txt**

`pip install -r requirements.txt`

- launch **numpy_challenge.py** as the main program:

`python3 numpy_challenge.py`

OR

Import **numpy_challenge.py** as the module in other .py programs:

`import numpy_challenge as {name}`
