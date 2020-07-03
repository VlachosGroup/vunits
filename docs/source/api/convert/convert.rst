.. _convert:

Unit Conversions
****************

Here we list functionality converting between units and unit sets.

.. currentmodule:: vunits.convert

Converting units of the same dimensions
---------------------------------------

This section shows API related to converting units of similar sets. For example,
``m/s`` and ``miles/hr`` both have dimensions of ``length``/``time``.

.. autosummary::
   :toctree: same_dim
   :nosignatures:

   convert_temp
   convert_unit
   debye_to_einstein
   einstein_to_debye

--------------------------------------------------------------------------------

Converting units of different dimensions
----------------------------------------

These are conversions between unit sets. For example, finding the vibrational
temperature (dimensions of ``temperature``) to vibrational frequencies
(dimensions of inverse ``time``).

.. autosummary::
   :toctree: diff_dim
   :nosignatures:

   energy_to_freq
   energy_to_temp
   energy_to_wavenumber
   freq_to_energy
   freq_to_temp
   freq_to_wavenumber
   inertia_to_temp
   temp_to_energy
   temp_to_freq
   temp_to_wavenumber
   wavenumber_to_energy
   wavenumber_to_freq
   wavenumber_to_inertia
   wavenumber_to_temp