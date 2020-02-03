import math
from warnings import warn
from collections import defaultdict

import numpy as np
import pandas as pd

HANDLED_FUNCTIONS = {}

class Quantity:
    """Represents a quantity with units

    Attributes
    ----------
        mag : float, optional
            Magnitude of :class:`~vunits.quantity.Quantity`. Default is 1.
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
        # Convert magnitude list to numpy array without altering original list
        mag_in = mag
        if isinstance(mag, list):
            mag_in = np.array(mag)
        self.mag = mag_in
        self._units = pd.Series(data={'m': m, 'kg': kg, 's': s, 'A': A, 'K': K,
                                      'mol': mol, 'cd': cd})

    @property
    def units(self):
        """Units of :class:`~vunits.quantity.Quantity`

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
        """Dimensions of :class:`~vunits.quantity.Quantity`

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
        """float: Length dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['m']
    
    @property
    def kg(self):
        return self._units['kg']
    
    @kg.setter
    def kg(self, val):
        self._units['kg'] = val

    @property
    def mass(self):
        """float: Mass dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['kg']

    @property
    def s(self):
        return self._units['s']
    
    @s.setter
    def s(self, val):
        self._units['s'] = val

    @property
    def time(self):
        """float: Time dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['s']
    
    @property
    def A(self):
        return self._units['A']
    
    @A.setter
    def A(self, val):
        self._units['A'] = val

    @property
    def current(self):
        """float: Current dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['A']
    
    @property
    def K(self):
        return self._units['K']
    
    @K.setter
    def K(self, val):
        self._units['K'] = val

    @property
    def temperature(self):
        """float: Temperature dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['K']
    
    @property
    def mol(self):
        return self._units['mol']
    
    @mol.setter
    def mol(self, val):
        self._units['mol'] = val

    @property
    def amount(self):
        """float: Amount dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['mol']
    
    @property
    def cd(self):
        return self._units['cd']
    
    @cd.setter
    def cd(self, val):
        self._units['cd'] = val

    @property
    def intensity(self):
        """float: Intensity dimension or :class:`~vunits.quantity.Quantity`"""
        return self._units['cd']

    @property
    def units_str(self):
        str_out = ''
        for unit, power in self.units.items():
            int_power = int(round(power))
            # Skip if no contribution from quantity
            if power == 0:
                continue
            # Add unit with appropriate power
            if np.isclose(power, 1.):
                str_out += ' {}'.format(unit)
            elif np.isclose(power, int_power):
                str_out += ' {}^{}'.format(unit, int_power)
            else:
                str_out += ' {}^{}'.format(unit, power)
        # Remove leading space
        str_out = str_out.strip()
        return str_out
    
    def __pos__(self):
        return Quantity._from_qty(units=self.units, mag=self.mag)
    
    def __neg__(self):
        return Quantity._from_qty(units=self.units, mag=-self.mag)

    def __abs__(self):
        return Quantity._from_qty(units=self.units, mag=np.abs(self.mag))

    def __round__(self, n):
        return Quantity._from_qty(units=self.units, mag=round(self.mag, n))

    def __floor__(self):
        return Quantity._from_qty(units=self.units, mag=math.floor(self.mag))

    def __ceil__(self):
        return Quantity._from_qty(units=self.units, mag=math.ceil(self.mag))

    def __trunc__(self):
        return Quantity._from_qty(units=self.units, mag=math.trunc(self.mag))

    def __iadd__(self, other):
        err_msg = ('Addition incompatible due to different units, {} and {}.'
                   ''.format(str(self), str(other)))
        other_units = self._get_other_units(other)
        if other_units is None:
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
        other_units = self._get_other_units(other)
        if other_units is None:
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
        str_out = '{} {}'.format(self.mag, self.units_str)
        return str_out
    
    # def __repr__(self):
    #     return ''

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
            out = Quantity._from_qty(units=-self.units, mag=other//self.mag)
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
        other_units = self._get_other_units(other)
        if other_units is None:
            # If other is dimensionless, add value and return Unit type
            out = Quantity._from_qty(units=-self.units, mag=other/self.mag)
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

    def __array__(self):
        return self.mag
        # if isinstance(self.mag, np.ndarray):
        #     out = self.mag
        # else:
        #     # If magnitude is not a numpy array already
        #     try:
        #         iter(self.mag)
        #     except TypeError:
        #         # If the magnitude is not iterable
        #         out = np.array([self.mag])
        #     else:
        #         out = np.array(self.mag)
        # return out

    # def __array_ufunc__(self, ufunc, method, *args, **kwargs):
    #     if method == '__call__':
    #         args_out = []
    #         for arg in args:
    #             try:
    #                 args_out.append(arg.mag)
    #             except AttributeError:
    #                 args_out.append(arg)
    #         return Quantity._from_qty(units=self.units,
    #                                   mag=ufunc(*args_out, **kwargs))
    #     else:
    #         raise NotImplementedError()

    def __array_function__(self, func, types, args, kwargs):
        if func not in HANDLED_FUNCTIONS:
            raise NotImplementedError()

        return HANDLED_FUNCTIONS[func](*args, **kwargs)

    @classmethod
    def from_units(cls, mag=1., units='', unit_db=None):
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
            unit_db : dict, optional
                Unit database to use parse units. Keys should be strings of
                expected units and values are :class:`~vunits.quantity.Quantity`
                objects. If ``unit_db`` is not specified, uses the
                ``vunits.db.unit_db``.
        Returns
        -------
            quantity : :class:`~vunits.quantity.Quantity`
                New quantity object.
        """
        from vunits.parse import _parse_unit
        qty_obj = _parse_unit(units=units, mag=mag, unit_db=unit_db)
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

    
    def to_dict(self):
        """Represents object as dictionary with JSON-accepted datatypes

        Returns
        -------
            obj_dict : dict
        """
        obj_dict = {
            'class': str(self.__class__),
            'm': self.m,
            'kg': self.kg,
            's': self.s,
            'A': self.A,
            'K': self.K,
            'mol': self.mol,
            'cd': self.cd
        }
        # Create simple type out of magnitude
        try:
            # See if magnitude has to_dict() method
            obj_dict['mag'] = self.mag.to_dict()
        except AttributeError:
            if isinstance(self.mag, np.ndarray):
                obj_dict['mag'] = list(self.mag)
            else:
                obj_dict['mag'] = self.mag

        return obj_dict

    @classmethod
    def from_dict(cls, json_obj):
        """Recreate an object from the JSON representation.

        Parameters
        ----------
            json_obj : dict
                JSON representation
        Returns
        -------
            Obj : Appropriate object
        """
        json_obj.pop('class', None)
        return cls(**json_obj)

