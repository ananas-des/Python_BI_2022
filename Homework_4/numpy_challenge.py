#!/usr/bin/env python
# coding: utf-8

# In[84]:


import numpy as np


def matrix_multiplication(matrix1, matrix2):
    '''Function matrix_multiplication() performs matrix multiplication of two 2D matrices
    
    Parameters:
    matrix1(m x n), matrix2(n x k) (numpy.ndarray): input arrays
    
    Returns: 
    matrix(m x k), numpy.array
    '''
    
    return np.matmul(matrix1, matrix2)


def multiplication_check(matrix_list):
    '''Function multiplication_check() determines whether matrices in list can be multiplied in given order
    
    Parameters:
    matrix_list (list): list of numpy.arrays
    
    Returns: bools after multiplication check
    True - matrices in list can be multiplied in given order    
    '''
    
    for index in range(len(matrix_list) - 1):
        if matrix_list[index].shape[1] != matrix_list[index+1].shape[0]:
            return False
        return True


def multiply_matrices(matrix_list):
    '''Function multiply_matrices() performs matrix multiplication of matrices in list in given order
    
    Parameters:
    matrix_list (list): list of numpy.arrays
    
    Principle:
    [a, b, c] - list of numpy.arrays
    multiply_matrices([a, b, c]) = (a @ b) @ c = res1 @ c = mult_result
    
    Returns:
    mult_result (numpy.array): resulted matrix
    None - if matrices in given order can't be multiplied
    '''
    
    mul_check = multiplication_check(matrix_list)
    if mul_check == False:
        return None
    mult_result = matrix_list[0]
    for index in range(1, len(matrix_list)):
        mult_result = matrix_multiplication(matrix1=mult_result, 
                                            matrix2=matrix_list[index])
    return mult_result


def compute_multidimensional_distance(array1, array2):
    '''Function compute_multidimensional_distance() calculates distance
    between given multidimensional coordinates using numpy.linalg.norm()
    
    Parameters:
    array1, array2 (numpy.array): 1D arrays with equal numbers of values
    
    Returns: value (float) - resulted distance  
    '''
    
    return np.linalg.norm(array1 - array2)


def compute_2d_distance(array1, array2):
    '''Function compute_2d_distance() deals with special case of distance
    between given multidimensional coordinates, when coordinates for object in 2D
    For calculations calls function compute_multidimensional_distance()
    
    Parameters:
    array1, array2 (numpy.array): 1D arrays with two values
    
    Returns: value (float) - resulted distance
    '''
    
    return compute_multidimensional_distance(array1, array2)


def compute_pair_distances(matrix_2D):
    '''Function compute_pair_distances() calculates square matrix containing the distances, 
    taken pairwise, between the elements in 2D array using numpy's broadcasting rules
    
    Parameters:
    2D_matrix (numpy.array): matrix with two dimensions
    
    Returns: 
    distance_matrix (numpy.ndarray) 
    '''
        
    distance_matrix = np.linalg.norm(a[:, None] - a[None, :], axis=-1)
    return distance_matrix


if __name__ == "__main__":
    # First way to create numpy array: numpy.arange and numpy.reshape
    # first_array shape is (20, 5)
    first_array = np.arange(1, 101).reshape(20, 5)
    print(f'First array:\n{first_array}\n')

    # Second way to create numpy array: numpy.indices
    # second_array shape is (2, 5, 5)
    second_array = np.indices((5,5))
    print(f'Second array:\n{second_array}\n')

    # Third way to create numpy array: numpy.diag
    # third_array shape is (5, 5)
    third_array = np.diag(['You', 'look', 'so', 'pretty', 'today'])
    print(f'Third array:\n{third_array}')

