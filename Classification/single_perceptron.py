# assuming two inputs
# output = f(x1 * w1 + x2 * w2 + bias)
# where x = inputs and w = weight

# to update the weights and bias
# new weight = old weight + learning rate * input * (difference in desired and actual output)
# new bias = old bias + learning rate * (difference in desired and actual output)
# obv only update if actual output is incorrect


import math
from enum import Enum


# tbh there probably is a better python way to do this but me dumb
# only threshold is tested
class ActivationFunctions(Enum):
    THRESHOLD = 0
    LINEAR = 1
    RELU = 2
    SIGMOID = 3
    TANH = 4


class Perceptron:
    def __init__(self, weights, bias, learning_rate):
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate

    def output(self, input, activation_function):
        x = 0
        print("net = ", end="")
        for i, j in zip(self.weights, input):
            x += i * j
            print("{} * {}".format(i, j), end=" + ")
        x += self.bias
        print("{} = {}".format(self.bias, x))

        if activation_function == ActivationFunctions.THRESHOLD:
            if x >= 0:
                print("y(net) = 1")
                return 1
            else:
                print("y(net) = 0")
                return 0

        elif activation_function == ActivationFunctions.LINEAR:
            print("y(net) = ", x)
            return x

        elif activation_function == ActivationFunctions.RELU:
            if x >= 0:
                print("y(net) = ", x)
                return x
            else:
                print("y(net) = 0")
                return 0

        elif activation_function == ActivationFunctions.SIGMOID:
            print("y(net) = ", 1 / (1 + math.exp(-x)))
            return 1 / (1 + math.exp(-x))

        elif activation_function == ActivationFunctions.TANH:
            print("y(net) = ", (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1))
            return (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)

    def updateParams(self, input, error):

        for i in range(len(self.weights)):
            print("NEW WEIGHT {} = {} + ".format(i + 1, self.weights[i]), end="")
            self.weights[i] += self.learning_rate * input[i] * error
            print(self.learning_rate, "*", input[i], "*", error, " = ", self.weights[i])

        print("NEW BIAS = {} + ".format(self.bias), end="")
        self.bias += self.learning_rate * error
        print(self.learning_rate, "*", error, " = ", self.bias)

    # stop = 0 means train until 100% accuracy
    def train(self, training_inputs, expected_outputs, stop, activation_function):
        done = False
        iterations = 0
        while not done:
            iterations += 1
            total_error = 0.0
            print("-----LOOP {}-----".format(iterations))
            for i, j in zip(training_inputs, expected_outputs):
                print(i)
                actual_output = self.output(i, activation_function)
                if j != actual_output:
                    print("INCORRECT --- DESIRED OUTPUT: {}".format(j))
                    error = j - actual_output
                    self.updateParams(i, error)
                    total_error += abs(error)
                else:
                    print("CORRECT --- NO UPDATE NEEDED")
                print()
            print()
            if iterations == stop or math.isclose(total_error, 0) or iterations == 100:
                done = True
                print("TRAINED {} TIMES".format(iterations))
                print("FINAL WEIGHTS: {}".format(self.weights))
                print("FINAL BIAS: {}".format(self.bias))


training_inputs = [[2, 0], [0, 2], [4, 2], [2, 4]]
expected_outputs = [0, 0, 1, 1]
weights = [0.3, 0.3]
bias = 0.3
learning_rate = 0.6

test = Perceptron(weights, bias, learning_rate)
test.train(training_inputs, expected_outputs, 0, ActivationFunctions.THRESHOLD)
