import math
from collections import defaultdict

import numpy as np
import pandas as pd

class Quantity:
    """Represents a quantity with units

    Attributes
    ----------
        mag : float, optional
            Magnitude of ``Quantity``. Default is 1.
        m : float, optional
            Power of meter (length). Default is 0.
        kg : float, optional
            Power of kilogram (mass). Default is 0.
        s : float, optional
            Power of seconds (time). Default is 0.
        A : float, optional
            Power of amperes (electric current). Default is 0.
        K : float, optional
            Power of Kelvin (temperature). Default is 0.
        mol : float, optional
            Power of moles (amount of substance). Default is 0.
        cd : float, optional
            Power of candela (luminous intensity). Default is 0.
    """

    def __init__(self, mag=1., m=0., kg=0., s=0., A=0., K=0., mol=0.,
                 cd=0.):
        self.mag = mag
        self._units = pd.Series(data={'m': m, 'kg': kg, 's': s, 'A': A, 'K': K,
                                      'mol': mol, 'cd': cd})

    @property
    def units(self):
        """Units of ``Quantity``

        Returns
        -------
            units : (7,) `pd.Series`_
                Powers of units. Columns are labeled with 'm', 'kg', 's', 'A',
                'K', 'mol', 'cd'.

        .. _`pd.Series`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
        """
        return self._units

    @units.setter
    def units(self, val):
        self._units = val

    @property
    def dim(self):
        """Dimensions of ``Quantity``

        Returns
        -------
            dim : (7,) `pd.Series`_
                Powers of units. Columns are labeled with 'length', 'mass',
                'time', 'current', 'temperature', 'amount', 'intensity'.

        .. _`pd.Series`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
        """
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
        """float: Length dimension or ``Quantity``"""
        return self._units['m']
    
    @property
    def kg(self):
        return self._units['kg']
    
    @kg.setter
    def kg(self, val):
        self._units['kg'] = val

    @property
    def mass(self):
        """float: Mass dimension or ``Quantity``"""
        return self._units['kg']

    @property
    def s(self):
        return self._units['s']
    
    @s.setter
    def s(self, val):
        self._units['s'] = val

    @property
    def time(self):
        """float: Time dimension or ``Quantity``"""
        return self._units['s']
    
    @property
    def A(self):
        return self._units['A']
    
    @A.setter
    def A(self, val):
        self._units['A'] = val

    @property
    def current(self):
        """float: Current dimension or ``Quantity``"""
        return self._units['A']
    
    @property
    def K(self):
        return self._units['K']
    
    @K.setter
    def K(self, val):
        self._units['K'] = val

    @property
    def temperature(self):
        """float: Temperature dimension or ``Quantity``"""
        return self._units['K']
    
    @property
    def mol(self):
        return self._units['mol']
    
    @mol.setter
    def mol(self, val):
        self._units['mol'] = val

    @property
    def amount(self):
        """float: Amount dimension or ``Quantity``"""
        return self._units['mol']
    
    @property
    def cd(self):
        return self._units['cd']
    
    @cd.setter
    def cd(self, val):
        self._units['cd'] = val

    @property
    def intensity(self):
        """float: Intensity dimension or ``Quantity``"""
        return self._units['cd']
    
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
            int_power = int(round(power))
            # Skip if no contribution from quantity
            if power == 0:
                continue
            if np.isclose(power, 1.):
                str_out += ' {}'.format(unit)
            elif np.isclose(power, int_power):
                str_out += ' {}^{}'.format(unit, int_power)
            else:
                str_out += ' {}^{}'.format(unit, power)
        return str_out
    
    def add(self, other, return_quantity=True, operation='Addition'):
        """Helper method for addition.

        Parameters
        ----------
            other : :class:`~vunits.quantity.Quantity` or other object
                Variable to add
            return_quantity : bool, optional
                If True, returns a :class:`~vunits.quantity.Quantity` object.
            operation : str, optional
                Operation to apply. Default is 'Addition'.
        Returns
        -------
            out : :class:`~vunits.quantity.Quantity` or other object
                Result of sum.
        """
        err_msg = ('{} incompatible due to different units, {} and {}.'
                   ''.format(operation, str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
            if not self._is_dimless():
                raise TypeError(err_msg)

            # Add value and return simpler type
            out = self.mag + other
            if return_quantity:
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
            # If other is dimensionless, floor divide the magnitude
            out = Quantity._from_qty(units=self.units, mag=other//self.mag)
        else:
            out_units = other_units - self.units
            out = Quantity._from_qty(mag=other.mag//self.mag, units=out_units)
        return out

    def __truediv__(self, other):
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, divide the magnitude
            out = Quantity._from_qty(units=self.units, mag=self.mag/other)
        else:
            out_units = self.units - other_units
            out = Quantity._from_qty(mag=self.mag/other.mag, units=out_units)
        return out

    def __rtruediv__(self, other):
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
        """Check if the :class:`~vunits.quantity.Quantity` is a dimensionless.

        Returns
        -------
            is_dimless : bool
                Returns True if all units are close to 0. Returns False
                otherwise.
        """
        return np.allclose(self.dim, np.zeros(len(self.dim)))

    def _is_temp(self):
        """Check if the :class:`~vunits.quantity.Quantity` is a temperature.

        Returns
        -------
            is_temp : bool
                Returns True if the units have a single power of 'K'. Returns
                False otherwise.
        """
        expected_val = pd.Series(data={'m': 0., 'kg': 0., 's': 0., 'A': 0.,
                                       'K': 1., 'mol': 0., 'cd': 0.})
        return self.units.equals(expected_val)

    def _get_other_units(self, other):
        """Helper method to test if ``other`` is a
        :class:`~vunits.quantity.Quantity` object and get its units.

        Parameters
        ----------
            other : :class:`~vunits.quantity.Quantity` or other object
                Variable to test
        Returns
        -------
            other_units : (7,) `pd.Series`_ or None
                If ``other`` is a :class:`~vunits.quantity.Quantity`, accesses
                ``other.units``. Otherwise return None

        .. _`pd.Series`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
        """
        try:
            other_units = other.units
        except AttributeError:
            other_units = None
        return other_units

    def __call__(self, units=None):
        """Returns quantity magnitude as a float in desired units

        Parameters
        ----------
            units : str, optional
                Desired units to return. Different units must be sparated by a
                ' ' or '/'. Supports powers as numbers after units.
                e.g. 'cm/s2', 'cm s-2', or 'cm s^-2'. If ``units`` is omitted,
                the SI equivalent is returned. ``units`` must correspond to
                the :class:`~vunits.quantity.Quantity` object's dimensions.
        Returns
        -------
            mag : float
                Float of the magnitude in the desired units.
        """
        if units is None:
            # Returns SI value
            out = self.mag
        elif self._is_temp():
            # Is this is a temperature quantity, convert temperature accounting
            # for offsets.
            from vunits.convert import convert_temp
            out = convert_temp(num=self.mag, initial='K', final=units)
        else:
            # Converts to the appropriate unit
            units_obj = Quantity.from_units(units=units)
            if not self.units.equals(units_obj.units):
                err_msg = ('Unit conversion not possible due to '
                           'incompatibility between object\'s units, {}, and '
                           'requested units, {}.'
                           ''.format(str(self), str(units_obj)))
                raise ValueError(err_msg)
            out = (self/units_obj).mag
        return out

    @classmethod
    def from_units(cls, mag=1., units=''):
        """Method to create a :class:`~vunits.quantity.Quantity` by parsing
        units.
        
        Parameters
        ----------
            mag : float, optional
                Magnitude of :class:`~vunits.quantity.Quantity`
            units : str, optional
                Units to parse. Different units must be sparated by a ' ' or
                '/'. Supports powers as numbers after units. e.g. 'cm/s2',
                'cm s-2', or 'cm s^-2'. Default is ''
        Returns
        -------
            quantity : :class:`~vunits.quantity.Quantity`
                New quantity object.
        """
        from vunits.parse import _parse_unit
        qty_obj = _parse_unit(units=units, mag=mag)
        return cls._from_qty(units=qty_obj.units, mag=qty_obj.mag)


    @classmethod
    def _from_qty(cls, units, mag=1., **kwargs):
        """Helper method to create a :class:`~vunits.quantity.Quantity`
        using the magnitude and units.

        Parameters
        ----------
            units : (7,) `pd.Series`_
                Units of the new quantity.
            mag : float, optional
                Magnitude of new quantity. Default is 1.
            kwargs : keyword arguments
                Required for child classes
        Returns
        -------
            quantity : :class:`~vunits.quantity.Quantity`
                New quantity object.

        .. _`pd.Series`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
        """
        return cls(mag=mag, m=units['m'], kg=units['kg'], s=units['s'],
                   A=units['A'], K=units['K'], mol=units['mol'], cd=units['cd'],
                   **kwargs)

class UnitQuantity(Quantity):
    """Helper class for defining specific units for unit parsing. Inherits from
    :class:`~vunits.quantity.Quantity`"""
    def __init__(self, mag=1., m=0., kg=0., s=0., A=0., K=0., mol=0.,
                 cd=0., add_short_prefix=True, add_long_prefix=True,
                 add_plural=True):
        super().__init__(mag=mag, m=m, kg=kg, s=s, A=A, K=K, mol=mol, cd=cd)
        self.add_short_prefix = add_short_prefix
        self.add_long_prefix = add_long_prefix
        self.add_plural = add_plural

def _force_get_quantity(obj, units):
    """Helper method to return :class:`~vunits.quantity.Quantity` object.

    Parameters
    ----------
        obj : float or :class:`~vunits.quantity.Quantity` object
            Object to convert
        units : str
            Units corresponding to ``obj`` if it is not a
            :class:`~vunits.quantity.Quantity` object
    Returns
    -------
        qty : :class:`~vunits.quantity.Quantity` obj
            :class:`~vunits.quantity.Quantity` object corresponding to ``obj``
    """
    if isinstance(obj, Quantity):
        out = obj
    else:
        out = Quantity.from_units(mag=obj, units=units)
    return out

def _return_quantity(quantity, return_quantity, units_out=None):
    """Helper method to return appropriate unit type

    Parameters
    ----------
        quantity : :class:`~vunits.quantity.Quantity` obj
            Quantity object to use
        return_quantity : bool
            If True, returns :class:`~vunits.quantity.Quantity` obj. Otherwise,
            return ``quantity.mag``
        units_out : str, optional
            Units to return. Not required if ``return_quantity`` is True.
    Returns
    -------
        out : :class:`~vunits.quantity.Quantity` obj or float
            Value to return based on ``return_quantity``.
    """
    if return_quantity:
        return quantity
    else:
        return quantity(units_out)

short_prefixes = {'Y': 1.e24, 'Z': 1.e21, 'E': 1.e18, 'P': 1.e15, 'T': 1.e12,
                  'G': 1.e9, 'M': 1.e6, 'k': 1.e3, 'h': 1.e2, 'da': 1.e1,
                  'd': 1.e-1, 'c': 1.e-2, 'm': 1.e-3, 'mu': 1.e-6, 'n': 1.e-9,
                  'p': 1.e-12, 'f': 1.e-15, 'a': 1.e-18, 'z': 1.e-21,
                  'y': 1.e-24}
"""dict: Short prefix used for unit symbols (e.g. km)."""

long_prefixes = {'yotta': 1.e24, 'zetta': 1.e21, 'exa': 1.e18, 'peta': 1.e15,
                 'tera': 1.e12, 'giga': 1.e9, 'mega': 1.e6, 'kilo': 1.e3,
                 'hecto': 1.e2, 'deca': 1.e1, 'deci': 1.e-1, 'centi': 1.e-2,
                 'milli': 1.e-3, 'micro': 1.e-6, 'nano': 1.e-9, 'pico': 1.e-12,
                 'femto': 1.e-15, 'atto': 1.e-18, 'zepto': 1.e-21,
                 'yocto': 1.e-24}
"""dict: Long prefix used for unit descriptions (e.g. kilometer)."""