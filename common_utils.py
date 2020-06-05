import numpy as np


def get_q(rho_inf: float, v_inf: float):
    q = rho_inf * v_inf ** 2 / 2
    return q


def get_ma(v_inf: float, a_inf: float) -> float:
    mainf = v_inf / a_inf
    return mainf


def get_ainf(t_inf: float, kappa: float = 1.4, rconst: float = 287.95) -> float:
    ainf = np.sqrt(kappa, rconst, t_inf)
    return ainf


def get_vinf_frm_ainf_a_mainf(a_inf: float, ma_inf: float) -> float:

    vinf = ma_inf * a_inf
    return vinf


def ma_frm_air_props(
        v_inf: float, t_inf: float, kappa: float = 1.4,
        rconst: float = 287.95) -> float:

    ainf = v_inf / get_ainf(t_inf=t_inf, kappa=kappa, rconst=rconst)
    return ainf


def get_kin_visc_frm_dyn_visc(dyn_visc: float, rho_inf: float) -> float:
    return dyn_visc / rho_inf


def get_reynolds(
        v_inf: float, l_ref: float, dyn_visc: float = None, rho_inf: float = None,
        kin_visc: float = None) -> float:

    if not kin_visc:
        kin_visc = \
            get_kin_visc_frm_dyn_visc(dyn_visc=dyn_visc,rho_inf=rho_inf)

    reynolds_num = v_inf * l_ref / kin_visc

    return reynolds_num
