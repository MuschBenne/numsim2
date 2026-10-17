import random
import numpy as np
import matplotlib.pyplot as plt

from params import PARAMS, IDX, initial_state, T_END, SEED
from oscillator_stoch import stoch, prop
from gillespie import ssa

N_RUNS = 5

random.seed(SEED)
runs_1 = []
for _ in range(N_RUNS):
    t, X = ssa(prop, stoch, initial_state(), [0, T_END], PARAMS)
    runs_1.append((t, X))

runs_2 = []
for _ in range(N_RUNS):
    t, X = ssa(prop, stoch, initial_state(), [0, T_END], {**PARAMS, "deltaR": 0.08})
    runs_2.append((t, X))


# Fall 1: delta_R = 0.2
plt.figure()
for t, X in runs_1:
    plt.plot(t, X[:, IDX["A"]], color="tab:blue", alpha=0.6)
    plt.plot(t, X[:, IDX["R"]], color="tab:orange", alpha=0.6)
plt.xlabel("Tid (h)")
plt.ylabel("Antal molekyler")
plt.title("delta_R = 0.2")
plt.show()

plt.figure()
for t, X in runs_2:
    plt.plot(t, X[:, IDX["A"]], color="tab:blue", alpha=0.6)
    plt.plot(t, X[:, IDX["R"]], color="tab:orange", alpha=0.6)
plt.xlabel("Tid (h)")
plt.ylabel("Antal molekyler")
plt.title("delta_R = 0.08")
plt.show()
