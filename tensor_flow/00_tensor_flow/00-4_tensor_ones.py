import numpy as np
# import pandas
import tensorflow as tf

# Create a tensor of all ones with 10 rows 7 col
tf.ones([10, 7])

# Create a tensor of all zeros with a tuple no diff
tf.zeros((3, 4))

# Convert numpy arrays into tensors
# Main diff from numpy arr and tensorsFlow tensors can be
# run on a gpu for numerical computing


numpy_A = np.arange(1, 25, dtype=np.int32)
print(numpy_A)

# the 'A' is associated with matrix ( The capitol part)
# if 'a' then it is associated with vector

A = tf.constant(numpy_A)
print(A)
