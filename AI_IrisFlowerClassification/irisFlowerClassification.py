import tensorflow as tf
import pandas as pd
import numpy as np
import csv

#Loading the dataset
dataset = open()

#Parameters
learningRate = 0.1

#Network Parameter
hiddenLayer1 = 3 #Number of neurons in hidden layer 1
hiddenLayer2 = 3 #Number of neurons in hidden layer 2
numInputs = 4 #Number of inputs
numOutputs = 3 #Number of outputs

#Weights and Biases
weights = {
    'hL1': tf.Variable (tf.random_normal ([numInputs, hiddenLayer1])),
    'hL2': tf.Variable (tf.random_normal ([hiddenLayer1, hiddenLayer2])),
    'output': tf.Variable (tf.random_normal ([hiddenLayer2, numOutputs]))
}
biases = {
    'hL1': tf.Variable (tf.random_normal ([hiddenLayer1])),
    'hL2': tf.Variable (tf.random_normal ([hiddenLayer2])),
    'output': tf.Variable (tf.random_normal ([numOutputs]))
}

def nn (x):
    