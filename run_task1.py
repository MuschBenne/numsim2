from scipy.integrate import solve_ivp
from params import PARAMS, IDX, initial_state, T_END
from ode_model import ode_func
import matplotlib.pyplot as plt

sol1 = solve_ivp(ode_func, [0, T_END], initial_state(), args=(PARAMS,), method="LSODA")

# Fall 1: delta_R = 0.2
plt.figure()
plt.plot(sol1.t, sol1.y[IDX["A"]], label="A")
plt.plot(sol1.t, sol1.y[IDX["R"]], label="R")
plt.xlabel("Tid (h)")
plt.ylabel("Mängd (mol)")
plt.title("delta_R = 0.2")
plt.legend()
plt.show()