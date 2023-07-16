import numpy as np
# import pandas
import tensorflow as tf


print(tf.config.list_physical_devices())

print(tf.__version__)

# Creating tensors with tf.constant()

scalar = tf.constant(7);
## Returns: <tf.Tensor: shape=(), dtype=int32, numpy=7>
scalar


## Checks the number of dimensions of a tensors(ndim)
## Output: 0
scalar.ndim

## Create a vector
vector = tf.constant([10,10])
## <tf.Tensor: shape(2,), dtype=int32, numpy=array([10,10], dtype=int32)>
vector

## Output: 1
vector.ndim

## Create a matrix
matrix = tf.constant([[10,7],[7,10]])
matrix

## <tf.Tensor: shape=(2,2), dtype=int32, numpy=array([[10,7],[7,10]], dtype=int32)

## Output: 2
matrix.ndim

## Create another matrix
matrix2 = tf.constant([[10.,7.],[3.,2.],[8.,9.]],dtype=tf.float16)
##Output: 2
matrix2

tensor = tf.constant([
  [
    [1,2,3],
    [4,5,6]
  ],
  [
    [7,8,9],
    [10,11,12]
  ],
  [
    [13,14,15],
    [16,17,18]
  ]
])

print(tensor)
## Output: 3
tensor.ndim

### ALL matrix, vecorts, scalar will be still referenced as tensors
