import tensorflow as tf
import pandas as pd
import numpy as np
import csv, random

#0 = Iris-Setosa; 1 = Iris-Versicolor; 2 = Iris-Viriginica

#Loading and setting the dataset
dataset = open('datasetNew.csv', 'r')
reader = csv.reader(dataset)
data = []
for row in reader :
    if row[4] == 'Iris-setosa' :
        row[4] = 0
    elif row[4] == 'Iris-versicolor' :
        row[4] = 1
    else :
        row[4] = 2
    data.append(row)
del data[0]

#Creating Training and Testing data
testDataSize = 5
testingData = []
for i in range(testDataSize) :
    testingData.append((data.pop(random.randint(1, len(data) - 1))))

trainInput = [i[:4] for i in data]
trainOutput = [i[4] for i in data]

testInput = [i[:4] for i in testingData]

#Parameters
learningRate = 0.001
epoch = 500
interval = 50

#Network Parameter
hiddenLayer1 = 3 #Number of neurons in hidden layer 1
hiddenLayer2 = 3 #Number of neurons in hidden layer 2
numInputs = 4 #Number of inputs
numOutputs = 3 #Number of outputs

#Placeholders
inputs = tf.placeholder("float", [None, numInputs])
target = tf.placeholder("float", [None, numOutputs])

#Weights and Biases
weights = {
    'hL1': tf.Variable (tf.random_normal ([numInputs, hiddenLayer1])), #Inputs to Hidden Layer 1
    'hL2': tf.Variable (tf.random_normal ([hiddenLayer1, hiddenLayer2])), #Hidden Layer 1 to Hidden Layer 2
    'output': tf.Variable (tf.random_normal ([hiddenLayer2, numOutputs])) #Hidden Layer 2 to Outputs
}
biases = {
    'hL1': tf.Variable (tf.random_normal ([hiddenLayer1])),
    'hL2': tf.Variable (tf.random_normal ([hiddenLayer2])),
    'output': tf.Variable (tf.random_normal ([numOutputs]))
}

#Creating model
def nn(x):
    # Hidden layers fully connected layer with all neurons
    layer1 = tf.add(tf.matmul(x, weights['hL1']), biases['hL1'])
    layer2 = tf.add(tf.matmul(layer1, weights['hL2']), biases['hL2'])
    # Output fully connected layer with a neuron for each class
    outLayer = tf.matmul(layer2, weights['output']) + biases['output']
    return outLayer

#Construct model
model = nn(inputs)

#Loss function and optimizer
loss = tf.reduce_mean(-tf.reduce_sum(target * tf.log(model), axis=0))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = learningRate).minimize(loss)

# Initialize all variables
init = tf.global_variables_initializer()

with tf.Session() as sess :
    sess.run(init)

    #Training
    print('Model Training Begins . . .')
    for i in range(1, (epoch + 1)):
        sess.run(optimizer, feed_dict={inputs: trainInput, target: trainOutput})
        if i % interval == 0:
            print('Epoch', i, '|', 'Loss:', sess.run(loss, feed_dict={inputs: trainInput, target: trainOutput}))

    # Prediction
    print('Model Predicting Begins . . .')
    for i in range(len(testDataSize)):
        print('Actual:', testInput[i], 'Predicted:', np.rint(sess.run(model, feed_dict={inputs: [trainInput[i]]})))