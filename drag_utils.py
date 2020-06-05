from math import pi


from common_utils import get_q


def get_drag_coef_using_lift_coef(
        cl: float, cd0: float, ar: float, e: float) -> float:

    cd = cd0 + cl ** 2 / pi / ar / e
    return cd


def get_drag(
        sref: float, cd: float, qinf: float = None, rho: float = None,
        vinf: float = None, **kwargs) -> float:

    qinf = qinf if qinf else get_q(rho_inf=rho, v_inf=vinf)
    drag = qinf * sref * cd
    return drag
