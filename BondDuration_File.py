def getBondDuration(y, face, couponRate, m, ppy=1):
    import numpy as np
    periods = ppy * m
    cf_per_period = couponRate * face / ppy
    t = np.arange(1, periods + 1)
    pv_factors = (1 + y/ppy) ** (-t)
    pv_coupons = cf_per_period * pv_factors
    pv_face = pv_factors[-1] * face
    pvcf = np.sum(pv_coupons) + pv_face
    pvcf_t = np.sum(pv_coupons * t) + pv_face * periods
    duration = pvcf_t / pvcf / ppy
    return duration
