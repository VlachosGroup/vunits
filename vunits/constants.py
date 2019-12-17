# -*- coding: utf-8 -*-
"""
vunits.constants

Contains universal constants for catalysis research.
"""

import numpy as np
from vunits.db import _temp_units
from vunits.convert import convert_temp
from vunits.quantity import Quantity, _force_get_quantity

R = Quantity.from_units(mag=8.3144598, units='J/mol/K')
r""":class:`~vunits.quantity.Quantity`: Molar (univeral or ideal) gas constant
(8.3144598 J/mol/K). Units supported have dimensions of
``energy``/``amount``/``temperature`` or equivalent quantities."""

h = Quantity.from_units(mag=6.626070040e-34, units='J s')
r""":class:`~vunits.quantity.Quantity`: Planck's constant (6.626070040e-34 J s).
Units supported have dimensions of ``energy``/``time`` or equivalent
quantities."""

h_bar = h/2./np.pi
r""":class:`~vunits.quantity.Quantity`: Planck's constant divided by
2:math:`\pi` (1.0545718e-34 J s). Units supported have dimensions of
``energy``/``time`` or equivalent quantities."""

kb = Quantity.from_units(mag=1.38064852e-23, units='J/K')
r""":class:`~vunits.quantity.Quantity`: Boltzmann constant (1.38064852e-23 J/K).
Units supported have dimensions of ``energy``/``temperature`` or equivalent
quantities."""

c = Quantity(mag=299792458., m=1., s=-1.)
r""":class:`~vunits.quantity.Quantity`: Speed of light (299792458 m/s). Units
supported have dimensions of ``length``/``time`` or equivalent quantities."""

m_e = Quantity(mag=9.1093837015, kg=1.)
r""":class:`~vunits.quantity.Quantity`: Mass of a electron (9.1093837015 kg).
Units supported have dimensions of ``mass`` or equivalent quantities."""

m_p = Quantity(mag=1.67262192369, kg=1.)
r""":class:`~vunits.quantity.Quantity`: Mass of a proton (1.67262192369 kg).
Units supported have dimensions of ``mass`` or equivalent quantities."""

m_n = Quantity(mag=1.67492749804, kg=1.)
r""":class:`~vunits.quantity.Quantity`: Mass of a neutron (1.67492749804 kg).
Units supported have dimensions of ``mass`` or equivalent quantities."""

P0 = Quantity.from_units(mag=1., units='bar')
r""":class:`~vunits.quantity.Quantity`: Standard pressure (1 bar). Units
supported have dimensions of ``pressure`` or equivalent quantities."""

T0 = Quantity(mag=298.15, K=1.)
r""":class:`~vunits.quantity.Quantity`: Standard temperature (298.15 K). Units
supported have dimensions of ``temperature`` or equivalent quantities."""

V0 = R*T0/P0
r""":class:`~vunits.quantity.Quantity`: Standard volume
(0.024789561893699998 m3/mol). Units supported have dimensions of
``volume``/``amount`` or equivalent quantities."""

N0 = Quantity(mag=6.02214086e23)
r""":class:`~vunits.quantity.Quantity`: Avogadro number
(6.02214086e23 molecules/mol). This constant is dimensionless. Use this value
instead of Avogadro's constant to preserve units."""

Na = Quantity(mag=6.02214086e23, mol=-1.)
r""":class:`~vunits.quantity.Quantity`: Avogadro constant
(6.02214086e23 molecules/mol). Units supported have dimensions of
``amount``\ :sup:`-1`\ ."""

e = Quantity.from_units(mag=1.6021766208e-19, units='C')
r""":class:`~vunits.quantity.Quantity`: Charge of electron (1.6021766208e-19 C).
Units supported have dimensions of ``charge`` or equivalent quantities."""

F = e*Na
r""":class:`~vunits.quantity.Quantity`: Faraday's constant
(96485.33293056407 C/mol). Units supported have dimensions of
``charge``/``amount`` or equivalent quantities."""

G = Quantity(mag=6.67430e-11, m=3., kg=-1., s=-2)
r""":class:`~vunits.quantity.Quantity`: Gravitational constant
(6.67430e-11 m3 kg\ :sup:`-1`\ s\ :sup:`-2`\ ). Units supported have dimensions
of ``volume``/``mass``/``time`` or equivalent quantities."""

eps_0 = Quantity.from_units(8.8541878128e-12, 'F/m')
r""":class:`~vunits.quantity.Quantity`: Vacuum electric permittivity
(8.8541878128e-12 F/m ). Units supported have dimensions
of ``capacitance``/``length`` or equivalent quantities."""

mu_0 = Quantity.from_units(1.25663706212, 'H/m')
r""":class:`~vunits.quantity.Quantity`: Vacuum magnetic permittivity
(1.25663706212 H/m ). Units supported have dimensions
of ``inductance``/``length`` or equivalent quantities."""

R_inf = m_e*e**4/8./eps_0**2/h**2
r""":class:`~vunits.quantity.Quantity`: Rydberg constant
(2.1799233153862138e-18 J). Units supported have dimensions
of ``energy`` or equivalent quantities."""

r_bohr = 4.*np.pi*eps_0*h_bar**2/m_e/e**2
r""":class:`~vunits.quantity.Quantity`: Bohr radius
(5.291648330110941e-11 m). Units supported have dimensions
of ``length`` or equivalent quantities."""