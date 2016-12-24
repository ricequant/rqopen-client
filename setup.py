#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from setuptools import (
    find_packages,
    setup,
)

from pip.req import parse_requirements


setup(
    name='rqopen-client',
    version='0.0.3',
    description='rqopen-client',
    packages=find_packages(exclude=[]),
    author='ricequant',
    author_email='public@ricequant.com',
    url="https://github.com/ricequant/rqopen-client",
    package_data={'': ['*.*']},
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
)
