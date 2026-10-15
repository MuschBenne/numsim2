import numpy as np
from params import STATE_NAMES, IDX

# Reaktionerna från Figur 1, i samma ordning som i prop() nedan.
# Varje reaktion: hur mycket varje ämne ändras när den sker.
REACTIONS = [
    {"A": -1, "R": -1, "C": +1},      # 0:  A + R -> C
    {"A": -1},                        # 1:  A -> ∅
    {"C": -1, "R": +1},               # 2:  C -> R
    {"R": -1},                        # 3:  R -> ∅
    {"DA": -1, "A": -1, "DA_p": +1},  # 4:  DA + A -> DA'
    {"DR": -1, "A": -1, "DR_p": +1},  # 5:  DR + A -> DR'
    {"DA_p": -1, "A": +1, "DA": +1},  # 6:  DA' -> A + DA
    {"MA": +1},                       # 7:  DA -> DA + MA
    {"MA": +1},                       # 8:  DA' -> DA' + MA
    {"MA": -1},                       # 9:  MA -> ∅
    {"A": +1},                        # 10: MA -> A + MA
    {"DR_p": -1, "A": +1, "DR": +1},  # 11: DR' -> A + DR
    {"MR": +1},                       # 12: DR -> DR + MR
    {"MR": +1},                       # 13: DR' -> DR' + MR
    {"MR": -1},                       # 14: MR -> ∅
    {"R": +1},                        # 15: MR -> MR + R
]


def stoch():
    S = np.zeros((len(REACTIONS), len(STATE_NAMES)))
    for r, changes in enumerate(REACTIONS):
        for name, change in changes.items():
            S[r, IDX[name]] = change
    return S


def prop(X, params):
    p = params
    # hämta via namn så att det funkar oavsett ordning i STATE_NAMES
    DA, DR, DA_p, DR_p, MA, A, MR, R, C = (X[IDX[n]] for n in ["DA", "DR", "DA_p", "DR_p", "MA", "A", "MR", "R", "C"])
    return np.array([
        p["gammaC"] * A * R,      # 0
        p["deltaA"] * A,          # 1
        p["deltaA"] * C,          # 2: komplexet bryts ned via A-delen, därför deltaA
        p["deltaR"] * R,          # 3
        p["gammaA"] * DA * A,     # 4
        p["gammaR"] * DR * A,     # 5
        p["thetaA"] * DA_p,       # 6
        p["alphaA"] * DA,         # 7
        p["alphaA_p"] * DA_p,     # 8
        p["deltaMA"] * MA,        # 9
        p["betaA"] * MA,          # 10
        p["thetaR"] * DR_p,       # 11
        p["alphaR"] * DR,         # 12
        p["alphaR_p"] * DR_p,     # 13
        p["deltaMR"] * MR,        # 14
        p["betaR"] * MR,          # 15
    ])
