import numpy as np

from common_utils import *
from drag_utils import get_drag, get_sphere_stokes_drag_coeff
from lift_utils import get_magnus_force


if __name__ == '__main__':

    golf_ball = \
        get_re_inf(v_inf=70, l_ref=0.043, rho_inf=1.2255, visc_dyn=1.81e-5)
    cricket_ball = \
        get_re_inf(v_inf=40, l_ref=0.068, rho_inf=1.2255, visc_dyn=1.81e-5)
    socc_ball = \
        get_re_inf(v_inf=16, l_ref=0.19, rho_inf=1.2255, visc_dyn=1.81e-5)
    baseba_ball = \
        get_re_inf(v_inf=45, l_ref=0.075, rho_inf=1.2255, visc_dyn=1.81e-5)

    for ball_re in [golf_ball, cricket_ball, socc_ball, baseba_ball]:
        print(ball_re)

    v_inf = 70
    d_ref = 0.043
    m_ref = 0.064
    aoa_rad = np.deg2rad(30)  # deg
    v_x_inf = v_inf * np.cos(aoa_rad)
    v_y_inf = v_inf * np.sin(aoa_rad)
    s_ref = np.pi * d_ref ** 2 / 4
    rho_inf = 1.225
    visc_dyn = 1.81e-5

    # v_inf: float, l_ref: float, dyn_visc: float = None, rho_inf: float = None,
    # kin_visc: float = None

    re_x = \
        get_re_inf(
            v_inf=v_x_inf, l_ref=d_ref, visc_dyn=visc_dyn, rho_inf=rho_inf)

    # sref: float, cd: float, qinf: float = None, rho: float = None,
    # vinf: float = None, ** kwargs

    cd = 0.25

    drag = get_drag(
        s_ref=s_ref,
        rho=rho_inf,
        v_inf=v_inf,
        cd=cd)

    drag_x = drag * np.cos(aoa_rad)
    drag_y = drag * np.sin(aoa_rad)

    w_ref = 9.81 * m_ref

    print(
        'Drag X: {} | Drag y: {} | Total y: {}'
        .format(drag_x, drag_y, drag_y + w_ref))

    omega_rpm_ref = 1000
    omega_ref = 1000 * 2 * np.pi / 60

    magnus_force = get_magnus_force(
        r_ref=d_ref / 2, rho_inf=rho_inf, omega_ref=omega_ref, v_inf=v_inf)

    print('magnus_force')
    print(magnus_force)

    total_y = magnus_force * np.cos(aoa_rad) - drag_y - w_ref
    total_x = -drag_x - (magnus_force * np.sin(aoa_rad))
    print('total forces')
    print('total_x')
    print(total_x)
    print('total_y')
    print(total_y)

    re_inf_quid = 5e4
    d_ref_quid = 0.032
    v_inf_quid = \
        get_v_inf_from_re_inf(
            re_inf=re_inf_quid, l_ref=d_ref_quid, rho_inf=rho_inf,
            visc_dyn=visc_dyn)

    print('v_inf_quid')
    print(v_inf_quid)
