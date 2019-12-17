.. _quantity:

Quantity
********

Initializing
------------

A :class:`~vunits.quantity.Quantity` object can represent most physical
quantities as it is based on elementary units (i.e. length, mass, time,
temperature, amount, electric current, and light intensity).

A :class:`~vunits.quantity.Quantity` object can be created manually if one knows
the magnitude and the corresponding SI base units. Below we initialize a
volumetric flow rate to be 10 m\ :sup:`3`\ /s. ::

   >>> from vunits.quantity import Quantity
   >>> vol_flow_rate = Quantity(mag=10., m=3., s=-1)

However, the most convenient way to create :class:`~vunits.quantity.Quantity`
objects is by using ``from_units``. ::

   >>> vol_flow_rate = Quantity.from_units(10., 'm3/s')

See the unit database (units_) for supported units.
Prefixes (such as 'k' for kilo or 'm' for milli) are also supported. Units
should be separated by spaces (' ') or forward slashes ('/'). Powers can be
specified by appending a number with or without a tilda ('^'). Below, we show
statements using ``from_units`` that create the same object as above.::

   >>> vol_flow_rate = Quantity.from_units(10., 'm^3 s-1')
   >>> vol_flow_rate = Quantity.from_units(10000., 'cm^3/ms')

Unit Conversions
----------------

Unit conversions are all handled internally. After a
:class:`~vunits.quantity.Quantity` object is created, you can specify any
equivalent unit by passing the desired unit as a string. For example, below we
convert ``vol_flow_rate`` to ft\ :sup:`3`\ /hr::

   >>> vol_flow_rate('ft3/min')
   21188.802067018023

Units can be compounded as long as the net dimension is equivalent.::

   >>> vol_flow_rate('mile ft km/day')
   1.7613672154617037

Converting the object to a string will give the magnitude and SI base units.::

   >>> str(vol_flow_rate)
   '10.0 m^3 s^-1'

Calling the object without a desired unit set will return a float of the SI
magnitude.::

   >>> vol_flow_rate()
   10.0

An error message will print out if the units are not equivalent.::

   >>> vol_flow_rate('kg/m3')
   ValueError: Unit conversion not possible due to incompatibility between
   object's units, 10.0 m^3 s^-1, and requested units, 1.0 m^-3 kg.

Operations
----------

:class:`~vunits.quantity.Quantity` objects support arithmetic (+, -, *, /, **)
and logical operations (<, >, <=, >=, ==).

Addition and Subtraction
~~~~~~~~~~~~~~~~~~~~~~~~
All unit conversions are done under the hood, allowing two
:class:`~vunits.quantity.Quantity` to be added or subtracted. Below, we add two
volumetric rates.::

   >>> vol_rate1 = Quantity.from_units(1., 'mol/cm3/s')
   >>> vol_rate2 = Quantity.from_units(7200., 'mol/cm3/hr') # 2 mol/cm3/s
   >>> net_vol_rate = vol_rate1 + vol_rate2
   >>> net_vol_rate('mol/cm3/s')
   3.0

Addition and subtraction are only valid if the dimensions agree. Below, we
try to add a surface rate to a volumetric rate and it throws an error.::

   >>> surf_rate = Quantity.from_units(1., 'mol/cm2/s')
   >>> bad_sum = vol_rate1 + surf_rate
   TypeError: Addition incompatible due to different units,
   999999.9999999999 m^-3 s^-1 mol and 10000.0 m^-2 s^-1 mol.

Similarly, an error will be raised if simple numerical types are added to
:class:`~vunits.quantity.Quantity` object with units.::

   >>> vol_flow_rate + 1.
   TypeError: Addition incompatible due to different units,
   999999.9999999999 m^-3 s^-1 mol and 1.

However, if the :class:`~vunits.quantity.Quantity` object is dimensionless, no
error will be thrown but the result will be another
:class:`~vunits.quantity.Quantity` object. Use ``()``, ``float()``, or ``int()``
to convert to the desired type.::

   >>> ratio = Quantity(0.5)
   >>> ratio + 0.2
   <vunits.quantity.Quantity object at 0x000002DFCD2364A8>
   >>> (ratio + 0.2)()
   0.7
   >>> float(ratio + 0.2)
   0.7

Multiplication and Division
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiplying and dividing units will apply the appropriate operations to the
units. Below, we calculate the standard molar volume by importing constants
(which are also :class:`~vunits.quantity.Quantity` objects).::

   >>> from vunits.constants import R, T0, P0
   
   >>> # Standard temperature
   >>> print(T0)
   298.15 K
   
   >>> # Standard pressure
   >>> print(P0)
   100000.0 m^-1.0 kg s^-2.0
   
   >>> # Calculate standard molar volume
   >>> V0 = R*T0/P0
   >>> print(V0)
   0.024789561893699998 m^3.0 mol^-1.0

Multiplying by simpler Python types (like float) will result in the magnitude
changing but remember that unless a unit set is called, it will return a
:class:`~vunits.quantity.Quantity` object.::

   >>> str(100*V0)
   '2.47895618937 m^3 mol^-1'
   >>> 100*V0
   <vunits.quantity.Quantity object at 0x000002DFCD276DD8>

Powers
~~~~~~

Similarly to multiplying and dividing, the power operator (\*\*) will handle
unit conversions appropriately. Below we square the volumetric flow rate from
the unit conversion section.::

   >>> str(vol_flow_rate**2)
   '100.0 m^6 s^-2'

Logical
~~~~~~~

Most of the logical operations (<, >, <=, =>) will only return without errors
if the units are equivalent.::

   >>> vol_rate1 > vol_rate2
   False
   >>> vol_rate1 < vol_rate2
   True
   >>> vol_rate1 >= vol_rate2
   False
   >>> vol_rate1 <= vol_rate2
   True
   >>> vol_rate1 > surf_rate
   TypeError: Greater than operation incompatible due to different units,
   999999.9999999999 m^-3 s^-1 mol and 10000.0 m^-2 s^-1 mol.

However, the equality operators (==, !=), will return never throw errors. 
If both are :class:`~vunits.quantity.Quantity` objects, the units and magnitude
are compared. A dimensionless :class:`~vunits.quantity.Quantity` object can be
compared to elementary types (e.g. float). In this case, the magnitudes are
compared::

   >>> vol_rate1 == vol_rate1
   True
   >>> vol_rate1 == vol_rate2
   False
   >>> vol_rate1 == surf_rate
   False
   >>> vol_rate1 == 1.
   False
   >>> vol_rate1 != 1.
   True

If the :class:`~vunits.quantity.Quantity` object is dimensionless, logical
operators will compare the magnitude.::

   >>> ratio > 0.6
   False
   >>> ratio < 0.6
   True
   >>> ratio == 0.6
   False
   >>> ratio == 0.5
   True
   >>> ratio != 0.6
   True

Docstring
---------

.. autoclass:: vunits.quantity.Quantity
   :members:

.. autoclass:: vunits.quantity.UnitQuantity
   :members: