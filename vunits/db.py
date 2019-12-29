from vunits.quantity import UnitQuantity

short_prefixes = {'Y': 1.e24, 'Z': 1.e21, 'E': 1.e18, 'P': 1.e15, 'T': 1.e12,
                  'G': 1.e9, 'M': 1.e6, 'k': 1.e3, 'h': 1.e2, 'da': 1.e1,
                  'd': 1.e-1, 'c': 1.e-2, 'm': 1.e-3, 'mu': 1.e-6, 'n': 1.e-9,
                  'p': 1.e-12, 'f': 1.e-15, 'a': 1.e-18, 'z': 1.e-21,
                  'y': 1.e-24}
"""dict: Short prefix used for unit symbols (e.g. km). See table of values
in the :ref:`prefix section <prefix_table>`"""

long_prefixes = {'yotta': 1.e24, 'zetta': 1.e21, 'exa': 1.e18, 'peta': 1.e15,
                 'tera': 1.e12, 'giga': 1.e9, 'mega': 1.e6, 'kilo': 1.e3,
                 'hecto': 1.e2, 'deca': 1.e1, 'deci': 1.e-1, 'centi': 1.e-2,
                 'milli': 1.e-3, 'micro': 1.e-6, 'nano': 1.e-9, 'pico': 1.e-12,
                 'femto': 1.e-15, 'atto': 1.e-18, 'zepto': 1.e-21,
                 'yocto': 1.e-24}
"""dict: Long prefix used for unit descriptions (e.g. kilometer). See table of
values in the :ref:`prefix section <prefix_table>`"""

