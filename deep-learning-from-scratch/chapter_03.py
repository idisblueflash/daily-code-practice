import numpy as np


def step_function_original(x: np.array) -> np.array:
    return None


def step_function_int(x: np.array) -> np.array:
    y = x > 0
    return y.astype(np.int)


def get_ranged_np_array(start: float, end: float, steps: float) -> np.array:
    return np.arange(start, end, steps)


def sigmoid(x: np.array) -> np.array:
    return 1 / (1 + np.exp(-x))