class UnitQuantity(Quantity):
    """Helper class for defining specific units for unit parsing. Inherits from
    :class:`~vunits.quantity.Quantity`"""
    def __init__(self, mag=1., m=0., kg=0., s=0., A=0., K=0., mol=0.,
                 cd=0., add_short_prefix=True, add_long_prefix=True,
                 plural_suffix=None):
        super().__init__(mag=mag, m=m, kg=kg, s=s, A=A, K=K, mol=mol, cd=cd)
        self.add_short_prefix = add_short_prefix
        self.add_long_prefix = add_long_prefix
        self.plural_suffix = plural_suffix

def _force_get_quantity(obj, units=''):
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

def _return_quantity(quantity, return_quantity, units_out=''):
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

def implements(np_function):
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func
    return decorator

'''
Sums, products, differences
https://docs.scipy.org/doc/numpy/reference/routines.math.html#sums-products-differences
'''
@implements(np.prod)
def prod(a, **kwargs):
    mag_out = np.prod(a.mag, **kwargs)
    units_out = _get_units_prod(a.mag, mag_out)*a.units
    return Quantity._from_qty(units=units_out, mag=mag_out)

@implements(np.sum)
def sum(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.sum(a.mag, **kwargs))

@implements(np.nanprod)
def nanprod(a, **kwargs):
    mag_out = np.nanprod(a.mag, **kwargs)
    units_out = _get_units_prod(a.mag, mag_out)*a.units
    return Quantity._from_qty(units=units_out, mag=mag_out)

