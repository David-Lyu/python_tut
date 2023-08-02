import numpy as np
# import pandas
import tensorflow as tf

# Manipulating tensors

# # Basic Operations
tensor = tf.constant([[10, 7], [3, 4]])

# These Tensor manipulation methods do not mutate original tensor

# Add +
# Output: [[20,17],[13,14]]; So adds 10 to all tensor elements
tensor + 10

# Delete -

# Multiply *

# Divide /

# Tensor flow library (better to use with GPU calculations)
# same as tensor * 10
tf.multiply(tensor, 10)
