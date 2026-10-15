# params.py
import numpy as np

# Tillståndsordning, används av både ODE och SSA
STATE_NAMES = ["DA", "DR", "DA_p", "DR_p", "MA", "MR", "A", "R", "C"]
IDX = {name: i for i, name in enumerate(STATE_NAMES)}

# Modellparametrar (enheter enligt uppgiften, h^-1 resp. mol^-1 h^-1)
PARAMS = {
    "alphaA": 50.0,   "alphaA_p": 500.0,
    "alphaR": 0.01,   "alphaR_p": 50.0,
    "betaA": 50.0,    "betaR": 5.0,
    "deltaMA": 10.0,  "deltaMR": 0.5,
    "deltaA": 1.0,    "deltaR": 0.2,   # 0.08 i andra fallet
    "gammaA": 1.0,    "gammaR": 1.0,   "gammaC": 2.0,
    "thetaA": 50.0,   "thetaR": 100.0,
}

def initial_state():
    x0 = np.zeros(len(STATE_NAMES))
    x0[IDX["DA"]] = 1
    x0[IDX["DR"]] = 1
    
    return x0

T_END = 200.0   # timmar
SEED = 42

