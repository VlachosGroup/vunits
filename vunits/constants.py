# -*- coding: utf-8 -*-
"""
vunits.constants

Contains universal constants for catalysis research
"""

import numpy as np
from vunits.db import _temp_units
from vunits.convert import convert_temp
from vunits.quantity import Quantity, _force_get_quantity

R = Quantity.from_units(mag=8.3144598, units='J/mol/K')
""":class:`~vunits.quantity.Quantity`: Molar (univeral or ideal) gas constant
(8.3144598 J/mol/K). Units supported have dimensions of
``energy``/``amount``/``temperature`` or equivalent quantities."""

h = Quantity.from_units(mag=6.626070040e-34, units='J s')
""":class:`~vunits.quantity.Quantity`: Planck's constant (6.626070040e-34 J s).
Units supported have dimensions of ``energy``/``time`` or equivalent
quantities."""

h_bar = h/2./np.pi
r""":class:`~vunits.quantity.Quantity`: Planck's constant divided by
2:math:`\pi` (1.0545718e-34 J s). Units supported have dimensions of
``energy``/``time`` or equivalent quantities."""

kb = Quantity.from_units(mag=1.38064852e-23, units='J/K')
""":class:`~vunits.quantity.Quantity`: Boltzmann constant (1.38064852e-23 J/K).
Units supported have dimensions of ``energy``/``temperature`` or equivalent
quantities."""

c = Quantity.from_units(mag=299792458., units='m/s')
""":class:`~vunits.quantity.Quantity`: Speed of light (299792458 m/s). Units
supported have dimensions of ``length``/``time`` or equivalent quantities."""

m_e = Quantity.from_units(mag=5.48579909070e-4, units='amu')
""":class:`~vunits.quantity.Quantity`: Mass of electron (5.48579909070e-4 amu).
Units supported have dimensions of ``mass`` or equivalent quantities."""

m_p = Quantity.from_units(mag=1.007276466879, units='amu')
""":class:`~vunits.quantity.Quantity`: Mass of proton (1.007276466879e-4 amu).
Units supported have dimensions of ``mass`` or equivalent quantities."""

P0 = Quantity.from_units(mag=1., units='bar')
""":class:`~vunits.quantity.Quantity`: Standard pressure (1 bar). Units
supported have dimensions of ``pressure`` or equivalent quantities."""

T0 = Quantity.from_units(mag=298.15, units='K')
""":class:`~vunits.quantity.Quantity`: Standard temperature (298.15 K). Units
supported have dimensions of ``temperature`` or equivalent quantities."""

V0 = R*T0/P0
""":class:`~vunits.quantity.Quantity`: Standard volume
(0.024789561893699998 m3/mol). Units supported have dimensions of
``volume``/``amount`` or equivalent quantities."""

Na = Quantity(mag=6.02214086e23)
""":class:`~vunits.quantity.Quantity`: Avogadro number (or constant)
(6.02214086e23 molecules/mol). This constant is dimensionless."""

e = Quantity.from_units(mag=1.6021766208e-19, units='C')
""":class:`~vunits.quantity.Quantity`: Charge of electron (1.6021766208e-19 C).
Units supported have dimensions of ``charge`` or equivalent quantities."""