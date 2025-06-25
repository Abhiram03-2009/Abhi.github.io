import numpy as np
import matplotlib.pyplot as plt
from urllib import request
import gzip
import pickle
import os

filename = [
["training_images","train-images-idx3-ubyte.gz"],
["test_images","t10k-images-idx3-ubyte.gz"],
["training_labels","train-labels-idx1-ubyte.gz"],
["test_labels","t10k-labels-idx1-ubyte.gz"]
]

def download_mnist():
    base_url = "http://yann.lecun.com/exdb/mnist/"
    for name in filename:
        print("Downloading "+name[1]+"...")
        request.urlretrieve(base_url+name[1], name[1])
    print("Download complete.")

def save_mnist():
    mnist = {}
    for name in filename[:2]:
        with gzip.open(name[1], 'rb') as f:
            mnist[name[0]] = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1,28*28)
    for name in filename[-2:]:
        with gzip.open(name[1], 'rb') as f:
            mnist[name[0]] = np.frombuffer(f.read(), np.uint8, offset=8)
    with open("mnist.pkl", 'wb') as f:
        pickle.dump(mnist,f)
    print("Save complete.")

def init():
    download_mnist()
    save_mnist()

def load():
    with open("mnist.pkl",'rb') as f:
        mnist = pickle.load(f)
    return mnist["training_images"], mnist["training_labels"], mnist["test_images"], mnist["test_labels"]

if 'mnist.pkl' not in os.listdir('.'):
    init()
  
x_train, t_train, x_test, t_test = load()

def sigmoid_func(X):
    return 1 / (1 + np.e**(-X))

def one_layer_init(input_size, output_size):
    Theta = np.random.uniform(low=-.3, high=0.3, size=(output_size, input_size))
    return add_bias(Theta)

def add_bias(X):
    return np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

def compute_layer(A, Theta):
    return sigmoid_func(A @ Theta.T)

def one_layer_output(X, Theta):
    return compute_layer(add_bias(X), Theta)

def n_layer_init(layer_sizes):
    layers = [one_layer_init(layer_sizes[i-1], layer_sizes[i]) for i in range(1, len(layer_sizes))]
    return layers

def n_layer_output(X, Theta):
    current_output = one_layer_output(X, Theta[0])
    for i in range(1, len(Theta)):
        current_output = one_layer_output(current_output, Theta[i])
    return current_output

def cost_function(A, Y):
    return -np.sum(Y * np.log(A) + (1-Y) * np.log(1-A))

def output_delta(A_j, Y):
    return A_j - Y

def hidden_delta(A_j, Delta_next, Theta_j):
    return ((1 - A_j) * A_j) * (Delta_next @ Theta_j)

def weight_update(A_j, Delta_next, Theta_j, rate):
    return Theta_j - rate * np.dot(Delta_next.T, A_j)

def three_layer_training(X, Y, Theta_0, Theta_1, Theta_2, iters=5000, rate=0.9):
    A_0 = add_bias(X)    
    costs = []
    for i in range(iters):
        A_1 = add_bias(compute_layer(A_0, Theta_0))
        A_2 = add_bias(compute_layer(A_1, Theta_1))
        A_3 = compute_layer(A_2, Theta_2)
        
        cost = cost_function(A_3, Y)
        print('Cost is now:', cost)
        costs.append(cost)
        
        Delta_3 = output_delta(A_3, Y)
        Delta_2 = hidden_delta(A_2, Delta_3, Theta_2)[:,1:]
        Delta_1 = hidden_delta(A_1, Delta_2, Theta_1)[:,1:]
        
        Theta_2 = weight_update(A_2, Delta_3, Theta_2, rate)
        Theta_1 = weight_update(A_1, Delta_2, Theta_1, rate)
        Theta_0 = weight_update(A_0, Delta_1, Theta_0, rate)
    plt.plot(costs)
    plt.show()
    return [Theta_0, Theta_1, Theta_2]

def one_hot(t):
    one_hot = np.zeros((len(t), 10))
    one_hot[np.arange(len(t)), t] = 1
    return one_hot
  
def validate(A, Y):
    return np.sum((np.argmax(A, axis=1) == np.argmax(Y, axis=1))) / Y.shape[0]

train_targets = one_hot(t_train)
test_targets = one_hot(t_test)

Theta = n_layer_init(layer_sizes=(784, 300, 100, 10))
Theta = three_layer_training(x_train, train_targets, Theta[0], Theta[1], Theta[2], 200, 0.000005)

output = n_layer_output(x_train, Theta)
targets = one_hot(t_train)
print(f'Here\'s how the network did on the train set: {validate(output, targets)}')

output = n_layer_output(x_test, Theta)
targets = one_hot(t_test)
print(f'Here\'s how the network did on the test set: {validate(output, targets)}')
