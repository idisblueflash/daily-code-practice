import numpy as np

from chapter_03 import step_function_original, step_function_int, \
    get_ranged_np_array, sigmoid


class TestStepFunction:
    EXPECTED_INT_LIST = [0, 0, 1]
    EXPECTED_BOOL_LIST = [False, False, True]
    INPUT_LIST = np.array([-1, 0, 1])

    def test_returns_bool_list(self):
        real = list(step_function_original(self.INPUT_LIST))
        assert real == self.EXPECTED_BOOL_LIST

    def test_returns_int_list(self):
        real = list(step_function_int(self.INPUT_LIST))
        assert real == self.EXPECTED_INT_LIST

    def test_returns_int_list_not_bool(self):
        real = list(step_function_int(self.INPUT_LIST))
        str_expected = [str(e) for e in self.EXPECTED_INT_LIST]
        str_real = [str(r) for r in real]
        assert str_expected == str_real


class TestMisc:
    def test_generate_array_by_range(self):
        assert len(get_ranged_np_array(start=-5.0, end=5.0, steps=0.1)) == 100


class TestSigmoid:
    def test_case_1(self):
        x = np.array([-1.0, 1.0, 2.0])
        assert list(sigmoid(x)) == \
               [0.2689414213699951, 0.7310585786300049, 0.8807970779778823]
