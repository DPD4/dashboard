# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in financial_dashboard_final/__init__.py
from financial_dashboard_final import __version__ as version

setup(
    name="financial_dashboard_final",
    version=version,
    description="Arabic Financial Dashboard for ERPNext",
    author="Your Company",
    author_email="admin@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)