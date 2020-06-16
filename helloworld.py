import tensorflow as tf

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print('train',mnist.train.num_examples,
      ',validation',mnist.validation.num_examples,
      ',test',mnist.test.num_examples)
