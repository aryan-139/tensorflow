import tensorflow as tf

#check the version of the tensorflow
print(tf.__version__)

# Simple test: Create two tensors and add them
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
c = tf.add(a, b)

# Print the result
print("Result of a + b:\n", c)