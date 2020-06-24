import numpy as np

from common_utils import *

if __name__ == '__main__':

    v_inf = 10
    rho_inf = 0.5
    t_inf = 233
    gas_const = 287
    kappa = 1.4

    p = get_p_from_ideal_gas_eq(rho=rho_inf, gas_const=gas_const, t=t_inf)
    print(p)

    # a_inf = get_a_inf(kappa=kappa, gas_const=gas_const, t_inf=t_inf)
    ma_inf = \
        get_ma_frm_air_props(
            v_inf=v_inf, kappa=kappa, gas_const=gas_const, t_inf=t_inf)
    print(ma_inf)

    # assuming Re1 = Re2 and Ma1 = Ma2
    # from Re1 = Re2 one can show that rho2 = rho1 * l_full / l_model * Ma1 / Ma2
    # so rho2 = rho1 * l_full / l_model * 1
    rho_tunnel = 5 * rho_inf
    p_tunnel = 1e5
    t_tunnel = \
        get_t_from_ideal_gas_eq(rho=rho_tunnel, gas_const=gas_const, p=p_tunnel)

    print('t_tunnel')
    print(t_tunnel)

    a_tunnel = get_a_inf(t_inf=t_tunnel, kappa=kappa, gas_const=gas_const)

    v_inf_tunnel = a_tunnel * ma_inf

    print('v_inf_tunnel')
    print(v_inf_tunnel)

    # from D_full / D_tunnel
    drag_tunnel = 100
    drag_full = \
        rho_inf * v_inf ** 2 / rho_tunnel / v_inf_tunnel ** 2 * 25 * drag_tunnel

    print('drag_full')
    print(drag_full)
