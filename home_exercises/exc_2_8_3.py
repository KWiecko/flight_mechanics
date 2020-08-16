import numpy as np

from common_utils import *
from drag_utils import get_drag, get_cd_w_cl
from lift_utils import get_magnus_force, get_cl_min_pow_sq_polar, get_v_frm_lift
from power_utils import get_power_frm_w_rho_s_cl_cd


if __name__ == '__main__':
    s_ref = 0.3
    w = 3.5
    rho_inf = 1.225
    ar = 10
    e = 0.95
    cd0 = 0.02

    cl_min_pow = get_cl_min_pow_sq_polar(cd0=cd0, ar=ar, e=e)
    print(round(cl_min_pow, 2))

    cd_min_pow = get_cd_w_cl(cl=cl_min_pow, cd0=cd0, ar=ar, e=e)
    print(round(cd_min_pow, 2))

    v_min_pow = \
        get_v_frm_lift(w=w / 9.81, s_ref=s_ref, rho=rho_inf, cl=cl_min_pow)
    print(round(v_min_pow, 2))

    req_trust = \
        get_drag(s_ref=s_ref, cd=cd_min_pow, rho=rho_inf, v_inf=v_min_pow)
    print(round(req_trust, 3))

    req_power = \
        get_power_frm_w_rho_s_cl_cd(
            w=w / 9.81, rho_inf=rho_inf, s_ref=s_ref, cd=cd_min_pow,
            cl=cl_min_pow)

    print(round(req_power, 3))

    pass
