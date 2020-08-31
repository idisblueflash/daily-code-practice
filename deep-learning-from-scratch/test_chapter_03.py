import numpy as np

from chapter_03 import step_function_original, step_function_int


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

