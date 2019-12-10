#
# setup.py
#
# Installation script to get setuptools to install pmutt into
# a Python environment.
#

import sys
import setuptools

# Import the lengthy rich-text README as the package's long
# description:
with open('README.rst', 'r') as fh:
	long_description = fh.read()

setuptools_info = {
	'name': 'VUnits',
	'version': '0.0.0',
	'author': 'Vlachos Research Group',
	'author_email': 'vlachos@udel.edu',
	'description': 'Virtual Kinetic Laboratory Units (VUnits)',
	'long_description': long_description,
	'zip_safe': True,
	'url': 'https://github.com/VlachosGroup/vunits',
	'packages': setuptools.find_packages(),
	'package_data': {'':['*.xlsx']},
	'install_requires': ['numpy>=1.15.1'],
	'classifiers': [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Chemistry",
	    ],
    }

if sys.version_info[0] >= 3:
	#
	# Augment for Python 3 setuptools:
	#
	setuptools_info['long_description_content_type'] = 'text/x-rst'

setuptools.setup(**setuptools_info)
