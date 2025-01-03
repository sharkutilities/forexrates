# -*- encoding: utf-8 -*-

"""
A Python Package to Fetch FOREX Rates from API Sources

An one place that integrates different paid/open source API sources
to fetch foreign exchange rates.
"""

# ? package follows https://peps.python.org/pep-0440/
# ? https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
__version__ = "v0.0.1.dev0"

# init-time options registrations
from forexrates import io
from forexrates import api
