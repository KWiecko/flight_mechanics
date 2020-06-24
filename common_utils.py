import numpy as np


def get_q(rho_inf: float, v_inf: float):
    q = rho_inf * v_inf ** 2 / 2
    return q


def get_ma(v_inf: float, a_inf: float) -> float:
    mainf = v_inf / a_inf
    return mainf


def get_a_inf(t_inf: float, kappa: float = 1.4, gas_const: float = 287.95) -> float:
    ainf = np.sqrt(kappa * gas_const * t_inf)
    return ainf


def get_vinf_frm_ainf_a_mainf(a_inf: float, ma_inf: float) -> float:

    vinf = ma_inf * a_inf
    return vinf


def get_ma_frm_air_props(
        v_inf: float, t_inf: float, kappa: float = 1.4,
        gas_const: float = 287.95) -> float:

    ainf = v_inf / get_a_inf(t_inf=t_inf, kappa=kappa, gas_const=gas_const)
    return ainf


def get_kin_visc_frm_dyn_visc(visc_dyn: float, rho_inf: float) -> float:
    return visc_dyn / rho_inf


def get_re_inf(
        v_inf: float, l_ref: float, visc_dyn: float = None, rho_inf: float = None,
        visc_kin: float = None) -> float:

    if not visc_kin:
        visc_kin = \
            get_kin_visc_frm_dyn_visc(visc_dyn=visc_dyn, rho_inf=rho_inf)

    reynolds_num = v_inf * l_ref / visc_kin

    return reynolds_num


def get_v_inf_from_re_inf(
        re_inf: float, l_ref: float, visc_dyn: float = None,
        rho_inf: float = None, visc_kin: float = None):

    if not visc_kin:
        visc_kin = \
            get_kin_visc_frm_dyn_visc(visc_dyn=visc_dyn, rho_inf=rho_inf)

    v_inf = re_inf * visc_kin / l_ref
    return v_inf


def get_p_from_ideal_gas_eq(rho: float, gas_const: float, t: float) -> float:

    p = rho * gas_const * t

    return p


def get_t_from_ideal_gas_eq(p: float, gas_const: float, rho: float) -> float:

    t = p / gas_const / rho

    return t


def get_rho_from_ideal_gas_eq_with_a_inf(
        kappa: float, p: float, a: float) -> float:
    rho = kappa * p / a ** 2
    return rho
