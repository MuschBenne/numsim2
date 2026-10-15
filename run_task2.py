import random
import numpy as np
import matplotlib.pyplot as plt

from params import PARAMS, IDX, initial_state, T_END, SEED
from oscillator_stoch import stoch, prop
from gillespie import ssa

N_RUNS = 5

random.seed(SEED)
runs = []
for _ in range(N_RUNS):
    t, X = ssa(prop, stoch, initial_state(), [0, T_END], PARAMS)
    runs.append((t, X))