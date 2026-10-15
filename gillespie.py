import numpy as np
import random



def ssa(prop, stoch, X0, tspan, params):
    t = tspan[0]
    X = np.array(X0)
    sMat = stoch()
    # listor i stället för np.append, annars kopieras hela arrayen varje steg och det blir jättesegt
    tlist = [t]
    Xlist = [X.copy()]
    while t < tspan[1]:
        re = prop(X, params)  # hur "sannolik" varje reaktion är just nu
        a0 = re.sum()  # total takt, alltså hur ofta nåt händer överhuvudtaget
        if a0 <= 1e-10:  # inget kan hända längre, då är vi klara
            print('Simuleringen avslutad vid t=', t)
            break
        # slumpar väntetiden till nästa reaktion (exponentialfördelad), 1-random för att slippa log(0)
        t += -np.log(1-random.random()) / a0
        # lägg reaktionerna efter varandra som bitar på en linjal och kasta en pil, biten den landar i är reaktionen som sker
        # pilen kastas över cumsum[-1] och inte a0, annars kan avrundning göra att den hamnar utanför linjalen
        cre = np.cumsum(re)
        r = np.searchsorted(cre, random.random() * cre[-1], side='right')
        X = X + sMat[r,:]  # uppdatera antalet molekyler enligt den reaktionens rad
        tlist.append(t)
        Xlist.append(X)
    return np.array(tlist), np.array(Xlist)
