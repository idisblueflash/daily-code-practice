import numpy as np


def and_perceptron(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    #  tmp = ?
    # return 1 if tmp?theta else 0


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


class TestANDPerceptron:
    def test_0_0_to_0(self):
        assert and_perceptron(0, 0) == 0

    def test_1_0_to_0(self):
        assert and_perceptron(1, 0) == 0

    def test_0_1_to_0(self):
        assert and_perceptron(0, 1) == 0

    def test_1_1_to_1(self):
        assert and_perceptron(1, 1) == 1

    def test_0_0_to_0_np(self):
        assert and_perceptron_np(0, 0) == 0

    def test_1_0_to_0_np(self):
        assert and_perceptron_np(1, 0) == 0

    def test_0_1_to_0_np(self):
        assert and_perceptron_np(0, 1) == 0

    def test_1_1_to_1_np(self):
        assert and_perceptron_np(1, 1) == 1


class TestNANDPerceptron:
    def test_0_0_to_1(self):
        assert nand_perceptron(0, 0) == 1

    def test_1_0_1(self):
        assert nand_perceptron(1, 0) == 1

    def test_0_1_1(self):
        assert nand_perceptron(0, 1) == 1

    def test_1_1_0(self):
        assert nand_perceptron(1, 1) == 0


class TestORPerceptron:
    def test_0_0_0(self):
        assert or_perceptron_np(0, 0) == 0

    def test_1_0_1(self):
        assert or_perceptron_np(1, 0) == 1

    def test_0_1_1(self):
        assert or_perceptron_np(0, 1) == 1

    def test_1_1_1(self):
        assert or_perceptron_np(1, 1) == 1
