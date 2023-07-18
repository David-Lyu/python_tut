import numpy as np
# import pandas
import tensorflow as tf

changeable_tensor = tf.Variable([10,7])
unchangeable_tensor = tf.constant([10,7])

#output changeable
## tf.Variable 'Variable:0' shape=(2,) dtype=int32 numpy=array([10,7]) dtype=int32
#output unchangeable
## tf.Tensor: shape=(2,), dtype=int32, numpy=array([10,7], dtype=int32)

#Try to change one of the elements:
##Changeable

# changeable_tensor[0] = 7; #error object doesn't support reassignment
changeable_tensor[0].assign(7);
#output is array(7,7)

##Unchangeable tensor
#unchangeable_tensor[0] = 7 #similar error asa before
#unchangeable_tensor[0].assign(7) object has no attr assign
