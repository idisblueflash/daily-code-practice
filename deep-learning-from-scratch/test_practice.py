from chapter_02 import and_perceptron, and_perceptron_np, nand_perceptron, \
    or_perceptron_np, xor_perceptron


class TestXORPerceptron:
    def test_0_0_0(self):
        assert xor_perceptron(0, 0) == 0

    def test_1_0_1(self):
        assert xor_perceptron(1, 0) == 1

    def test_0_1_1(self):
        assert xor_perceptron(0, 1) == 1

    def test_1_1_0(self):
        assert xor_perceptron(1, 1) == 0


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
    def test_0_0_1(self):
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
