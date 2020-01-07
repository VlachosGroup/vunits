.. _release_notes:

Release Notes
*************

Development Branch
------------------
`Development Branch`_

Version 0.0.2
-------------
Jan. 7, 2020

- Saved ``unit_db`` as JSON file for faster initialization.
- Wrote ``vunits.run_tests`` function to simplify running the test suite.
- Added ability to express :class:`~vunits.quantity.Quantity` object as a dict.

Version 0.0.1
-------------
Dec. 26, 2019

- Added :class:`~vunits.quantity.Quantity` class.
- Added unit parser that supports powers, compound units, derived units 
  to determine inputted units.
- Updated constants in :mod:`~vunits.constants` module to use Quantity
  objects.
- Added database with preliminary set of units.
- Added unit tests.
- Created :mod:`~vunits.convert` module for unit conversion and type
  conversion.

Version 0.0.0
-------------
Dec. 9, 2019

- Duplicated `pMuTT.constants`_ module

.. _`Development Branch`: https://github.com/VlachosGroup/vunits/commits/development
.. _`pMuTT.constants`: https://vlachosgroup.github.io/pMuTT/constants.html