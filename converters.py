import numpy as np
import os
import pandas as pd
import swifter
import yaml


class UnitsConverter:

    @property
    def units_yml_pth(self) -> str:
        return self._units_yml_pth

    @units_yml_pth.setter
    def units_yml_pth(self, new_val: str):
        self._units_yml_pth = new_val

    @property
    def units_dict(self) -> dict:
        return self._units_dict

    @units_dict.setter
    def units_dict(self, new_val: dict):
        self._units_dict = new_val

    def __init__(self, units_yml_pth: str = ''):
        # self.units_yml_pth = units_yml_pth
        self._set_units_yml_pth(units_yml_pth=units_yml_pth)
        self._read_units()

    def _set_units_yml_pth(self, units_yml_pth: str = ''):

        self.units_yml_pth = units_yml_pth
        if not self.units_yml_pth:
            print('Setting default yaml pth')
            curr_f_dir_pth = os.sep.join(str(__file__).split(os.sep)[:-1])
            self.units_yml_pth = '{}/units.yaml'.format(curr_f_dir_pth)

    def _read_units(self):
        try:
            with open(self.units_yml_pth, 'r') as uf:
                self.units_dict = yaml.load(uf)
        except FileNotFoundError as fnf_exc:
            print(fnf_exc)

    def convert(
            self, in_df: pd.DataFrame, vals_cn: str,
            units_cn: str) -> pd.DataFrame:

        in_df['conv_{}'.format(vals_cn)] = \
            in_df[vals_cn] * in_df[units_cn].swifter.apply(
                lambda x: self.units_dict[x])
        return in_df


if __name__ == '__main__':
    pass
