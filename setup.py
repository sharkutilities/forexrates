#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

# import the package directly for config settings
import forexrates

setup(
    name = "forexrates",
    version = forexrates.__version__,
    author = "shark-utilities developers",
    author_email = "neuralNOD@outlook.com",
    description = "A unified codebase for fetching FOREX Rates.",
    long_description = open("README.md", "r").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/sharkutilities/forexrates",
    packages = find_packages(
        exclude = [
            "tests", "tests.*", "examples", "examples.*"
        ]
    ),
    install_requires = [
        "tqdm>=4.64.1",
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "requests>=2.31.0",
        "psycopg2-binary>=2.9.0",
        "SQLAlchemy>=1.4.0,<2.0.0",
    ],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License"
    ],
    project_urls = {
        "Issue Tracker" : "https://github.com/sharkutilities/forexrates/issues",
        # "Code Documentations" : "https://.readthedocs.io/en/latest/index.html",
        "Org. Homepage" : "https://github.com/sharkutilities"
    },
    keywords = [
        # keywords for finding the package::
        "forex", "forex-rates", "currency", "currency-conversion",
        "api", "exchange-rate", "forex-api", "currency-api",
        # keywords for finding the package relevant to usecases::
        "data science", "data analysis", "data scientist", "data analyst"
    ],
    python_requires = ">=3.9"
)
