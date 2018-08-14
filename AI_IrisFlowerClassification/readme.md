# Iris FLower Classification 
### Using a Deep Feedforward Neural Network created using Python and Tensorflow
### - Vatsal Savani
<br/>
<br/>

## Description - What is the Iris Flower Dataset?
The Iris Dataset, which can be found at the : [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) - created by R.A. Fisher, is a database of 150 different plant samples as well as some properties about each flower. This dataset is perhaps the best known database to be found and is commonly used in Machine Learning to test various different ML algorithms. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other, which makes this an excellent choice as a dataset to test ML algorithms that are used for classification. 

The attributes for each Iris flower given in the dataset are :
* the ID
* Sepal length in cm
* Sepal width in cm
* Petal length in cm
* Petal width in cm
* the Class :
  - Iris-setosa
  - Iris-versicolour
  - Iris-virginica
  
More information can be found regarding the Iris Dataset here :
* https://en.wikipedia.org/wiki/Iris_flower_data_set, and
* https://archive.ics.uci.edu/ml/datasets/iris


## The Neural Network
The neural network is created using the Tensorflow library in Python; it is a [Deep Feedforward Neural Network](https://en.wikipedia.org/wiki/Feedforward_neural_network), which is also known as a multilayered-perceptron. A feedforward neural network is an artificial neural network wherein connections between the nodes do not form a cycle - this means information is not passed back, it is only passed on forward.

The general structure of the Neural Network used is as follows :
* Input Layer
  Nodes : 4
* 2 Hidden Layers :
  Hidden Layer 1 Nodes : 8
  Hidden Layer 2 Nodes : 8
* Output Layer
  Nodes : 3
  
To optimize the network, I use gradient descent which works quite level allowing me to attain an accuracy of 99%.
