import numpy as np

from common_utils import get_q


def get_lift(
        sref: float, cl: float, qinf: float = None, rho: float = None,
        vinf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=vinf)
    lift = qinf * sref * cl
    return lift


def get_cl(
        w: float, sref: float, qinf: float = None, rho: float = None,
        vinf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=vinf)
    lift_coeff = w / qinf / sref
    return lift_coeff


def get_cl_min_pow_sq_polar(cd0: float, ar: float, e: float) -> float:
    cl = np.sqrt(3 * cd0 * np.pi * ar * e)
    return cl


def get_v_frm_lift(w: float, s_ref: float, rho: float, cl: float) -> float:

    vinf = np.sqrt(2 * 9.81 * w / rho / s_ref / cl)

    return vinf


def get_cl_lin(a0: float, alpha: float, alpha_zero_lift: float) -> float:

    cl = a0 * (alpha - alpha_zero_lift) * 0.0174533

    return cl


def get_magnus_force(
        r_ref: float, rho_inf: float, omega_ref: float, v_inf: float) -> float:

    magnus_force = np.pi ** 2 * r_ref ** 3 * rho_inf * omega_ref * v_inf

    return magnus_force
