# -*- encoding: utf-8 -*-

"""
Base Class Wrapper and Structure for IO Integration

The base class is designed to be uniform for all integrated external
data sources with abstract class methods and properties.
"""

import pandas as pd

from typing import Iterable
from abc import ABC, abstractmethod

class BaseIO(ABC):
    def __init__(self, data : dict | Iterable[dict]) -> None:
        self.data = self.__parse_data__(data)


    @staticmethod
    def __parse_data__(data : dict | Iterable[dict]) -> pd.DataFrame:
        assert isinstance(data, (dict, list)), \
            "Data must be a dictionary or a list of dictionaries."

        return [data] if isinstance(data, dict) else data


    @abstractmethod
    def dataframe(self, *args, **kwargs) -> pd.DataFrame:
        pass
