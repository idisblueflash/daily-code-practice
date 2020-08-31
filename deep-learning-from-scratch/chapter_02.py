import numpy as np


def and_perceptron(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    return 1 if tmp > theta else 0


def general_perceptron_np(x1, x2, w1, w2, b):
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    tmp = np.sum(x * w) + b
    return 1 if tmp > 0 else 0


def and_perceptron_np(x1, x2):
    return general_perceptron_np(x1, x2, w1=0.5, w2=0.5, b=-0.7)


def nand_perceptron(x1, x2):
    return general_perceptron_np(x1, x2, w1=-0.5, w2=-0.5, b=0.7)


def or_perceptron_np(x1, x2):
    return general_perceptron_np(x1, x2, w1=0.5, w2=0.5, b=-0.2)


def xor_perceptron(x1, x2):
    s1 = nand_perceptron(x1, x2)
    s2 = or_perceptron_np(x1, x2)
    return and_perceptron_np(s1, s2)
