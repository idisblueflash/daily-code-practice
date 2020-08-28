from practice import func


def and_perceptron(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    #  tmp = ?
    # return 0 if tmp?theta else 1


class TestANDPerceptron:
    def test_0_0_to_0(self):
        assert and_perceptron(0, 0) == 0

    def test_1_0_to_0(self):
        assert and_perceptron(1, 0) == 0

    def test_0_1_to_0(self):
        assert and_perceptron(0, 1) == 0

    def test_1_1_to_1(self):
        assert and_perceptron(1, 1) == 1
