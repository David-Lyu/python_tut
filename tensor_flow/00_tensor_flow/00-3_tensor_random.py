import numpy as np
# import pandas
import tensorflow as tf

# Random Tensor
## a tensor with some arbitrary size with random numbers
## ex would be creating weight or certainty of ai

random_1 = tf.random.Generator.from_seed(42) #set seed for reproducibility
#normal uses a normal distribution (bell curve)
random_1.normal(shape=(3,2))

random_2 = tf.random.Generator.from_seed(42)
random_2.normal(shape=(3,2))
# Output:
## tf.tensor : shape(3,2), dtype=float32, numpy=array(<random matrix>), dtype=float32

random_1 == random_2
# Output
## true

# Shuffle the order in a tensor
# shuffle the order of input so helps prevent bias

not_shuffled = tf.constant([[10,7],[3,4],[2,5]])

not_shuffled.ndim;

# output: 2

tf.random.shuffle(not_shuffled);

# output reorder the tensor along first dimension (3,2) -> shuffle the dimension with 3 args
# so it shuffles along x axis or the items in the first array

tf.random.shuffle(not_shuffled); #seed = 42 -> same as tf.random.set_seed()

# ex: random_1 vs tf.random.shuffle(not_shuffled)

# Read through TensorFlow doc on random seed generation:

#https://www.tensorflow.org/api_docs/python/tf/random/set_seed

# Output is different everytime
tf.random.shuffle(not_shuffled, seed=42)

# Add global seed output stays the same read docks #4
tf.random.set_seed(42)
tf.random.shuffle(not_shuffled, seed=42)
