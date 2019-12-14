from vunits.quantity import UnitQuantity, short_prefixes, long_prefixes

derived_quantity = {
    # Time
    's': UnitQuantity(s=1., add_plural=False, add_long_prefix=False),
    'sec': UnitQuantity(s=1., add_short_prefix=False,
                        add_long_prefix=False),
    'second': UnitQuantity(s=1., add_short_prefix=False),
    'min': UnitQuantity(mag=1./60., s=1., add_short_prefix=False),
    'minute': UnitQuantity(mag=1./60., s=1., add_short_prefix=False),
    'hr': UnitQuantity(mag=1./3600., s=1., add_short_prefix=False),
    'hour': UnitQuantity(mag=1./3600., s=1., add_short_prefix=False),
    'day': UnitQuantity(mag=1./3600./24., s=1., add_short_prefix=False),
    'yr': UnitQuantity(mag=1./3600./24./365.25, s=1., add_short_prefix=False),
    'year': UnitQuantity(mag=1./3600./24./365.25, s=1., add_short_prefix=False),
    # Amount
    'mol': UnitQuantity(mol=1.),
    'mole': UnitQuantity(mol=1.),
    'molecule': UnitQuantity(mag=6.02214086e23, mol=1., add_short_prefix=False),
    'molec': UnitQuantity(mag=6.02214086e23, mol=1., add_short_prefix=False,
                          add_plural=False),
    'particle': UnitQuantity(mag=6.02214086e23, mol=1., add_short_prefix=False),
    # Mass
    'g': UnitQuantity(mag=1.e-3, kg=1., add_plural=False),
    'gram': UnitQuantity(mag=1.e-3, kg=1.),
    'u': UnitQuantity(mag=6.022e+26, kg=1., add_short_prefix=False,
                      add_plural=False),
    'amu': UnitQuantity(mag=6.022e+26, kg=1., add_short_prefix=False),
    'Da': UnitQuantity(mag=6.022e+26, kg=1., add_plural=False),
    'dalton': UnitQuantity(mag=6.022e+26, kg=1., add_short_prefix=False),
    'lb': UnitQuantity(mag=2.20462, kg=1., add_short_prefix=False),
    'pound': UnitQuantity(mag=2.20462, kg=1., add_short_prefix=False),
    # Length
    'm': UnitQuantity(m=1., add_plural=False),
    'meter': UnitQuantity(m=1., add_short_prefix=False),
    'in': UnitQuantity(mag=39.3701, m=1., add_short_prefix=False),
    'inch': UnitQuantity(mag=39.3701, m=1., add_short_prefix=False),
    'ft': UnitQuantity(mag=3.28084, m=1., add_short_prefix=False),
    'foot': UnitQuantity(mag=3.28084, m=1., add_short_prefix=False),
    'feet': UnitQuantity(mag=3.28084, m=1., add_short_prefix=False),
    'mile': UnitQuantity(mag=1./1609.344, m=1., add_short_prefix=False),
    'Ang': UnitQuantity(mag=1.e-10, m=1., add_short_prefix=False),
    # Current
    'A': UnitQuantity(A=1., add_long_prefix=False, add_plural=False),
    'ampere': UnitQuantity(A=1., add_short_prefix=False, add_plural=False),
    # Intensity
    'cd': UnitQuantity(cd=1., add_long_prefix=False, add_plural=False),
    'candela': UnitQuantity(cd=1., add_short_prefix=False),
    # Volume
    'L': UnitQuantity(mag=1.e3, m=3., add_long_prefix=False, add_plural=False),
    # Acceleration
    'g0': UnitQuantity(mag=0.101972, m=1., s=-2., add_plural=False,
                       add_long_prefix=False),
    # Force
    'N': UnitQuantity(kg=1., m=1., s=-2., add_long_prefix=False,
                      add_plural=False),
    'newton': UnitQuantity(kg=1., m=1., s=-2., add_short_prefix=True),
    'dyn': UnitQuantity(kg=1., m=1., s=-2., add_long_prefix=False,
                        add_plural=False),
    'dyne': UnitQuantity(kg=1., m=1., s=-2., add_short_prefix=False),
    'lbf': UnitQuantity(mag=0.22481, kg=1., m=1., s=-2.,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    # Energy
    'J': UnitQuantity(kg=1., m=2., s=-2., add_long_prefix=False,
                      add_plural=False),
    'cal': UnitQuantity(mag=0.239006, kg=1., m=2., s=-2., add_long_prefix=False,
                        add_plural=False),
    'eV': UnitQuantity(mag=6.241509e+18, kg=1., m=2., s=-2., add_long_prefix=False,
                       add_plural=False),
    'Latm': UnitQuantity(mag=101.33, kg=1., m=2., s=-2.,
                         add_short_prefix=False, add_long_prefix=False,
                         add_plural=False),
    'Eh': UnitQuantity(mag=2293710448690592., kg=1., m=2., s=-2.,
                       add_long_prefix=False, add_plural=False),
    'Ha': UnitQuantity(mag=2293710448690592., kg=1., m=2., s=-2.,
                       add_long_prefix=False, add_plural=False),
    # Pressure
    'Pa': UnitQuantity(kg=1, m=-1, s=-2, add_long_prefix=False,
                       add_plural=False),
    'atm': UnitQuantity(mag=9.86923e-6, kg=1, m=-1, s=-2,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    'bar': UnitQuantity(mag=1.e-5, kg=1, m=-1, s=-2),
    'mmHg': UnitQuantity(mag=0.00750062, kg=1, m=-1, s=-2,
                         add_short_prefix=False, add_long_prefix=False,
                         add_plural=False),
    'torr': UnitQuantity(mag=0.00750062, kg=1, m=-1, s=-2),
    'Torr': UnitQuantity(mag=0.00750062, kg=1, m=-1, s=-2),
    'psi': UnitQuantity(mag=0.000145038, kg=1, m=-1, s=-2,
                        add_short_prefix=False, add_long_prefix=False,
                        add_plural=False),
    }

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
    _prefix_derived_quantity = {}
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
                _prefix_derived_quantity[new_unit] = new_obj
        # Add long prefixes
        if qty_obj.add_short_prefix:
            for prefix, factor in long_prefixes.items():
                new_unit = '{}{}'.format(prefix, base_unit)
                new_obj = UnitQuantity._from_qty(
                        units=qty_obj.units, mag=qty_obj.mag*factor,
                        add_short_prefix=qty_obj.add_short_prefix,
                        add_long_prefix=qty_obj.add_long_prefix,
                        add_plural=qty_obj.add_plural)
                _prefix_derived_quantity[new_unit] = new_obj

    # Add entries with prefixes
    qty_dict_out = {**qty_dict, **_prefix_derived_quantity}
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
    _plural_derived_quantity = {}
    for base_unit, qty_obj in qty_dict.items():
        # Skip species that do not allow prefixes
        try:
            qty_obj.add_plural
        except AttributeError:
            print(base_unit)
            print(qty_obj.__dict__)
        if not qty_obj.add_plural:
            continue
        new_unit = '{}s'.format(base_unit)
        _plural_derived_quantity[new_unit] = qty_obj
    # Add entries with prefixes
    qty_dict_out = {**qty_dict, **_plural_derived_quantity}
    return qty_dict_out

derived_quantity = _add_prefixes(derived_quantity)
derived_quantity = _add_plural(derived_quantity)