from warnings import warn

import numpy as np
from vunits.quantity import Quantity as Qty
from vunits.quantity import _add_units, _sub_units, _mul_units

HANDLED_FUNCTIONS = {}


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
    units_out = _mul_units(a.units, _get_units_prod(a.mag, mag_out))
    return Qty._from_qty(units=units_out, mag=mag_out)

@implements(np.sum)
def sum(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.sum(a.mag, **kwargs))

@implements(np.nanprod)
def nanprod(a, **kwargs):
    mag_out = np.nanprod(a.mag, **kwargs)
    units_out = _mul_units(a.units, _get_units_prod(a.mag, mag_out))
    return Qty._from_qty(units=units_out, mag=mag_out)

@implements(np.nansum)
def nansum(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.nansum(a.mag, **kwargs))

@implements(np.cumsum)
def cumsum(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.cumsum(a.mag, **kwargs))

@implements(np.nancumsum)
def nancumsum(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.nancumsum(a.mag, **kwargs))

@implements(np.diff)
def diff(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.diff(a.mag, **kwargs))

@implements(np.ediff1d)
def ediff1d(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.ediff1d(a.mag, **kwargs))

'''
Exponents and logarithms
https://docs.scipy.org/doc/numpy/reference/routines.math.html#exponents-and-logarithms
'''
@implements(np.exp)
def exp(x, **kwargs):
    _dimless_warn('numpy.exp', x)
    return Qty(mag=np.exp(x.mag, **kwargs))

@implements(np.expm1)
def expm1(x, **kwargs):
    _dimless_warn('numpy.expm1', x)
    return Qty(mag=np.expm1(x.mag, **kwargs))    

@implements(np.exp2)
def exp2(x, **kwargs):
    _dimless_warn('numpy.exp2', x)
    return Qty(mag=np.exp2(x.mag, **kwargs))    

@implements(np.log)
def log(x, **kwargs):
    _dimless_warn('numpy.log', x)
    return Qty(mag=np.log(x.mag, **kwargs))

@implements(np.log10)
def log10(x, **kwargs):
    _dimless_warn('numpy.log10', x)
    return Qty(mag=np.log10(x.mag, **kwargs))

@implements(np.log2)
def log2(x, **kwargs):
    _dimless_warn('numpy.log2', x)
    return Qty(mag=np.log2(x.mag, **kwargs))

@implements(np.log1p)
def log1p(x, **kwargs):
    _dimless_warn('numpy.log1p', x)
    return Qty(mag=np.log1p(x.mag, **kwargs))

@implements(np.logaddexp)
def logaddexp(x, **kwargs):
    _dimless_warn('numpy.logaddexp', x)
    return Qty(mag=np.logaddexp(x.mag, **kwargs))

@implements(np.logaddexp2)
def logaddexp2(x, **kwargs):
    _dimless_warn('numpy.logaddexp2', x)
    return Qty(mag=np.logaddexp2(x.mag, **kwargs))

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
                            'Qty object ({}) so units cannot be inferred. '
                            'Therefore the result will have the same units as '
                            'y.'.format(dx))
                warn(warn_msg)                
                x_units = Qty().units
        else:
            warn_msg = ('Inputted x variable to numpy.trapz was not a '
                        'Qty object ({}) so units cannot be inferred. '
                        'Therefore the result will have the same units as '
                        'y.'.format(x))
            warn(warn_msg)                
            x_units = Qty().units
    units_out = _add_units(y_units, x_units)
    return Qty._from_qty(mag=np.trapz(y.mag, **kwargs), units=units_out)


'''
Other special functions
https://docs.scipy.org/doc/numpy/reference/routines.math.html#other-special-functions
'''
@implements(np.i0)
def i0(x, **kwargs):
    _dimless_warn('numpy.i0', x)
    return Qty(mag=np.i0(x.mag, **kwargs))

@implements(np.sinc)
def sinc(x, **kwargs):
    _dimless_warn('numpy.sinc', x)
    return Qty(mag=np.sinc(x.mag, **kwargs))

'''
Miscellaneous
https://docs.scipy.org/doc/numpy/reference/routines.math.html#miscellaneous
'''
@implements(np.clip)
def clip(a, **kwargs):
    return Qty._from_qty(units=a.units, mag=np.clip(a.mag, **kwargs))

@implements(np.sqrt)
def sqrt(x, **kwargs):
    units_out = _mul_units(x.units, 0.5)
    return Qty._from_qty(units=units_out, mag=np.sqrt(x.mag, **kwargs))

@implements(np.cbrt)
def cbrt(x, **kwargs):
    units_out = _mul_units(a.units, 1./3.)
    return Qty._from_qty(units=units_out, mag=np.cbrt(x.mag, **kwargs))

@implements(np.square)
def square(x, **kwargs):
    units_out = _mul_units(x.units, 2.)
    return Qty._from_qty(units=units_out, mag=np.square(x.mag, **kwargs))

@implements(np.absolute)
def absolute(x, **kwargs):
    return Qty._from_qty(units=x.units, mag=np.absolute(x.mag, **kwargs))

@implements(np.fabs)
def fabs(x, **kwargs):
    return Qty._from_qty(units=x.units, mag=np.fabs(x.mag, **kwargs))

@implements(np.sign)
def sign(x, **kwargs):
    return Qty(mag=np.sign(x.mag, **kwargs))

@implements(np.heaviside)
def heaviside(x1, x2, **kwargs):
    # TODO Check if this requires units
    try:
        x2_mag = x2.mag
    except AttributeError:
        x2_mag = x2
    return Qty(mag=np.heaviside(x1=x1.mag, x2=x2_mag, **kwargs))

@implements(np.maximum)
def maximum(x, **kwargs):
    return Qty._from_qty(units=x.units, mag=np.maximum(x.mag, **kwargs))

@implements(np.minimum)
def minimum(x, **kwargs):
    return Qty._from_qty(units=x.units, mag=np.minimum(x.mag, **kwargs))

@implements(np.fmax)
def fmax(x1, x2, **kwargs):
    x2_units = x1._get_other_units(x2)
    if x1.units != x2_units:
        err_msg = ('Incompatible units between x1 ({}) and x2 ({}) for '
                   'numpy.fmax.'.format(x1, x2))
        raise TypeError(err_msg)
    return Qty._from_qty(units=x.units,
                         mag=np.fmax(x1.mag, x2.mag, **kwargs))

@implements(np.fmin)
def fmin(x1, x2, **kwargs):
    x2_units = x1._get_other_units(x2)
    if x1.units != x2_units:
        err_msg = ('Incompatible units between x1 ({}) and x2 ({}) for '
                   'numpy.fmin.'.format(x1, x2))
        raise TypeError(err_msg)
    return Qty._from_qty(units=x.units,
                         mag=np.fmin(x1.mag, x2.mag, **kwargs))

@implements(np.nan_to_num)
def nan_to_num(x, **kwargs):
    return Qty._from_qty(units=x.units,
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
    return Qty.from_units(units=fp_units,
                          mag=np.interp(x.mag, xp=xp, fp=fp_out, **kwargs))


@implements(np.mean)
def mean(a):
    return Qty._from_qty(units=a.units, mag=np.mean(a.mag, **kwargs))


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
    if not quantity._is_dimless():
        warn_msg = ('Passed {} to {} function. The Quantity object should be '
                    'dimensionless.'
                    ''.format(repr(quantity), func_name))
        warn(warn_msg)