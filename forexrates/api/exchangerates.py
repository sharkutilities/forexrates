# -*- encoding: utf-8 -*-

"""
API Handling for the Exchangerates API (https://exchangeratesapi.io/)

Exchange Rates API provides historic and real-time exchange rates and
currency conversions. More information about the API is available at
https://exchangeratesapi.io/documentation/.
"""

import datetime as dt
from typing import Iterable
from forexrates.api.base import BaseAPI

class ExchangeRatesAPI(BaseAPI):
    def __init__(self, apikey : str, **kwargs) -> None:
        super().__init__(apikey)

        # ! override default endpoint with endpoint
        # ? the endpoint can be date (%Y-%m-%d) for historic rates
        self._endpoint = kwargs.get("endpoint", "latest")

        # ? each base class accepts parameters as keyword arguments
        self._base = kwargs.get("base", "EUR")


    @property
    def uri(self) -> str:
        return "https://api.exchangeratesapi.io/v1/"
    

    @property
    def endpoint(self) -> str:
        # ? endpoint can be date (%Y-%m-%d) for historic rates
        retval = self._endpoint

        # if date object, then parse as string
        if isinstance(retval, dt.date):
            retval = retval.strftime("%Y-%m-%d")

        return retval
    

    @property
    def params(self) -> dict:
        return {
            "base" : self._base,
            "access_key" : self.apikey
        }
    

    @property
    def headers(self) -> None:
        pass


    def get(self, parsewith : callable = None, **kwargs) -> Iterable:
        return super().get(parsewith = parsewith, **kwargs)
