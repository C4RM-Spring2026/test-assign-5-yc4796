def getBondPrice(y, face, couponRate, m, ppy=1):
    import numpy as np
    periods = ppy * m
    cf_per_period = couponRate * face / ppy
    t = np.arange(1, periods + 1)
    pv_factors = (1 + y/ppy) ** (-t)
    pvcfsum = np.sum(cf_per_period * pv_factors)
    pv_face = pv_factors[-1] * face
    bondprice = pvcfsum + pv_face
    return bondprice