@implements(np.nansum)
def nansum(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.nansum(a.mag, **kwargs))

@implements(np.cumsum)
def cumsum(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.cumprod(a.mag, **kwargs))

@implements(np.nancumsum)
def nancumsum(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.nancumprod(a.mag, **kwargs))

@implements(np.diff)
def diff(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.diff(a.mag, **kwargs))

@implements(np.ediff1d)
def ediff1d(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.ediff1d(a.mag, **kwargs))

'''
Exponents and logarithms
https://docs.scipy.org/doc/numpy/reference/routines.math.html#exponents-and-logarithms
'''
@implements(np.exp)
def exp(x, **kwargs):
    print(x)
    _dimless_warn('numpy.exp', x)
    return Quantity(mag=np.exp(x.mag, **kwargs))

@implements(np.expm1)
def expm1(x, **kwargs):
    _dimless_warn('numpy.expm1', x)
    return Quantity(mag=np.expm1(x.mag, **kwargs))    

@implements(np.exp2)
def exp2(x, **kwargs):
    _dimless_warn('numpy.exp2', x)
    return Quantity(mag=np.exp2(x.mag, **kwargs))    

@implements(np.log)
def log(x, **kwargs):
    _dimless_warn('numpy.log', x)
    return Quantity(mag=np.log(x.mag, **kwargs))

@implements(np.log10)
def log10(x, **kwargs):
    _dimless_warn('numpy.log10', x)
    return Quantity(mag=np.log10(x.mag, **kwargs))

@implements(np.log2)
def log2(x, **kwargs):
    _dimless_warn('numpy.log2', x)
    return Quantity(mag=np.log2(x.mag, **kwargs))

@implements(np.log1p)
def log1p(x, **kwargs):
    _dimless_warn('numpy.log1p', x)
    return Quantity(mag=np.log1p(x.mag, **kwargs))

@implements(np.logaddexp)
def logaddexp(x, **kwargs):
    _dimless_warn('numpy.logaddexp', x)
    return Quantity(mag=np.logaddexp(x.mag, **kwargs))

@implements(np.logaddexp2)
def logaddexp2(x, **kwargs):
    _dimless_warn('numpy.logaddexp2', x)
    return Quantity(mag=np.logaddexp2(x.mag, **kwargs))

@implements(np.trapz)
def trapz(y, x=None, dx=1.):
    try:
        x_units = x.units
    except AttributeError:
        if x is None:
            # If x is not set, infer units from dx
            try:
                x_units = dx.units
            except AttributeError:
                warn_msg = ('Inputted dx variable to numpy.trapz was not a '
                            'Quantity object ({}) so units cannot be inferred. '
                            'Therefore the result will have the same units as '
                            'y.'.format(dx))
                warn(warn_msg)                
                x_units = Quantity().units
        else:
            warn_msg = ('Inputted x variable to numpy.trapz was not a '
                        'Quantity object ({}) so units cannot be inferred. '
                        'Therefore the result will have the same units as '
                        'y.'.format(x))
            warn(warn_msg)                
            x_units = Quantity().units
    units_out = y_units + x_units
    return Quantity._from_qty(mag=np.trapz(y.mag, **kwargs), units=units_out)


'''
Other special functions
https://docs.scipy.org/doc/numpy/reference/routines.math.html#other-special-functions
'''
@implements(np.i0)
def i0(x, **kwargs):
    _dimless_warn('numpy.i0', x)
    return Quantity(mag=np.i0(x.mag, **kwargs))

@implements(np.sinc)
def sinc(x, **kwargs):
    _dimless_warn('numpy.sinc', x)
    return Quantity(mag=np.sinc(x.mag, **kwargs))

'''
Miscellaneous
https://docs.scipy.org/doc/numpy/reference/routines.math.html#miscellaneous
'''
@implements(np.clip)
def clip(a, **kwargs):
    return Quantity._from_qty(units=a.units, mag=np.clip(a.mag, **kwargs))

