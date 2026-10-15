def ode_func(t, y, p):
    DA, DR, DA_p, DR_p, MA, A, MR, R, C = y
     
    dDA   = p["thetaA"]*DA_p - p["gammaA"]*DA*A
    dDR   = p["thetaR"]*DR_p - p["gammaR"]*DR*A
    dDA_p = p["gammaA"]*DA*A - p["thetaA"]*DA_p
    dDR_p = p["gammaR"]*DR*A - p["thetaR"]*DR_p
    dMA   = p["alphaA_p"]*DA_p + p["alphaA"]*DA - p["deltaMA"]*MA
    dMR   = p["alphaR_p"]*DR_p + p["alphaR"]*DR - p["deltaMR"]*MR
    dA    = (p["betaA"]*MA + p["thetaA"]*DA_p + p["thetaR"]*DR_p - A*(p["gammaA"]*DA + p["gammaR"]*DR + p["gammaC"]*R + p["deltaA"]))
    dR    = (p["betaR"]*MR - p["gammaC"]*A*R + p["deltaA"]*C - p["deltaR"]*R)
    dC    = p["gammaC"]*A*R - p["deltaA"]*C
    
    return [dDA, dDR, dDA_p, dDR_p, dMA, dA, dMR, dR, dC]