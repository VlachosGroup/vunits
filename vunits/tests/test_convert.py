import os
import unittest

import numpy as np
import pandas as pd

from vunits import constants as c


class TestConvert(unittest.TestCase):
    def setUp(self):
        # Read excel sheet with answers
        os.chdir(os.path.dirname(__file__))
        self.ans = pd.read_excel('test_constants.xlsx',
                                 sheet_name='ans',
                                 index_col=0, header=0)

    def test_convert_unit(self):
        # Test all combinations for temperature conversion
        self.assertAlmostEqual(c.convert_unit(c.T0('K'), initial='K', final='C'),
                               self.ans.at['test_convert_unit', 1])
        self.assertAlmostEqual(c.convert_unit(c.T0('K'), initial='K', final='F'),
                               self.ans.at['test_convert_unit', 2])
        self.assertAlmostEqual(c.convert_unit(c.T0('K'), initial='K', final='R'),
                               self.ans.at['test_convert_unit', 3])

        self.assertAlmostEqual(c.convert_unit(c.T0('C'), initial='C', final='K'),
                               self.ans.at['test_convert_unit', 0])
        self.assertAlmostEqual(c.convert_unit(c.T0('C'), initial='C', final='F'),
                               self.ans.at['test_convert_unit', 2])
        self.assertAlmostEqual(c.convert_unit(c.T0('C'), initial='C', final='R'),
                               self.ans.at['test_convert_unit', 3])

        self.assertAlmostEqual(c.convert_unit(c.T0('F'), initial='F', final='K'),
                               self.ans.at['test_convert_unit', 0])
        self.assertAlmostEqual(c.convert_unit(c.T0('F'), initial='F', final='C'),
                               self.ans.at['test_convert_unit', 1])
        self.assertAlmostEqual(c.convert_unit(c.T0('F'), initial='F', final='R'),
                               self.ans.at['test_convert_unit', 3])

        self.assertAlmostEqual(c.convert_unit(c.T0('R'), initial='R', final='K'),
                               self.ans.at['test_convert_unit', 0])
        self.assertAlmostEqual(c.convert_unit(c.T0('R'), initial='R', final='C'),
                               self.ans.at['test_convert_unit', 1])
        self.assertAlmostEqual(c.convert_unit(c.T0('R'), initial='R', final='F'),
                               self.ans.at['test_convert_unit', 2])

        # Test a unit conversion with multiple-based units
        self.assertAlmostEqual(c.convert_unit(initial='m', final='cm'),
                               self.ans.at['test_convert_unit', 4])
        # Test if error raised when units in different set
        with self.assertRaises(ValueError):
            c.convert_unit(initial='cm', final='J')
        # Test if error raised when unaccepted unit inputted
        with self.assertRaises(ValueError):
            c.convert_unit(initial='arbitrary unit', final='J')
        with self.assertRaises(ValueError):
            c.convert_unit(initial='cm', final='arbitrary unit')

    def test_energy_to_freq(self):
        E_J = c.convert_unit(0.1, initial='eV', final='J')
        self.assertAlmostEqual(c.energy_to_freq(E_J),
                               self.ans.at['test_energy_to_freq', 0])

    def test_energy_to_temp(self):
        E_J = c.convert_unit(0.1, initial='eV', final='J')
        self.assertAlmostEqual(c.energy_to_temp(E_J),
                               self.ans.at['test_energy_to_temp', 0])

    def test_energy_to_wavenumber(self):
        E_J = c.convert_unit(0.1, initial='eV', final='J')
        self.assertAlmostEqual(c.energy_to_wavenumber(E_J),
                               self.ans.at['test_energy_to_wavenumber', 0])

    def test_freq_to_energy(self):
        self.assertAlmostEqual(c.freq_to_energy(2.42E+13),
                               self.ans.at['test_freq_to_energy', 0])

    def test_freq_to_temp(self):
        self.assertAlmostEqual(c.freq_to_temp(2.42E+13),
                               self.ans.at['test_freq_to_temp', 0])

    def test_freq_to_wavenumber(self):
        self.assertAlmostEqual(c.freq_to_wavenumber(2.42E+13),
                               self.ans.at['test_freq_to_wavenumber', 0])

    def test_inertia_to_temp(self):
        self.assertAlmostEqual(c.inertia_to_temp(7.20E-46),
                               self.ans.at['test_inertia_to_temp', 0])

    def test_temp_to_energy(self):
        self.assertAlmostEqual(c.temp_to_energy(1160.),
                               self.ans.at['test_temp_to_energy', 0])

    def test_temp_to_freq(self):
        self.assertAlmostEqual(c.temp_to_freq(1160.),
                               self.ans.at['test_temp_to_freq', 0])

    def test_temp_to_wavenumber(self):
        self.assertAlmostEqual(c.temp_to_wavenumber(1160.),
                               self.ans.at['test_temp_to_wavenumber', 0])

    def test_wavenumber_to_energy(self):
        self.assertAlmostEqual(c.wavenumber_to_energy(810.),
                               self.ans.at['test_wavenumber_to_energy', 0])

    def test_wavenumber_to_freq(self):
        self.assertAlmostEqual(c.wavenumber_to_freq(810.),
                               self.ans.at['test_wavenumber_to_freq', 0])

    def test_wavenumber_to_inertia(self):
        self.assertAlmostEqual(c.wavenumber_to_inertia(810.),
                               self.ans.at['test_wavenumber_to_inertia', 0])
    
    def test_wavenumber_to_temp(self):
        self.assertAlmostEqual(c.wavenumber_to_temp(810.),
                               self.ans.at['test_wavenumber_to_temp', 0])

    def test_debye_to_einstein(self):
        self.assertAlmostEqual(c.debye_to_einstein(215.),
                               self.ans.at['test_debye_to_einstein', 0])

    def test_einstein_to_debye(self):
        self.assertAlmostEqual(c.einstein_to_debye(175.),
                               self.ans.at['test_einstein_to_debye', 0])

if __name__ == '__main__':
    unittest.main()