#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from setuptools import (
    find_packages,
    setup,
)

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

setup(
    name='rqopen-client',
    version='0.0.5',
    description='rqopen-client',
    packages=find_packages(exclude=[]),
    author='ricequant',
    author_email='public@ricequant.com',
    url="https://github.com/ricequant/rqopen-client",
    package_data={'': ['*.*']},
    install_requires=[
        str(ir.req)
        for ir in parse_requirements("requirements.txt", session=False)
    ],
    zip_safe=False,
)
