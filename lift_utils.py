import numpy as np

from common_utils import get_q


def get_lift(
        sref: float, cl: float, qinf: float = None, rho: float = None,
        vinf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=vinf)
    lift = qinf * sref * cl
    return lift


def get_lift_coeff(
        w: float, sref: float, qinf: float = None, rho: float = None,
        vinf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=vinf)
    lift_coeff = w / qinf / sref
    return lift_coeff


def get_v_frm_lift(w: float, sref: float, rho: float, cl: float) -> float:

    vinf = np.sqrt(2 * 9.81 * w / rho / sref / cl)

    return vinf


def get_cl_lin(a0: float, alpha: float, alpha_zero_lift: float) -> float:

    cl = a0 * (alpha - alpha_zero_lift) * 0.0174533

    return cl