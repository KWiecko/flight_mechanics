from math import pi


from common_utils import get_q


def get_drag_coef_using_lift_coef(
        cl: float, cd0: float, ar: float, e: float) -> float:

    cd = cd0 + cl ** 2 / pi / ar / e
    return cd


def get_drag(
        s_ref: float, cd: float, qinf: float = None, rho: float = None,
        v_inf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=v_inf)
    drag = qinf * s_ref * cd
    return drag


def get_sphere_stokes_drag_coeff(re_inf: float = None) -> float:

    stokes_drag_coeff = 24 / re_inf

    return stokes_drag_coeff
