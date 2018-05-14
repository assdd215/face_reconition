#encoding=utf-8
"""
这里尝试来写一写MTCNN网络的训练顺序
"""

import tensorflow as tf
import numpy as np


class Network(object):

    def make_var(self,name,shape):
        return tf.get_variable(name,shape,trainable=True)

    def conv(self,input,kernel,strides,relu=True,biased=True,padding="SAME"):
        output = tf.nn.conv2d(input=input,filter=kernel,strides=strides,padding=padding)
        if biased:
            biases = tf.get_variable("biases",shape=[len(kernel[-1])])
            output = tf.nn.bias_add(output,biases)
        if relu:
            output = tf.nn.relu(output)
        return output


    def prelu(self,input,name):
        with tf.variable_scope(name):
            i = int(input.get_shape()[-1])
            alpha = self.make_var('alpha',shape=(i,))
            output = tf.nn.relu(input) + tf.multiply(alpha,-tf.nn.relu(-input))
        return output

    def max_pool(self,input,kernel,strides,padding='SAME'):
        return tf.nn.max_pool(input,ksize=kernel,padding=padding)

    def fc(self,input,num_out,name,relu=True):
        input_shape = input.get_shape()



class PNet(Network):
    def setup(self,input):
        covn = self.conv(input,[3,3,3,10],[1,1,1,1])



