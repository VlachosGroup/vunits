.. _install:

Installation
************

Installing Python
-----------------
Anaconda is the recommended method to install Python for scientific
applications. It is supported on Linux, Windows and Mac OS X.
`Download Anaconda here`_. Note that VUnits runs on Python 3.X.

Installing VUnits using pip
---------------------------
Using pip is the most straightforward way to install VUnits.

1. Open a command prompt with access to Python (if Python is installed via
   Anaconda on Windows, open the Anaconda Prompt from the start menu).

2. Install VUnits by typing the following in the command prompt:
::

    pip install vunits

The output towards the end should state "Successfully built VUnits" if the
installation was successful.

Installing VUnits from source
-----------------------------
If you would prefer to install from source or you are interested in development,
follow the instructions below.
::

    pip install git+https://github.com/VlachosGroup/VUnits.git

Installing the developer branch
-------------------------------
Changes that will be in the next release will be located in the Developer branch
but may have more bugs than the master branch. You can install using the
following:
::


    pip install --upgrade git+https://github.com/VlachosGroup/VUnits.git@development

Upgrading VUnits using pip
--------------------------
To upgrade to a newer release, use the --upgrade flag:
::

    pip install --upgrade vunits

Running unit tests
------------------
VUnits has a suite of unit tests that should be run before committing any code.
To run the tests, navigate to the tests folder (vunits/tests) via a command line
with access to Python.

Run the following command:
::

     python -m unittest

The expected output is shown below. The number of tests will not
necessarily be the same. ::

    .........................
    ----------------------------------------------------------------------
    Ran 25 tests in 0.020s

    OK

.. _`Download Anaconda here`: https://www.anaconda.com/distribution/#download-section
.. _`See GitHub instructions on cloning repositories here`: https://help.github.com/en/articles/cloning-a-repository
