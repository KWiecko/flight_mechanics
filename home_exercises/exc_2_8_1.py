from common_utils import *


if __name__ == '__main__':

    golf_ball = \
        get_reynolds(v_inf=70, l_ref=0.043, rho_inf=1.2255, dyn_visc=1.81e-5)
    cricket_ball = \
        get_reynolds(v_inf=40, l_ref=0.068, rho_inf=1.2255, dyn_visc=1.81e-5)
    socc_ball = \
        get_reynolds(v_inf=16, l_ref=0.19, rho_inf=1.2255, dyn_visc=1.81e-5)
    baseba_ball = \
        get_reynolds(v_inf=45, l_ref=0.075, rho_inf=1.2255, dyn_visc=1.81e-5)

    for ball_re in [golf_ball, cricket_ball, socc_ball, baseba_ball]:
        print(ball_re)
