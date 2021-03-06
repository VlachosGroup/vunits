Virtual Kinetic Laboratory Units (VUnits)
=========================================

The **V**\ irtual Kinetic Laboratory **Units**\ (VUnits) is a Python library for
unit conversion and constants developed by the Vlachos Research Group at the
University of Delaware. This code supports Python-based Virutal Kinetic
Laboratory software and aims to be lightweight.

.. image:: https://raw.githubusercontent.com/VlachosGroup/vunits/master/docs/source/logos/vunits_web.png
   :target: https://vlachosgroup.github.io/vunits/
   :align: center

Documentation
-------------

See our `documentation page`_ for examples, equations used, and docstrings.

Developers
----------

-  Jonathan Lym (jlym@udel.edu)

Dependencies
------------

-  Python3
-  `Numpy`_: Used for vector and matrix operations
-  `Pandas`_: (Optional) Used by testing suite to read Excel spreadsheets
-  `xlrd`_: (Optional) Used by testing suite to read Excel spreadsheets

Getting Started
---------------

1. Install using pip (`see documentation for more thorough instructions`_)::

    pip install vunits


License
-------

This project is licensed under the MIT License - see the `LICENSE.md`_
file for details.

Contributing
------------

If you have a suggestion or find a bug, please post to our `Issues page`_ with 
the |enhancement_label| or |bug_label| tag respectively.

Finally, if you would like to add to the body of code, please:

- fork the development branch
- make the desired changes
- write the appropriate unit tests
- submit a `pull request`_.

Questions
---------

If you are having issues, please post to our `Issues page`_ with the 
|help_wanted_label| or |question_label| tag. We will do our best to assist.

Funding
-------

This material is based upon work supported by the Department of Energy's Office 
of Energy Efficient and Renewable Energy's Advanced Manufacturing Office under 
Award Number DE-EE0007888-9.5.

Special Thanks
--------------

-  Jaynell Keely (Logo design)


.. |bug_label| image:: https://raw.githubusercontent.com/VlachosGroup/vunits/master/docs/source/images/labels/bug_small.png
   :height: 20
   :target: https://github.com/VlachosGroup/vunits/issues?utf8=%E2%9C%93&q=label%3Abug

.. |enhancement_label| image:: https://raw.githubusercontent.com/VlachosGroup/vunits/master/docs/source/images/labels/enhancement_small.png
   :height: 20
   :target: https://github.com/VlachosGroup/vunits/issues?utf8=%E2%9C%93&q=label%3Aenhancement

.. |help_wanted_label| image:: https://raw.githubusercontent.com/VlachosGroup/vunits/master/docs/source/images/labels/help_wanted_small.png
   :height: 20
   :target: https://github.com/VlachosGroup/vunits/issues?utf8=%E2%9C%93&q=label%3A%22help%20wanted%22

.. |question_label| image:: https://raw.githubusercontent.com/VlachosGroup/vunits/master/docs/source/images/labels/question_small.png
   :height: 20
   :target: https://github.com/VlachosGroup/vunits/issues?utf8=%E2%9C%93&q=label%3Aquestion

.. _`documentation page`: https://vlachosgroup.github.io/vunits/
.. _Numpy: http://www.numpy.org/
.. _Pandas: https://pandas.pydata.org/
.. _xlrd: https://xlrd.readthedocs.io/en/latest/
.. _tests directory: https://github.com/VlachosGroup/vunits/tree/master/vunits/tests
.. _LICENSE.md: https://github.com/VlachosGroup/vunits/blob/master/LICENSE.md
.. _`see documentation for more thorough instructions`: https://vlachosgroup.github.io/vunits/install.html
.. _`Issues page`: https://github.com/VlachosGroup/vunits/issues
.. _`pull request`: https://github.com/VlachosGroup/vunits/pulls