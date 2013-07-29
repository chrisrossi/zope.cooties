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
import re
import urllib2
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
except IOError:
    README = ''

pkgre = re.compile('href="/pypi/([^/"]+)/')
prefixes = [
    'zope.',
    'zc.',
    'z3c.',
# Uncomment following line to unleash Plone pain.
#    'Products.'
]

def matches(name):
    for prefix in prefixes:
        if name.startswith(prefix):
            return True
    return False

def get_zope_packages():
    html = urllib2.urlopen('https://pypi.python.org/pypi/').read()
    return [pkg.strip() for pkg in pkgre.findall(html) if matches(pkg)]

random.seed()
zope_packages = get_zope_packages()
install_requires=[random.choice(zope_packages), random.choice(zope_packages)]

setup(name='zope.cooties',
      version='40.5',
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
