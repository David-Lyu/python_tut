import numpy as np
# import pandas
import tensorflow as tf

# Getting information from tensors

# When dealing with tensors you probably want to be aware of the following attributes
# - Shape
# - Rank: number of tensor dimensions
# - Axis or dimensions
# - Size: Number of elements

# rank example
rank_4_tensor = tf.zeros(shape=[2, 3, 4, 5])
print(rank_4_tensor)

# Shape: [2,3,4,5]
rank_4_tensor.shape
# Axis/deminsions: 4
rank_4_tensor.ndim

# Size # 120 elements
rank_4_tensor.size

# Get various attr of our tensor
print("DataType:", rank_4_tensor.dtype)
print("Dimensions:", rank_4_tensor.ndim)
print("Shape of tensor", rank_4_tensor.shape)
print("Last axis element:", rank_4_tensor.shape([-1]))
print("Total num elements", tf.size(rank_4_tensor.size))
