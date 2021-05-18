import tensorflow as tf
import numpy as np
import csv
import random
import time

# Dataset creation and editing
# Output class identification : [black, white]

# Loading and setting up the dataset
datasetFile = open('./dataset.csv', 'r')
reader = csv.reader(datasetFile)

# Formatting dataset to suit our needs for this NeuralNet
dataset = []


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hLen = len(hex)
    return [int(hex[i:i+hLen//3], 16) for i in range(0, hLen, hLen//3)]


for row in reader:
    row[0] = hex_to_rgb(row[0])
    for i in range(len(row[0])):
        row[0][i] = row[0][i]/255

    if int(row[1]) == 0:
        row[1] = [1, 0]
    else:
        row[1] = [0, 1]

    dataset.append(row)

random.shuffle(dataset)

# Creating Training and Testing Data
# The number of instances to test with once the Neural Network has been trained
testDataSize = 250

testingData = []  # Array that will store instances that will be used to test the NN

for i in range(testDataSize):
    # Removing instances from the complete dataset while also simultaneously appending these instances to the testingData array
    testingData.append((dataset.pop(random.randint(1, len(dataset) - 1))))

# Data instances (inputs and targets), separated into 2 arrays, for the use of training the neural network
trainInput = [i[0] for i in dataset]
trainOutput = [i[1] for i in dataset]

# Data instances (inputs and outputs), separated into 2 arrays, for the use of testing the neural network
testInput = [i[0] for i in testingData]
testOutput = [i[1] for i in testingData]


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# Neural Network

# Function to calculate network accuracy
def calc_accuracy(npArr1, npArr2):
    common = 0
    for i in range(len(npArr1)-1):
        for j in range(len(npArr1[i])-1):
            if npArr1[i][j] == npArr2[i][j]:
                common += 1
    return common/len(npArr1)*100


# Parameters
learningRate = 0.01
epoch = 3000
interval = int(epoch/15)

# Network Parameters
numInputs = 3  # Number of total inputs - input nodes
hiddenLayer1 = 7  # Number of neurons in hidden layer 1
hiddenLayer2 = 7  # Number of neurons in hidden layer 1
numOutputs = 2  # Number of total outputs - output nodes

# Placeholders
inputs = tf.placeholder('float', [None, numInputs])
targets = tf.placeholder('float', [len(trainInput), numOutputs])

# Weights and Biases
weights = {
    # Inputs to Hidden Layer 1
    'hL1': tf.Variable(tf.random_normal([numInputs, hiddenLayer1])),
    # Inputs to Hidden Layer 2
    'hL2': tf.Variable(tf.random_normal([hiddenLayer1, hiddenLayer2])),
    # Hidden Layer 1 to Outputs
    'output': tf.Variable(tf.random_normal([hiddenLayer2, numOutputs]))
}
biases = {
    # Biases for Hidden Layer 1 Nodes
    'hL1': tf.Variable(tf.random_normal([hiddenLayer1])),
    # Biases for Hidden Layer 1 Nodes
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
loss = tf.reduce_mean(-tf.reduce_sum(targets *
                                     tf.log(tf.clip_by_value(model, 1e-10, 1.0))))
optimizer = tf.train.AdamOptimizer(learning_rate=learningRate).minimize(
    loss)  # Data is optimized using Gradient Descent

# Initialize all variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    # Training
    startTime = time.time()
    print('Model Training Begins . . .')
    for i in range(1, (epoch + 1)):
        sess.run(optimizer, feed_dict={
                 inputs: trainInput, targets: trainOutput})
        if i % interval == 0:
            print('Epoch', i, '|', 'Loss:', sess.run(
                loss, feed_dict={inputs: trainInput, targets: trainOutput}))
    timeTaken = time.time()-startTime

    # Prediction and Testing
    correctOutput = []
    predictedOutput = []

    print('\nModel Predicting Begins . . .')
    for i in range(testDataSize):
        correctOutput.append(np.rint(testOutput[i]))
        predictedOutput.append(
            np.rint(sess.run(model, feed_dict={inputs: [testInput[i]]})[0]))

        print('Actual:', correctOutput[i], 'Predicted:', predictedOutput[i])

    print()
    print('* '*10)
    print('Accuracy : {}%'.format(calc_accuracy(correctOutput, predictedOutput)))
    print('* '*10)

    print()
    print('* '*10)
    print('Time taken to train model:', timeTaken)
    print('* '*10)
