import numpy as np


def get_breuget_range(
        wto: float, we: float, eta_prop: float, ld_ratio: float,
        qr: float) -> float:
    rt = np.log(wto/we) * eta_prop * ld_ratio * qr / 9.81
    return rt
