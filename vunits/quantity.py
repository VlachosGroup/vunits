import math
from collections import defaultdict

import numpy as np
import pandas as pd

class Quantity:
    """Represents a quantity with units

    Attributes
    ----------
        val : float, optional
            Magnitude of quantity. Default is 1.
        length : float, optional
            Power of length. Default is 0.
        mass : float, optional
            Power of mass. Default is 0.
        time : float, optional
            Power of time. Default is 0.
        current : float, optional
            Power of electric current. Default is 0.
        temperature : float, optional
            Power of temperature. Default is 0.
        amount : float, optional
            Amount of substance. Default is 0.
        intensity : float, optional
            Luminous intensity. Default is 0.
    """

    def __init__(self, mag=1., m=0., kg=0., s=0., A=0., K=0., mol=0.,
                 cd=0., prefix=True):
        self.mag = mag
        self._units = pd.Series(data={'m': m, 'kg': kg, 's': s, 'A': A, 'K': K,
                                      'mol': mol, 'cd': cd})
        self.prefix = prefix

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, val):
        self._units = val

    @property
    def dim(self):
        return pd.Series(data={'length': self.m, 'mass': self.kg,
                               'time': self.s, 'current': self.current,
                               'temperature': self.K, 'amount': self.mol,
                               'intensity': self.cd})

    @property
    def m(self):
        return self._units['m']
    
    @m.setter
    def m(self, val):
        self._units['m'] = val

    @property
    def length(self):
        return self._units['m']
    
    @length.setter
    def length(self, val):
        self._units['m'] = val

    @property
    def kg(self):
        return self._units['kg']
    
    @kg.setter
    def kg(self, val):
        self._units['kg'] = val

    @property
    def mass(self):
        return self._units['kg']
    
    @mass.setter
    def mass(self, val):
        self._units['kg'] = val

    @property
    def s(self):
        return self._units['s']
    
    @s.setter
    def s(self, val):
        self._units['s'] = val

    @property
    def time(self):
        return self._units['s']
    
    @time.setter
    def time(self, val):
        self._units['s'] = val

    @property
    def A(self):
        return self._units['A']
    
    @A.setter
    def A(self, val):
        self._units['A'] = val

    @property
    def current(self):
        return self._units['A']
    
    @current.setter
    def current(self, val):
        self._units['A'] = val

    @property
    def K(self):
        return self._units['K']
    
    @K.setter
    def K(self, val):
        self._units['K'] = val

    @property
    def temperature(self):
        return self._units['K']
    
    @temperature.setter
    def temperature(self, val):
        self._units['K'] = val

    @property
    def mol(self):
        return self._units['mol']
    
    @mol.setter
    def mol(self, val):
        self._units['mol'] = val

    @property
    def amount(self):
        return self._units['mol']
    
    @amount.setter
    def amount(self, val):
        self._units['mol'] = val

    @property
    def cd(self):
        return self._units['cd']
    
    @cd.setter
    def cd(self, val):
        self._units['cd'] = val

    @property
    def intensity(self):
        return self._units['cd']
    
    @intensity.setter
    def intensity(self, val):
        self._units['cd'] = val

    def __pos__(self):
        return Quantity._from_qty(units=self.units, mag=self.mag)
    
    def __neg__(self):
        return Quantity._from_qty(units=self.units, mag=-self.mag)

    def __abs__(self):
        return Quantity._from_qty(units=self.units, mag=np.abs(self.mag))

    def __round__(self):
        return Quantity._from_qty(units=self.units, mag=round(self.mag))

    def __floor__(self):
        return Quantity._from_qty(units=self.units, mag=math.floor(self.mag))

    def __ceil__(self):
        return Quantity._from_qty(units=self.units, mag=math.ceil(self.mag))

    def __trunc__(self):
        return Quantity._from_qty(units=self.units, mag=math.trunc(self.mag))

    def __iadd__(self, other):
        err_msg = ('Addition incompatible due to different units, {} and {}.'
                   ''.format(str(self), str(other)))
        try:
            other_units = other.units
        except AttributeError:
            # If self is dimensionless, add value and return simpler type
            if self._is_dimless():
                self.mag += other
            else:
                raise TypeError(err_msg)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)

            # Create new Quantity object with same units and values added
            self.mag += other.mag
        return self

    def __isub__(self, other):
        self += -other
        return self

    def __imul__(self, other):
        try:
            other_units = other.units
        except AttributeError:
            # If self is dimensionless, add value and return Unit type
            if self._is_dimless():
                self.mag *= other
        else:
            self.units = self.units + other_units
            self.mag *= other.mag
        return self

    def __int__(self):
        return int(self.mag)

    def __float__(self):
        return float(self.mag)

    def __str__(self):
        str_out = str(self.mag)
        for unit, power in self.units.items():
            # Skip if no contribution from quantity
            if power == 0:
                continue
            if np.isclose(power, 1.):
                str_out += ' {}'.format(unit)
            else:
                str_out += ' {}^{}'.format(unit, power)
        return str_out
    
    def add(self, other, unit_obj_out=False, operation='Addition'):
        err_msg = ('{} incompatible due to different units, {} and {}.'
                   ''.format(operation, str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            if not self._is_dimless():
                raise TypeError(err_msg)

            # Add value and return simpler type
            out = self.mag + other
            if unit_obj_out:
                out = Quantity._from_qty(units=self.units, mag=out)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)

            # Create new Quantity object with same units and values added
            out = Quantity._from_qty(units=self.units, mag=self.mag+other.mag)
        return out

    def __add__(self, other):
        return self.add(other=other)

    def __radd__(self, other):
        return self.add(other=other)

    def __sub__(self, other):
        return self.add(other=-other, operation='Subtraction')

    def __rsub__(self, other):
        err_msg = ('Subtraction incompatible due to different units, {} and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, add value and return simpler type
            if not self._is_dimless():
                raise TypeError(err_msg)
            out = other - self.mag
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)
            # Create new Quantity object with same units and values added
            out = Quantity._from_qty(units=self.units, mag=other.mag-self.mag)
        return out

    def __mul__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=self.units, mag=self.mag*other)
        else:
            out_units = self.units + other_units            
            out = Quantity._from_qty(mag=self.mag*other.mag, units=out_units)
        return out
    
    def __rmul__(self, other):
        return self.__mul__(other=other)

    def __floordiv__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=self.units, mag=self.mag//other)
        else:
            out_units = self.units - other_units            
            out = Quantity._from_qty(mag=self.mag//other.mag, units=out_units)
        return out

    def __rfloordiv__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=self.units, mag=other//self.mag)
        else:
            out_units = other_units - self.units
            out = Quantity._from_qty(mag=other.mag//self.mag, units=out_units)
        return out

    def __div__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=self.units, mag=self.mag/other)
        else:
            out_units = self.units - other_units
            out = Quantity._from_qty(mag=self.mag/other.mag, units=out_units)
        return out

    def __rdiv__(self, other):
        other_units = self._get_other_units
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=self.units, mag=other/self.mag)
        else:
            out_units = other_units - self.units
            out = Quantity._from_qty(mag=other.mag/self.mag, units=out_units)
        return out

    def __pow__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            mag = self.mag**other
            units = self.units*other
        elif other._is_dimless():
            mag = self.mag**other.mag
            units = self.units*other.mag
        else:
            err_msg = ('Power operation incompatible exponent with units, {}.'
                       ''.format(str(other)))
            raise TypeError(err_msg)
        out = Quantity._from_qty(mag=mag, units=units)
        return out

    def __lt__(self, other):
        err_msg = ('Less than operation incompatible due to different units, {}'
                   ' and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, compare magnitudes
            if self._is_dimless():
                out = self.mag < other
            else:
                raise TypeError(err_msg)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)
            # Compare magnitudes
            out = self.mag < other.mag
        return out

    def __le__(self, other):
        err_msg = ('Less than or equal to operation incompatible due to '
                   'different units, {} and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, compare magnitudes
            if self._is_dimless():
                out = self.mag <= other
            else:
                raise TypeError(err_msg)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)
            # Compare magnitudes
            out = self.mag <= other.mag
        return out

    def __eq__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, compare magnitudes
            if self._is_dimless():
                out = (self.mag == other)
            else:
                # Quantities not equivalent if self has units
                out = False
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                out = False
            else:
                # Compare magnitudes
                out = (self.mag == other.mag)
        return out

    def __ne__(self, other):
        return (not self == other)

    def __gt__(self, other):
        err_msg = ('Greater than operation incompatible due to different units,'
                   '{} and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, compare magnitudes
            if self._is_dimless():
                out = self.mag > other
            else:
                raise TypeError(err_msg)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)
            # Compare magnitudes
            out = self.mag > other.mag
        return out

    def __ge__(self, other):
        err_msg = ('Greater than or equal to operation incompatible due to '
                   'different units, {} and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            # If self is dimensionless, compare magnitudes
            if self._is_dimless():
                out = self.mag >= other
            else:
                raise TypeError(err_msg)
        else:
            # Check if units are the same
            if not self.units.equals(other_units):
                raise TypeError(err_msg)
            # Compare magnitudes
            out = self.mag >= other.mag
        return out

    def _is_dimless(self):
        return np.allclose(self.dim, np.zeros(len(self.dim)))

    def _get_other_units(self, other):
        try:
            other_units = other.units
        except AttributeError:
            other_units = None
        return other_units

    def __call__(self, units=None):
        if units is None:
            out = self.mag
        else:
            units_obj = Quantity.from_units(units=units)
            if not self.units.equals(units_obj.units):
                err_msg = ('Unit conversion not possible due to '
                           'incompatibility between object\'s units, {}, and '
                           'requested units, {}.'
                           ''.format(str(self), str(units_obj)))
                raise ValueError(err_msg)
            out = (self * units_obj**-1).mag
        return out

    @classmethod
    def from_units(cls, units, mag=1.):
        from vunits.parse import parse_unit
        qty_obj = parse_unit(units=units, mag=mag)
        return cls._from_qty(units=qty_obj.units, mag=qty_obj.mag)


    @classmethod
    def _from_qty(cls, units, mag=1., **kwargs):
        return cls(mag=mag, m=units['m'], kg=units['kg'], s=units['s'],
                   A=units['A'], K=units['K'], mol=units['mol'], cd=units['cd'],
                   **kwargs)

class UnitQuantity(Quantity):
    """Helper class for defining specific units. Inherits from
    :class:`~vunits.quantity.UnitQuantity`"""
    def __init__(self, mag=1., m=0., kg=0., s=0., A=0., K=0., mol=0.,
                 cd=0., add_short_prefix=True, add_long_prefix=True,
                 add_plural=True):
        super().__init__(mag=mag, m=m, kg=kg, s=s, A=A, K=K, mol=mol, cd=cd)
        self.add_short_prefix = add_short_prefix
        self.add_long_prefix = add_long_prefix
        self.add_plural = add_plural

SI_units = ['m', 'kg', 's', 'A', 'K', 'mol', 'cd']
short_prefixes = {'Y': 1.e24, 'Z': 1.e21, 'E': 1.e18, 'P': 1.e15, 'T': 1.e12,
                  'G': 1.e9, 'M': 1.e6, 'k': 1.e3, 'h': 1.e2, 'da': 1.e1,
                  'd': 1.e-1, 'c': 1.e-2, 'm': 1.e-3, 'mu': 1.e-6, 'n': 1.e-9,
                  'p': 1.e-12, 'f': 1.e-15, 'a': 1.e-18, 'z': 1.e-21,
                  'y': 1.e-24}
long_prefixes = {'yotta': 1.e24, 'zetta': 1.e21, 'exa': 1.e18, 'peta': 1.e15,
                 'tera': 1.e12, 'giga': 1.e9, 'mega': 1.e6, 'kilo': 1.e3,
                 'hecto': 1.e2, 'deca': 1.e1, 'deci': 1.e-1, 'centi': 1.e-2,
                 'milli': 1.e-3, 'micro': 1.e-6, 'nano': 1.e-9, 'pico': 1.e-12,
                 'femto': 1.e-15, 'atto': 1.e-18, 'zepto': 1.e-21,
                 'yocto': 1.e-24}