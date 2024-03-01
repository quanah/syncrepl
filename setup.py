#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 et

# syncrepl_client installer code.
#
# Refer to the AUTHORS file for copyright statements.
#
# This file contains only factual information.
# Therefore, this file is likely not copyrightable.
# As such, this file is in the public domain.
# For locations where public domain does not exist, this file is licensed
# under the Creative Commons CC0 Public Domain Dedication, the text of which
# may be found in the file `LICENSE_others.md` that was included with this
# distribution, and also at
# https://github.com/akkornel/syncrepl/blob/master/LICENSE_others.md


import re
import setuptools
from setuptools import setup, find_packages
from sys import argv, version_info


# Thanks to https://hynek.me/articles/conditional-python-dependencies/
# for helping me understand the mess that is requirements specifications.

install_requirements = list()
extra_requirements = dict()

# Make sure we have 3.10+
# This is covered again later in the 'python_requires' option, but let's be
# safe.
if ((version_info[0] == 3) and
    (version_info[1] < 10)
):
    raise OSError('Python 3.10 or later is required.')

install_requirements.append('python-ldap')

# We need pyasn1.
# Well, actually python-ldap/pyldap require pyasn1, but it's an optional
# dependency for them, as it is only used with syncrepl.  So, we require it!
install_requirements.append('pyasn1>=0.2.2')

# Have code pull the version number from _version.py
def version():
    with open('syncrepl_client/_version.py', encoding='utf8') as file:
        regex = r"^__version__ = '(.+)'$"
        matches = re.search(regex, file.read(), re.M)
        if matches:
            return matches.group(1)
        else:
            raise LookupError('Unable to find version number')


# Have code pull the long description from our README
def readme():
    with open('README.rst', encoding='utf8') as file:
        return file.read()


# Let setuptools handle the rest
setup(
    name = 'syncrepl-client',
    version = version(),
    description = 'An easier-to-use LDAP syncrepl client',
    long_description = readme(),

    keywords = 'ldap syncrepl',

    author = 'A. Karl Kornel',
    author_email = 'karl@kornel.us',

    url = 'http://github.com/akkornel/syncrepl',

    packages = find_packages(),
    scripts = ['syncrepl-client'],
    zip_safe = True,
    include_package_data = True,

    python_requires = '>=3.10',
    install_requires = install_requirements,
    extras_require = extra_requirements,
    provides = ['syncrepl_client'],

    license = 'BSD 3-Clause',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP'
    ]
)
