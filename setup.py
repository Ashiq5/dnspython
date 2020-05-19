#!/usr/bin/env python3
#
# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license
#
# Copyright (C) 2003-2007, 2009-2011 Nominum, Inc.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice
# appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NOMINUM DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NOMINUM BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys
from setuptools import setup

version = '2.0.0'

try:
    sys.argv.remove("--cython-compile")
except ValueError:
    compile_cython = False
else:
    compile_cython = True
    from Cython.Build import cythonize
    ext_modules = cythonize(['dns/*.py', 'dns/rdtypes/*.py', 'dns/rdtypes/*/*.py'])

kwargs = {
    'name' : 'dnspython',
    'version' : version,
    'description' : 'DNS toolkit',
    'long_description' : \
    """dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.""",
    'author' : 'Bob Halley',
    'author_email' : 'halley@dnspython.org',
    'license' : 'ISC',
    'url' : 'http://www.dnspython.org',
    'packages' : ['dns', 'dns.rdtypes', 'dns.rdtypes.IN', 'dns.rdtypes.ANY', 'dns.rdtypes.CH'],
    'package_data' : {'dns': ['py.typed']},
    'download_url' : \
    'http://www.dnspython.org/kits/{}/dnspython-{}.tar.gz'.format(version, version),
    'classifiers' : [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: Freeware",
        "Operating System :: Microsoft :: Windows :: Windows 95/98/2000",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        ],
    'python_requires': '>=3.6',
    'test_suite': 'tests',
    'provides': ['dns'],
    'extras_require': {
        'DOH': ['requests', 'requests-toolbelt'],
        'IDNA': ['idna>=2.1'],
        'DNSSEC': ['cryptography>=2.6'],
        'trio': ['trio>=0.14.0'],
        },
    'ext_modules': ext_modules if compile_cython else None,
    'zip_safe': False if compile_cython else None,
    }

setup(**kwargs)
