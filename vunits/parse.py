import re
from vunits.quantity import Quantity
from vunits.quantity_db import derived_quantity

def parse_unit(units='', mag=1.):
    # Separate numerators
    units_list1 = units.split(' ')

    # Separate denominators
    units_list2 = []
    units_pow2 = []
    for coupled_units in units_list1:
        units_list = coupled_units.split('/')
        units_list2.extend(units_list)

        # Add powers
        units_pow = [1] + [-1]*len(units_list2)
        units_pow2.extend(units_pow)

    # Remove powers if any
    units_list3 = []
    units_pow3 = []
    power_pattern = re.compile(r'-*[0-9]+')
    for i, units2 in enumerate(units_list2):
        match = power_pattern.search(units2)
        if match is None:
            power_str = ''
            power_float = float(units_pow2[i])
        else:
            power_str = match.group(0)
            power_float = float(power_str)*units_pow2[i]
        unit = units2.replace(power_str, '')
        units_list3.append(unit)
        units_pow3.append(power_float)

    # Create Quantity object
    quantity_out = Quantity(mag=mag)
    for unit, power in zip(units_list3, units_pow3):
        try:
            quantity_out *= derived_quantity[unit]**power
        except KeyError:
            err_msg = ('When trying to parse "{}", encountered unit "{}", '
                       'which is not supported.'
                       ''.format(units, unit))
            raise ValueError(err_msg)
    return quantity_out
