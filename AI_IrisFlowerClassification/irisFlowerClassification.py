
import tensorflow as tf
import csv
import random
import numpy as np

# Dataset creation and editing

# Output class indentification : [setosa, versicolor, virginica]

# Loading and setting up the dataset
datasetFile = open('datasetNew.csv', 'r')
reader = csv.reader(datasetFile)
dataset = []

# Changing the output from 1 into 3 - this will allow the neural network to process the dataset. This is done because we have 3 different possible outputs.
for row in reader:
    if row[4] == 'Iris-setosa':
        row[4] = [1, 0, 0]
    elif row[4] == 'Iris-versicolor':
        row[4] = [0, 1, 0]
    else:
        row[4] = [0, 0, 1]
    dataset.append(row)

del dataset[0]

random.shuffle(dataset)

# Creating Training and Testing data
# The number of instances to test with once the Neural Network has been trained
testDataSize = 15

testingData = []  # Array that will store instances that will be used to test the NN

for i in range(testDataSize):
    # Removing instances from the complete dataset while also simultaneously appending these instances to the testingData array
    testingData.append((dataset.pop(random.randint(1, len(dataset) - 1))))

# Data instances (inputs and targets), separated into 2 arrays, for the use of training the neural network
trainInput = [i[:4] for i in dataset]
trainOutput = [i[4] for i in dataset]
# Data instances (inputs and outputs), separated into 2 arrays, for the use of testing the neural network
testInput = [i[:4] for i in testingData]
testOutput = [i[4] for i in testingData]

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# Neural Network

# Parameters
learningRate = 0.001
epoch = 700
interval = 50

# Network Parameters
hiddenLayer1 = 8  # Number of neurons in hidden layer 1
hiddenLayer2 = 8  # Number of neurons in hidden layer 2
numInputs = 4  # Number of total inputs - input nodes
numOutputs = 3  # Number of total outputs - output nodes

# Placeholders
inputs = tf.placeholder("float", [None, numInputs])
target = tf.placeholder("float", [len(trainInput), numOutputs])

# Weights and Biases
weights = {
    # Inputs to Hidden Layer 1
    'hL1': tf.Variable(tf.random_normal([numInputs, hiddenLayer1])),
    # Hidden Layer 1 to Hidden Layer 2
    'hL2': tf.Variable(tf.random_normal([hiddenLayer1, hiddenLayer2])),
    # Hidden Layer 2 to Outputs
    'output': tf.Variable(tf.random_normal([hiddenLayer2, numOutputs]))
}
biases = {
    # Biases for Hidden Layer 1 Nodes
    'hL1': tf.Variable(tf.random_normal([hiddenLayer1])),
    # Biases for Hidden Layer 2 Nodes
    'hL2': tf.Variable(tf.random_normal([hiddenLayer2])),
    # Biases for the Output Nodes
    'output': tf.Variable(tf.random_normal([numOutputs]))
}

# Creating the model


def nn(x):
    # Hidden layers fully connected layer with all neurons
    layer1 = tf.nn.relu(tf.add(tf.matmul(x, weights['hL1']), biases['hL1']))
    layer2 = tf.nn.relu(
        tf.add(tf.matmul(layer1, weights['hL2']), biases['hL2']))
    # Output fully connected layer with a neuron for each class
    outputLayer = tf.nn.softmax(
        tf.matmul(layer2, weights['output']) + biases['output'])
    return outputLayer


# Constructing the model
model = nn(inputs)

# Loss function and optimizer
loss = tf.reduce_mean(-tf.reduce_sum(target * tf.log(model), axis=0))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learningRate).minimize(
    loss)  # Data is optimized using Gradient Descent

# Initialize all variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Training
    print('Model Training Begins . . .')
    for i in range(1, (epoch + 1)):
        sess.run(optimizer, feed_dict={
                 inputs: trainInput, target: trainOutput})
        if i % interval == 0:
            print('Epoch', i, '|', 'Loss:', sess.run(
                loss, feed_dict={inputs: trainInput, target: trainOutput}))

    # Prediction and Testing
    correctOutput = []
    predictedOutput = []

    print('\nModel Predicting Begins . . .')
    for i in range(testDataSize):
        correctOutput.append(testOutput[i])
        predictedOutput.append(
            np.rint(sess.run(model, feed_dict={inputs: [testInput[i]]})))
        print('Actual:', correctOutput[i], 'Predicted:', predictedOutput[i])
