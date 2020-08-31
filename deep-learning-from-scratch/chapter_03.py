import numpy as np


def step_function_original(x: np.array) -> np.array:
    return x > 0


def step_function_int(x: np.array) -> np.array:
    y = x > 0
    return y.astype(np.int)
