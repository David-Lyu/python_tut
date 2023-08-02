import numpy as np
# import pandas
import tensorflow as tf

# Tensors can be indexed like pythons list

some_list = [1, 2, 3, 4]
some_list[0]

rank_4_tensor = tf.zeros(shape=[2, 3, 4, 5])
# Gets the first two elements of each dimension
print(rank_4_tensor[:2, :2, :2, :2])
# Gets the first element of the first dimension and the first 2 elements in 2nd dim and get the rest
print(rank_4_tensor[:1, :2])
print(rank_4_tensor[:1, :2, :3])

# Get the first element each dimension from each index except for the final one
some_list[:1]

# just ':' by itself is like omiting it
rank_4_tensor[:1, :1, :1, :]

# TensorShape([2,2],2)
rank_2_tensor = tf.constant([[10, 7], [3, 4]])

# Get last item of each of our rank 2 tensor
some_list[-1]

# Outputs: [7,4]
rank_2_tensor[:, -1]

# Add in extra dimension to our rank 2 tensor
# Output tf.Tensor: shape=(2,2,1), dtype=int32, numpy=array([[[10],[7]],[[3],[4]]])
# 2 elements in first array; 2 elements in second array; and 1 element in last array
rank_3_tensor = rank_2_tensor[..., tf.newaxis]

# Alt to tf.newaxis
tf.expand_dims(rank_2_tensor, axis=-1)  # "-1" means expand the final axis

# when adding a new axis the numbers stay the same but how the numbers are stored changed.
# If we put it in the first axis it shape would be (1,2,2). So it added the new tensors into the first axis. (put the rest of the tensor in a new tensor)
