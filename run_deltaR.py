import random
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp
from params import PARAMS, IDX, initial_state, T_END, SEED
from ode_model import ode_func
from gillespie import ssa
from oscillator_stoch import stoch, prop

NEW_PARAMS = {**PARAMS, "deltaR": 0.08}

# ODE Solution
ode_sol = solve_ivp(ode_func, [0, T_END], initial_state(), args=(NEW_PARAMS,), method="LSODA",
                    rtol=1e-6, atol=1e-9)  # standardtoleransen ger för få punkter, kantiga toppar

plt.figure()
plt.plot(ode_sol.t, ode_sol.y[IDX["A"]], label="A")
plt.plot(ode_sol.t, ode_sol.y[IDX["R"]], label="R")
plt.xlabel("Tid (h)")
plt.ylabel("Mängd (mol)")
plt.title("delta_R = 0.08")
plt.legend()
plt.show()

# Monte Carlo Solution
N_RUNS = 5

random.seed(SEED)
runs = []
for _ in range(N_RUNS):
    t, X = ssa(prop, stoch, initial_state(), [0, T_END], NEW_PARAMS)
    runs.append((t, X))

plt.figure()
for t, X in runs:
    plt.plot(t, X[:, IDX["A"]], color="tab:blue", alpha=0.6)
    plt.plot(t, X[:, IDX["R"]], color="tab:orange", alpha=0.6)
plt.xlabel("Tid (h)")
plt.ylabel("Antal molekyler")
plt.title("delta_R = 0.08")
plt.show()