unit_db = {
    # Time
    's': UnitQuantity(s=1., add_plural=False, add_long_prefix=False),
    'sec': UnitQuantity(s=1., add_short_prefix=False,
                        add_long_prefix=False),
    'second': UnitQuantity(s=1., add_short_prefix=False),
    'min': UnitQuantity(mag=60., s=1., add_short_prefix=False),
    'minute': UnitQuantity(mag=60., s=1., add_short_prefix=False),
    'h': UnitQuantity(mag=3600., s=1., add_short_prefix=False),
    'hr': UnitQuantity(mag=3600., s=1., add_short_prefix=False),
    'hour': UnitQuantity(mag=3600., s=1., add_short_prefix=False),
    'day': UnitQuantity(mag=3600.*24., s=1., add_short_prefix=False),
    'week': UnitQuantity(mag=3600.*24.*7., s=1., add_short_prefix=False),
    'yr': UnitQuantity(mag=3600.*24.*365.25, s=1., add_short_prefix=False),
    'year': UnitQuantity(mag=3600.*24.*365.25, s=1., add_short_prefix=False),
    # Amount
    'mol': UnitQuantity(mol=1.),
    'mole': UnitQuantity(mol=1.),
    'molecule': UnitQuantity(mag=1./6.02214086e23, mol=1.,
                             add_short_prefix=False),
    'molec': UnitQuantity(mag=1./6.02214086e23, mol=1., add_short_prefix=False,
                          add_plural=False),
    'particle': UnitQuantity(mag=1./6.02214086e23, mol=1.,
                             add_short_prefix=False),
    # Mass
    'g': UnitQuantity(mag=1.e-3, kg=1., add_plural=False),
    'gram': UnitQuantity(mag=1.e-3, kg=1.),
    'u': UnitQuantity(mag=1./6.022e+26, kg=1., add_short_prefix=False,
                      add_plural=False),
    'amu': UnitQuantity(mag=1./6.022e+26, kg=1., add_short_prefix=False),
    'Da': UnitQuantity(mag=1./6.022e+26, kg=1., add_plural=False),
    'dalton': UnitQuantity(mag=1./6.022e+26, kg=1., add_short_prefix=False),
    'lb': UnitQuantity(mag=1./2.20462, kg=1., add_short_prefix=False),
    'pound': UnitQuantity(mag=1./2.20462, kg=1., add_short_prefix=False),
    # Length
    'm': UnitQuantity(m=1., add_plural=False),
    'meter': UnitQuantity(m=1., add_short_prefix=False),
    'in': UnitQuantity(mag=1./39.3701, m=1., add_short_prefix=False),
    'inch': UnitQuantity(mag=1./39.3701, m=1., add_short_prefix=False),
    'ft': UnitQuantity(mag=1./3.28084, m=1., add_short_prefix=False),
    'foot': UnitQuantity(mag=1./3.28084, m=1., add_short_prefix=False,
                         add_plural=False),
    'feet': UnitQuantity(mag=1./3.28084, m=1., add_short_prefix=False,
                         add_plural=False),
    'mile': UnitQuantity(mag=1609.344, m=1., add_short_prefix=False),
    'Ang': UnitQuantity(mag=1.e-10, m=1., add_short_prefix=False),
    # Temperature
    'K': UnitQuantity(K=1., add_short_prefix=False, add_long_prefix=False,
                      add_plural=False),
    'oC': UnitQuantity(K=1., add_short_prefix=False, add_long_prefix=False,
                      add_plural=False),
    'R': UnitQuantity(mag=1.8, K=1., add_short_prefix=False,
                      add_long_prefix=False, add_plural=False),
    'oF': UnitQuantity(mag=1.8, K=1., add_short_prefix=False,
                       add_long_prefix=False, add_plural=False),
    # Current
    'A': UnitQuantity(A=1., add_long_prefix=False, add_plural=False),
    'ampere': UnitQuantity(A=1., add_short_prefix=False, add_plural=False),
    # Intensity
    'cd': UnitQuantity(cd=1., add_long_prefix=False, add_plural=False),
    'candela': UnitQuantity(cd=1., add_short_prefix=False),
    # Volume
    'L': UnitQuantity(mag=1.e-3, m=3., add_long_prefix=False, add_plural=False),
    'liter': UnitQuantity(mag=1.e-3, m=3., add_short_prefix=False),
    # Acceleration
    'g0': UnitQuantity(mag=9.80665, m=1., s=-2., add_plural=False,
                       add_long_prefix=False),
    # Force
    'N': UnitQuantity(kg=1., m=1., s=-2., add_long_prefix=False,
                      add_plural=False),
    'newton': UnitQuantity(kg=1., m=1., s=-2., add_short_prefix=True),
    'dyn': UnitQuantity(mag=1.e-5, kg=1., m=1., s=-2., add_long_prefix=False,
                        add_plural=False),
    'dyne': UnitQuantity(mag=1.e-5, kg=1., m=1., s=-2., add_short_prefix=False),
    'lbf': UnitQuantity(mag=4.448222, kg=1., m=1., s=-2.,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    # Energy
    'J': UnitQuantity(kg=1., m=2., s=-2., add_long_prefix=False,
                      add_plural=False),
    'joule': UnitQuantity(kg=1., m=2., s=-2., add_short_prefix=False),
    'cal': UnitQuantity(mag=4.184, kg=1., m=2., s=-2., add_long_prefix=False,
                        add_plural=False),
    'eV': UnitQuantity(mag=1.6021766208e-19, kg=1., m=2., s=-2.,
                       add_long_prefix=False, add_plural=False),
    'Latm': UnitQuantity(mag=101.325, kg=1., m=2., s=-2.,
                         add_short_prefix=False, add_long_prefix=False,
                         add_plural=False),
    'Eh': UnitQuantity(mag=4.3597447222071e-18, kg=1., m=2., s=-2.,
                       add_long_prefix=False, add_plural=False),
    'Ha': UnitQuantity(mag=4.3597447222071e-18, kg=1., m=2., s=-2.,
                       add_long_prefix=False, add_plural=False),
    'hartree': UnitQuantity(mag=4.3597447222071e-18, kg=1., m=2., s=-2.,
                            add_short_prefix=False),
    'BTU': UnitQuantity(mag=1055., kg=1., m=2., s=-2, add_short_prefix=False,
                        add_long_prefix=False, add_plural=True),
    # Pressure
    'Pa': UnitQuantity(kg=1, m=-1, s=-2, add_long_prefix=False,
                       add_plural=False),
    'pascal': UnitQuantity(kg=1, m=-1, s=-2, add_short_prefix=False),
    'atm': UnitQuantity(mag=101325., kg=1, m=-1, s=-2,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    'bar': UnitQuantity(mag=1.e5, kg=1, m=-1, s=-2),
    'mmHg': UnitQuantity(mag=133.322, kg=1, m=-1, s=-2,
                         add_short_prefix=False, add_long_prefix=False,
                         add_plural=False),
    'torr': UnitQuantity(mag=133.322, kg=1, m=-1, s=-2),
    'Torr': UnitQuantity(mag=133.322, kg=1, m=-1, s=-2),
    'psi': UnitQuantity(mag=6894.76, kg=1, m=-1, s=-2,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    # Charge
    'C': UnitQuantity(A=1., s=1., add_long_prefix=False, add_plural=False),
    'coulomb': UnitQuantity(A=1., s=1., add_short_prefix=True),
    # Potential difference
    'V': UnitQuantity(kg=1., m=2., s=-3., A=-1., add_long_prefix=False,
                      add_plural=False),
    'volt': UnitQuantity(kg=1., m=2., s=-3., A=-1., add_short_prefix=False),
    # Frequency
    'Hz': UnitQuantity(s=-1, add_long_prefix=False, add_plural=False),
    'hertz': UnitQuantity(s=-1, add_long_prefix=False, add_plural=False),
    # Capacitance
    'F': UnitQuantity(s=4, A=2, m=-2, kg=-1, add_long_prefix=False,
                      add_plural=False),
    'farad': UnitQuantity(s=4, A=2, m=-2, kg=-1, add_short_prefix=False),
    # Electric inductance
    'H': UnitQuantity(kg=1., m=2., s=-2, A=-2, add_long_prefix=False,
                      add_plural=False),
    'henry': UnitQuantity(kg=1., m=2., s=-2, A=-2, add_short_prefix=False),
    # Power
    'W': UnitQuantity(kg=1., m=2, s=-3, add_long_prefix=False,
                      add_plural=False),
    'watt': UnitQuantity(kg=1., m=2, s=-3, add_short_prefix=False),
    # Electric resistance
    'ohm': UnitQuantity(kg=1., m=2, s=-3, A=-2),
    # Magnetic flux density
    'T': UnitQuantity(kg=1., s=-2, A=-1, add_plural=False,
                      add_long_prefix=False),
    'tesla': UnitQuantity(kg=1., s=-2, A=-1, add_short_prefix=False),
    # Magnetic flux
    'Wb': UnitQuantity(kg=1., m=2, s=-2, A=-1, add_long_prefix=False,
                       add_plural=False),
    'weber': UnitQuantity(kg=1., m=2, s=-2, A=-1, add_short_prefix=False),
    }
"""dict: Keys represent units and values represent corresponding
:class:`~vunits.quantity.UnitQuantity` object.

Notes
-----
    See :ref:`units page <unit_tables>` for a complete list of units and the
    :ref:`prefix section <prefix_table>` for supported prefixes.
"""

def _add_prefixes(qty_dict):
    """Helper method to add prefixes to dictionary
    
    Parameters
    ----------
        qty_dict : dict
            Dictionary whose keys are the quantity name and values are the
            :class:`~vunits.quantity.UnitQuantity` objects. If a
            ``UnitQuantity`` has ``add_short_prefix`` set to ``False``,
            prefixes will not be added.
    Returns
    -------
        qty_dict_out : dict
            Dictionary with the updated prefix entries.
    """
    # Add prefixes to dictionary
    _prefix_unit_db = {}
    for base_unit, qty_obj in qty_dict.items():
        # Add short prefixes
        if qty_obj.add_short_prefix:
            for prefix, factor in short_prefixes.items():
                new_unit = '{}{}'.format(prefix, base_unit)
                new_obj = UnitQuantity._from_qty(
                        units=qty_obj.units, mag=qty_obj.mag*factor,
                        add_short_prefix=qty_obj.add_short_prefix,
                        add_long_prefix=qty_obj.add_long_prefix,
                        add_plural=qty_obj.add_plural)
                _prefix_unit_db[new_unit] = new_obj
        # Add long prefixes
        if qty_obj.add_long_prefix:
            for prefix, factor in long_prefixes.items():
                new_unit = '{}{}'.format(prefix, base_unit)
                new_obj = UnitQuantity._from_qty(
                        units=qty_obj.units, mag=qty_obj.mag*factor,
                        add_short_prefix=qty_obj.add_short_prefix,
                        add_long_prefix=qty_obj.add_long_prefix,
                        add_plural=qty_obj.add_plural)
                _prefix_unit_db[new_unit] = new_obj

    # Add entries with prefixes
    qty_dict_out = {**qty_dict, **_prefix_unit_db}
    return qty_dict_out

def _add_plural(qty_dict):
    """Helper method to add plural units to dictionary (e.g. seconds)
    
    Parameters
    ----------
        qty_dict : dict
            Dictionary whose keys are the quantity name and values are the
            :class:`~vunits.quantity.UnitQuantity` objects. If a
            ``UnitQuantity`` has ``add_short_prefix`` set to ``False``,
            prefixes will not be added.
    Returns
    -------
        qty_dict_out : dict
            Dictionary with the updated plural entries.
    """
    # Add prefixes to dictionary
    _plural_unit_db = {}
    for base_unit, qty_obj in qty_dict.items():
        # Skip species that do not allow prefixes
        try:
            qty_obj.add_plural
        except AttributeError:
            pass
        if not qty_obj.add_plural:
            continue
        new_unit = '{}s'.format(base_unit)
        _plural_unit_db[new_unit] = qty_obj
    # Add entries with prefixes
    qty_dict_out = {**qty_dict, **_plural_unit_db}
    return qty_dict_out

# Add prefix and plural entries
unit_db = _add_prefixes(unit_db)
unit_db = _add_plural(unit_db)

_temp_units = ('K', 'R', 'oC', 'oF')
"""tuple: Helper tuple to identify if a unit belongs to temperature."""

symmetry_dict = {
    'C1': 1,
    'Cs': 1,
    'C2': 2,
    'C2v': 2,
    'C3v': 3,
    'Cinfv': 1,
    'D2h': 4,
    'D3h': 6,
    'D5h': 10,
    'Dinfh': 2,
    'D3d': 6,
    'Td': 12,
    'Oh': 24
}
"""dict : Keys are point groups and the values are the symmetry numbers used for
rotational modes."""

atomic_weight = {
    1: 1.008,
    2: 4.002602,
    3: 6.938,
    4: 9.0121831,
    5: 10.806,
    6: 12.0116,
    7: 14.007,
    8: 15.999,
    9: 18.99840316,
    10: 20.1797,
    11: 22.98976928,
    12: 24.305,
    13: 26.9815385,
    14: 28.085,
    15: 30.973762,
    16: 32.06,
    17: 35.45,
    18: 39.948,
    19: 39.0983,
    20: 40.078,
    21: 44.955908,
    22: 47.867,
    23: 50.9415,
    24: 51.9961,
    25: 54.938044,
    26: 55.845,
    27: 58.933194,
    28: 58.6934,
    29: 63.546,
    30: 65.38,
    31: 69.723,
    32: 72.63,
    33: 74.921595,
    34: 78.971,
    35: 79.901,
    36: 83.798,
    37: 85.4678,
    38: 87.62,
    39: 88.90584,
    40: 91.224,
    41: 92.90637,
    42: 95.95,
    43: 98.,
    44: 101.07,
    45: 102.9055,
    46: 106.42,
    47: 107.8682,
    48: 112.414,
    49: 114.818,
    50: 118.71,
    51: 121.76,
    52: 127.6,
    53: 126.90447,
    54: 131.293,
    55: 132.905452,
    56: 137.327,
    57: 138.90547,
    58: 140.116,
    59: 140.90766,
    60: 144.242,
    61: 145,
    62: 150.36,
    63: 151.964,
    64: 157.25,
    65: 158.92535,
    66: 162.5,
    67: 164.93033,
    68: 167.259,
    69: 168.93422,
    70: 173.054,
    71: 174.9668,
    72: 178.49,
    73: 180.94788,
    74: 183.84,
    75: 186.207,
    76: 190.23,
    77: 192.217,
    78: 195.084,
    79: 196.966569,
    80: 200.592,
    81: 204.382,
    82: 207.2,
    83: 208.9804,
    84: 209.,
    85: 210.,
    86: 222.,
    87: 223.,
    88: 226.,
    89: 227.,
    90: 232.0377,
    91: 231.03588,
    92: 238.02891,
    93: 237.,
    94: 244.,
    95: 243.,
    96: 247.,
    97: 247.,
    98: 251.,
    99: 252.,
    100: 257.,
    101: 258.,
    102: 259.,
    103: 262.,
    104: 267.,
    105: 268.,
    106: 271.,
    107: 272.,
    108: 270.,
    109: 276.,
    110: 281.,
    111: 280.,
    112: 285.,
    113: 284.,
    114: 289.,
    115: 288.,
    116: 293.,
    118: 294.,
    'H': 1.008,
    'He': 4.002602,
    'Li': 6.938,
    'Be': 9.0121831,
    'B': 10.806,
    'C': 12.0116,
    'N': 14.007,
    'O': 15.999,
    'F': 18.99840316,
    'Ne': 20.1797,
    'Na': 22.98976928,
    'Mg': 24.305,
    'Al': 26.9815385,
    'Si': 28.085,
    'P': 30.973762,
    'S': 32.06,
    'Cl': 35.45,
    'Ar': 39.948,
    'K': 39.0983,
    'Ca': 40.078,
    'Sc': 44.955908,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938044,
    'Fe': 55.845,
    'Co': 58.933194,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.63,
    'As': 74.921595,
    'Se': 78.971,
    'Br': 79.901,
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.90584,
    'Zr': 91.224,
    'Nb': 92.90637,
    'Mo': 95.95,
    'Tc': 98.,
    'Ru': 101.07,
    'Rh': 102.9055,
    'Pd': 106.42,
    'Ag': 107.8682,
    'Cd': 112.414,
    'In': 114.818,
    'Sn': 118.71,
    'Sb': 121.76,
    'Te': 127.6,
    'I': 126.90447,
    'Xe': 131.293,
    'Cs': 132.905452,
    'Ba': 137.327,
    'La': 138.90547,
    'Ce': 140.116,
    'Pr': 140.90766,
    'Nd': 144.242,
    'Pm': 145.,
    'Sm': 150.36,
    'Eu': 151.964,
    'Gd': 157.25,
    'Tb': 158.92535,
    'Dy': 162.5,
    'Ho': 164.93033,
    'Er': 167.259,
    'Tm': 168.93422,
    'Yb': 173.054,
    'Lu': 174.9668,
    'Hf': 178.49,
    'Ta': 180.94788,
    'W': 183.84,
    'Re': 186.207,
    'Os': 190.23,
    'Ir': 192.217,
    'Pt': 195.084,
    'Au': 196.966569,
    'Hg': 200.592,
    'Tl': 204.382,
    'Pb': 207.2,
    'Bi': 208.9804,
    'Po': 209.,
    'At': 210.,
    'Rn': 222.,
    'Fr': 223.,
    'Ra': 226.,
    'Ac': 227.,
    'Th': 232.0377,
    'Pa': 231.03588,
    'U': 238.02891,
    'Np': 237.,
    'Pu': 244.,
    'Am': 243.,
    'Cm': 247.,
    'Bk': 247.,
    'Cf': 251.,
    'Es': 252.,
    'Fm': 257.,
    'Md': 258.,
    'No': 259.,
    'Lr': 262.,
    'Rf': 267.,
    'Db': 268.,
    'Sg': 271.,
    'Bh': 272.,
    'Hs': 270.,
    'Mt': 276.,
    'Ds': 281.,
    'Rg': 280.,
    'Cn': 285.,
    'Uut': 284.,
    'Fl': 289.,
    'Uup': 288.,
    'Lv': 293.,
    'Uuo': 294.,
}
"""dict : Atomic weight. The key can be the atomic number, the element symbol,
or the element name"""