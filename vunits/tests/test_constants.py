# -*- coding: utf-8 -*-
"""
vunits.test_constants
Tests for vunits.constants file
Created on Fri Jul 7 12:31:00 2018
"""
import os
import unittest

import numpy as np
import pandas as pd

from vunits import constants as c


class TestConstants(unittest.TestCase):

    def setUp(self):
        # Read excel sheet with answers
        os.chdir(os.path.dirname(__file__))
        self.ans = pd.read_excel('test_constants.xlsx',
                                 sheet_name='ans',
                                 index_col=0, header=0)

    def test_R(self):
        # Test R for all units
        self.assertAlmostEqual(c.R('J/mol/K'), self.ans.at['test_R', 0])
        self.assertAlmostEqual(c.R('kJ/mol/K'), self.ans.at['test_R', 1])
        self.assertAlmostEqual(c.R('L kPa/mol/K'), self.ans.at['test_R', 2])
        self.assertAlmostEqual(c.R('cm3 kPa/mol/K'), self.ans.at['test_R', 3])
        self.assertAlmostEqual(c.R('m3 Pa/mol/K'), self.ans.at['test_R', 4])
        self.assertAlmostEqual(c.R('cm3 MPa/mol/K'), self.ans.at['test_R', 5])
        self.assertAlmostEqual(c.R('m3 bar/mol/K'), self.ans.at['test_R', 6])
        self.assertAlmostEqual(c.R('L bar/mol/K'), self.ans.at['test_R', 7])
        self.assertAlmostEqual(c.R('L torr/mol/K'), self.ans.at['test_R', 8])
        self.assertAlmostEqual(c.R('cal/mol/K'), self.ans.at['test_R', 9])
        self.assertAlmostEqual(c.R('kcal/mol/K'), self.ans.at['test_R', 10])
        self.assertAlmostEqual(c.R('L atm/mol/K'), self.ans.at['test_R', 11])
        self.assertAlmostEqual(c.R('cm3 atm/mol/K'), self.ans.at['test_R', 12])
        self.assertAlmostEqual(c.R('eV/K'), self.ans.at['test_R', 13])
        self.assertAlmostEqual(c.R('Eh/K'), self.ans.at['test_R', 14])
        self.assertAlmostEqual(c.R('Ha/K'), self.ans.at['test_R', 15])
        # Test R raises an error when an supported unit is passed
        with self.assertRaises(ValueError):
            c.R('arbitrary unit')

    def test_h(self):
        # Test h for all units (bar=False)
        self.assertAlmostEqual(c.h('J s'), self.ans.at['test_h', 0])
        self.assertAlmostEqual(c.h('kJ s'), self.ans.at['test_h', 1])
        self.assertAlmostEqual(c.h('eV s'), self.ans.at['test_h', 2])
        self.assertAlmostEqual(c.h('Eh s'), self.ans.at['test_h', 3])
        self.assertAlmostEqual(c.h('Ha s'), self.ans.at['test_h', 4])
        # Test h raises an error when an supported unit is passed
        with self.assertRaises(ValueError):
            c.h('arbitrary unit')

    def test_h_bar(self):
        # Test h for all units (bar=True)
        self.assertAlmostEqual(c.h_bar('J s'), self.ans.at['test_h',5])
        self.assertAlmostEqual(c.h_bar('kJ s'), self.ans.at['test_h', 6])
        self.assertAlmostEqual(c.h_bar('eV s'), self.ans.at['test_h', 7])
        self.assertAlmostEqual(c.h_bar('Eh s'), self.ans.at['test_h', 8])
        self.assertAlmostEqual(c.h_bar('Ha s'), self.ans.at['test_h', 9])

    def test_kb(self):
        # Test kb for all units
        self.assertAlmostEqual(c.kb('J/K'), self.ans.at['test_kb', 0])
        self.assertAlmostEqual(c.kb('kJ/K'), self.ans.at['test_kb', 1])
        self.assertAlmostEqual(c.kb('eV/K'), self.ans.at['test_kb', 2])
        self.assertAlmostEqual(c.kb('cal/K'), self.ans.at['test_kb', 3])
        self.assertAlmostEqual(c.kb('kcal/K'), self.ans.at['test_kb', 4])
        self.assertAlmostEqual(c.kb('Eh/K'), self.ans.at['test_kb', 5])
        self.assertAlmostEqual(c.kb('Ha/K'), self.ans.at['test_kb', 6])
        # Test kb raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.kb('arbitrary unit')

    def test_c(self):
        # Test c for all units
        self.assertAlmostEqual(c.c('m/s'), self.ans.at['test_c', 0])
        self.assertAlmostEqual(c.c('cm/s'), self.ans.at['test_c', 1])
        # Test c raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.c('arbitrary unit')

    def test_m_e(self):
        # Test m_e for all units
        self.assertAlmostEqual(c.m_e('kg'), self.ans.at['test_m_e', 0])
        self.assertAlmostEqual(c.m_e('g'), self.ans.at['test_m_e', 1])
        self.assertAlmostEqual(c.m_e('amu'), self.ans.at['test_m_e', 2])
        # Test m_e raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.m_e('arbitrary unit')

    def test_m_p(self):
        # Test m_p for all units
        self.assertAlmostEqual(c.m_p('kg'), self.ans.at['test_m_p', 0])
        self.assertAlmostEqual(c.m_p('g'), self.ans.at['test_m_p', 1])
        self.assertAlmostEqual(c.m_p('amu'), self.ans.at['test_m_p', 2])
        # Test m_p raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.m_p('arbitrary unit')

    def test_P0(self):
        # Test P0 for all units
        self.assertAlmostEqual(c.P0('bar'), self.ans.at['test_P0', 0])
        self.assertAlmostEqual(c.P0('atm'), self.ans.at['test_P0', 1])
        self.assertAlmostEqual(c.P0('Pa'), self.ans.at['test_P0', 2])
        self.assertAlmostEqual(c.P0('kPa'), self.ans.at['test_P0', 3])
        self.assertAlmostEqual(c.P0('MPa'), self.ans.at['test_P0', 4])
        self.assertAlmostEqual(c.P0('psi'), self.ans.at['test_P0', 5])
        self.assertAlmostEqual(c.P0('mmHg'), self.ans.at['test_P0', 6])
        self.assertAlmostEqual(c.P0('torr'), self.ans.at['test_P0', 7])
        # Test P0 raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.P0('arbitrary unit')

    def test_T0(self):
        # Test T0 for all units
        self.assertAlmostEqual(c.T0('K'), self.ans.at['test_T0', 0])
        self.assertAlmostEqual(c.T0('C'), self.ans.at['test_T0', 1])
        self.assertAlmostEqual(c.T0('R'), self.ans.at['test_T0', 2])
        self.assertAlmostEqual(c.T0('F'), self.ans.at['test_T0', 3])
        # Test T0 raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.T0('arbitrary unit')

    def test_V0(self):
        # Test V0 for all units
        self.assertAlmostEqual(c.V0('m3/mol'), self.ans.at['test_V0', 0])
        self.assertAlmostEqual(c.V0('cm3/mol'), self.ans.at['test_V0', 1])
        self.assertAlmostEqual(c.V0('mL/mol'), self.ans.at['test_V0', 2])
        self.assertAlmostEqual(c.V0('L/mol'), self.ans.at['test_V0', 3])
        # Test V0 raises an error when an unsupported unit is passed
        with self.assertRaises(ValueError):
            c.V0('arbitrary unit')

if __name__ == '__main__':
    unittest.main()
