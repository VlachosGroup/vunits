.. _db:

Database
********

Miscellaneous databases stored by VUnits.

.. currentmodule:: vunits.db

Unit Database
-------------

This database is responsible for parsing units. The accepted options are
available in :ref:`unit_tables`.

.. autosummary::
   :toctree: unit
   :nosignatures:

   read_unit_db
   write_unit_db

--------------------------------------------------------------------------------

Prefixes
--------

This database is responsible for applying the correct order-of-magnitude
adjustments to the base quantities.

.. autosummary::
   :toctree: prefix
   :nosignatures:

   long_prefixes
   short_prefixes
   
--------------------------------------------------------------------------------

Misc.
-----

These miscellaneous databases store other values useful for processing.


.. autosummary::
   :toctree: misc
   :nosignatures:

   atomic_weight
   symmetry_dict