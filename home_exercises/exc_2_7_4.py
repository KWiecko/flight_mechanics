import pandas as pd
from pprint import pprint
from tabulate import tabulate

from common_utils import *
from drag_utils import *
from lift_utils import *
from converters import UnitsConverter

if __name__ == '__main__':
    all_data = pd.DataFrame({
        'value_name': [
            'w', 'sref', 'ar', 'rho12k', 'ainf12k', 'rho35k', 'ainf35k'],
        'value': [550000, 4600, 9, 1.6e-3, 1069, 7.3e-4, 973],
        'frm_to_units': [
            'lbs_2_kg', 'ft2_2_m2', 'no_unit', 'slugpft3_2_kgpm3', 'ftps_2_mps',
            'slugpft3_2_kgpm3', 'ftps_2_mps']})

    uc = UnitsConverter()

    conv_all_data = \
        uc.convert(in_df=all_data, vals_cn='value', units_cn='frm_to_units')

    raw_conv_vals_series = conv_all_data['conv_value']
    raw_conv_vals_series.index = conv_all_data['value_name']

    CD0 = 0.05
    e = 0.8

    res = {}

    for h_sfx in ['12k', '35k']:
        conv_vals_series = raw_conv_vals_series.copy(deep=True)

        conv_vals_series['vinf{}'.format(h_sfx)] = \
            get_vinf_frm_ainf_a_mainf(
                a_inf=conv_vals_series['ainf{}'.format(h_sfx)], ma_inf=0.85)

        conv_vals_series.index = \
            [el.replace(h_sfx, '') for el in conv_vals_series.index]

        input_kwargs = conv_vals_series.to_dict()

        res['cl_{}'.format(h_sfx)] = get_cl(**input_kwargs) * 9.81

        res['cd_{}'.format(h_sfx)] = \
            get_cd_w_cl(
                cl=res['cl_{}'.format(h_sfx)], cd0=CD0, ar=input_kwargs['ar'],
                e=e)

        res['ld_ratio_{}'.format(h_sfx)] = \
            res['cl_{}'.format(h_sfx)] / res['cd_{}'.format(h_sfx)]

        input_kwargs['cd'] = res['cd_{}'.format(h_sfx)]

        print(h_sfx)
        print(input_kwargs)

        res['req_thrust_{}'.format(h_sfx)] = get_drag(**input_kwargs)
        res['req_thrust_{}_lbf'.format(h_sfx)] = \
            get_drag(**input_kwargs) * uc.units_dict['n_2_lbf']
        res['req_power_{}'.format(h_sfx)] = \
            res['req_thrust_{}'.format(h_sfx)] * input_kwargs['vinf']

        res['req_power_{}_lbffps'.format(h_sfx)] = \
            res['req_thrust_{}'.format(h_sfx)] * input_kwargs['vinf'] * \
            uc.units_dict['n_2_lbf'] * uc.units_dict['mps_2_fps']

    pprint(res)
    print(tabulate(conv_all_data))

