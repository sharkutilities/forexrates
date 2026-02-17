#!/usr/bin/env python
#
# Copywright (C) 2024 Debmalya Pramanik <neuralNOD@gmail.com>
# LICENSE: MIT License

import os
import sys

from setuptools import setup
from setuptools import find_packages

sys.path.append(
    os.path.join(os.path.dirname(__file__))
)

import forexrates

setup(
    name = "forexrates",
    version = forexrates.__version__,
    author = "shark-utilities developers",
    author_email = "neuralNOD@outlook.com",
    description = "A unified codebase for fetching FOREX rates.",
    # long_description = open("README.md", "r").read(),
    # long_description_content_type = "text/markdown",
    url = "https://github.com/sharkutilities/forexrates",
    packages = find_packages(
        exclude = ["tests*", "examples*"]
    ),
    install_requires = [
        "greenlet==3.3.1",
        "numpy==2.4.2",
        "pandas==3.0.0",
        "psycopg2==2.9.11",
        "python-dateutil==2.9.0.post0",
        "six==1.17.0",
        "SQLAlchemy==2.0.46",
        "tqdm==4.67.3",
        "typing_extensions==4.15.0",
        "tzdata==2025.3",
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
        "forex", "api", "exchange rates", "foreign exchange rates",
        # keywords for finding the package relevant to usecases::
        "wrappers", "data science", "data analysis", "data scientist", "data analyst"
    ],
    python_requires = ">=3.10"
)
