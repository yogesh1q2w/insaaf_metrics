from metrics.f1 import compute_f1
from metrics.rfs import compute_rfs

def compute_lss(df, beta=1):
    f1 = compute_f1(df)
    rfs = compute_rfs(df)
    
    lss_beta = (1 + beta**2)* (f1 * rfs)/((beta **2) * f1 + rfs)
    return lss_beta