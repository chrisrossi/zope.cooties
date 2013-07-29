##############################################################################
#
# Copyright (c) 2008-2013 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
import random
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
except IOError:
    README = ''

random.seed()
zope_packages = [p.strip() for p in
                 open(os.path.join(here, 'zope_packages.txt'))]
install_requires=[random.choice(zope_packages), random.choice(zope_packages)]

setup(name='zope.cooties',
      version='40.4',
      description=('Give the haters more to hate.'),
      long_description=README,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: Repoze Public License",
        ],
      keywords='zope cooties lol',
      author="Chris Rossi",
      author_email="chris@archimedeanco.com",
      url="http://pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      )

