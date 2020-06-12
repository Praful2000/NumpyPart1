# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Numpy in Python 

import numpy as np

a = np.array([1,2,3])

print(a[2])



Two Dimention Array 

a = np.array([[1,2,4],[4,6,8],[3,4,6]])

Dimens :
a.ndim

Size of array : 
a.size

size of data type :
    
a.itemsize

print(a)





a = np.array([[1,2,4],[3,4,6]], dtype = np.float64)

a.itemsize

a.size 

size of element =  a.size


width and height 

a.shape

arr = np.zeros((2,3))

arr = np.ones((3,4))



Using numpy List

arr = np.arange(1,9)
print(arr)

If we want to take steps 


arr = np.arange(1,10,3)

print(arr)

We want to generate numbers between the range of something also want linearly 
spaced than the function is 

arr = np.linspace(1,20,5)
print(arr)


if we want to reshape our array :
    
arr = np.arange(1,11)
arr.shape
arr = arr.reshape(2,5)
arr = arr.reshape(10,)


To make any array to one dimention 

arr.ravel()


arr.min()
arr.max()
arr.sum()

arr = arr.reshape(5,2)
arr = arr.sum(axis = 1)

np.sqrt(arr)

Standard Daviation 

np.std(arr)

Basic Mathmatics Operations on Array 

arr1 = np.array([[1,2],[6,7]])
arr2 = np.array([[3,4],[5,6]])

arr = arr1 * arr2 
print(arr)



it will do Matrics Product 

arr = arr1.dot(arr2)
arr





    







