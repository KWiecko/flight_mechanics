import numpy as np


def get_power_frm_w_rho_s_cl_cd(
        w: float, rho_inf: float, s_ref: float, cd: float, cl: float):

    power = \
        np.sqrt((2 * (w * 9.81) ** 3) / (rho_inf * s_ref)) * cd * \
        np.power(cl, -1.5)

    return power