@implements(np.sqrt)
def sqrt(x, **kwargs):
    units_out = x.units/2.
    return Quantity._from_qty(units=units_out, mag=np.sqrt(x.mag, **kwargs))

@implements(np.cbrt)
def cbrt(x, **kwargs):
    units_out = a.units/3.
    return Quantity._from_qty(units=units_out, mag=np.cbrt(x.mag, **kwargs))

@implements(np.square)
def square(x, **kwargs):
    units_out = x.units*2.
    return Quantity._from_qty(units=units_out, mag=np.square(x.mag, **kwargs))

@implements(np.absolute)
def absolute(x, **kwargs):
    return Quantity._from_qty(units=x.units, mag=np.absolute(x.mag, **kwargs))

@implements(np.fabs)
def fabs(x, **kwargs):
    return Quantity._from_qty(units=x.units, mag=np.fabs(x.mag, **kwargs))

@implements(np.sign)
def sign(x, **kwargs):
    return Quantity(mag=np.sign(x.mag, **kwargs))

@implements(np.heaviside)
def heaviside(x1, x2, **kwargs):
    try:
        x2_mag = x2.mag
    except AttributeError:
        x2_mag = x2
    return Quantity(mag=np.heaviside(x1=x1.mag, x2=x2_mag, **kwargs))

@implements(np.maximum)
def maximum(x, **kwargs):
    return Quantity._from_qty(units=x.units, mag=np.maximum(x.mag, **kwargs))

@implements(np.minimum)
def minimum(x, **kwargs):
    return Quantity._from_qty(units=x.units, mag=np.minimum(x.mag, **kwargs))

@implements(np.fmax)
def fmax(x1, x2, **kwargs):
    x2_units = x1._get_other_units(x2)
    if not x1.equals(x2):
        err_msg = ('Incompatible units between x1 ({}) and x2 ({}) for '
                   'numpy.fmax.'.format(x1, x2))
        raise TypeError(err_msg)
    return Quantity._from_qty(units=x.units,
                              mag=np.fmax(x1.mag, x2.mag, **kwargs))

@implements(np.fmin)
def fmin(x1, x2, **kwargs):
    x2_units = x1._get_other_units(x2)
    if not x1.equals(x2):
        err_msg = ('Incompatible units between x1 ({}) and x2 ({}) for '
                   'numpy.fmin.'.format(x1, x2))
        raise TypeError(err_msg)
    return Quantity._from_qty(units=x.units,
                              mag=np.fmin(x1.mag, x2.mag, **kwargs))

@implements(np.nan_to_num)
def nan_to_num(x, **kwargs):
    return Quantity._from_qty(units=x.units,
                              mag=np.nan_to_num(x.mag, **kwargs))

@implements(np.interp)
def interp(x, xp, fp, **kwargs):
    xp_out = _return_quantity(quantity=xp, return_quantity=False,
                              units_out=x.units_str)
    fp_out = _return_quantity(quantity=fp, return_quantity=False,
                              units_out=None)
    try:
        fp_units = fp.units
    except AttributeError:
        fp_units = ''
    return Quantity.from_units(units=fp_units,
                               mag=np.interp(x.mag, xp=xp, fp=fp_out, **kwargs))


@implements(np.mean)
def mean(a):
    return Quantity._from_qty(units=a.units, mag=np.mean(a.mag, **kwargs))


'''Helper functions'''
def _get_units_prod(array_in, array_out):
    """Helper method calculate units after a product operation
    
    Parameters
    ----------
        array_in : np.ndarray
            Array before product operation
        array_out : np.ndarray, float
            Array after product operation
    Returns
    -------
        n : int
            Factor to multiply units
    """
    try:
        size_out = array_out.size
    except AttributeError:
        # Use 1 if float is returned
        size_out = 1
    return array_in.size/size_out

def _dimless_warn(func_name, quantity):
    """Helper method that warns when mathematical operations expect
    dimensionless quantities but dimensional quantities are passed."""
    a = 1
    if not quantity._is_dimless():
        warn_msg = ('Passed Quantity object with units ({}) to {} '
                    'function. The Quantity object should be dimensionless'
                    ''.format(quantity, func_name))
        warn(warn_msg)