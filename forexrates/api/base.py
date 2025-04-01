# -*- encoding: utf-8 -*-

"""
Base API Class Wrapper and Structure for API Integration

The base class is designed to be uniform for all integrated external
data sources with abstract class methods and properties.
"""

import time
import requests

from typing import Iterable
from abc import ABC, abstractmethod

class BaseAPI(ABC):
    def __init__(self, apikey : str) -> None:
        self.apikey = apikey

        # create request sessions object for further use
        self._session = requests.Session()


    @property
    @abstractmethod
    def uri(self) -> str:
        pass


    @property
    @abstractmethod
    def headers(self) -> dict:
        pass


    @property
    @abstractmethod
    def endpoint(self) -> str:
        pass


    @property
    @abstractmethod
    def params(self) -> dict:
        pass


    def __format_error__(self, e : requests.exceptions.RequestException) -> str:
        """
        Format the Base Error Response Structure to Hide Sensitive Data

        The make request exposes some sensitive information in the URL
        string, which is not desired for security reasons. Referring
        to an existing issue, the problem is not yet resolved and may
        require an alternate approach.

        Override the method in the child class to preserve the sensitive
        information from leaking, or leave it to the parent class to
        return the value as is.

        :type  e: requests.exceptions.RequestException
        :param e: Exception to be formatted, to hide sensitive
            information from the URL string.
        """

        return e


    def make_request(self, method : str, **kwargs) -> requests.Response:
        sleep = kwargs.get("sleep", 2) # sleep b/w requests, in seconds
        retries = kwargs.get("retries", 3) # no. of retry attempts

        # create uri and append the endpoint to the url::
        uri = self.uri + self.endpoint

        # create url load like headers and params
        dataload = {"headers" : self.headers, "params" : self.params}

        # retry on the uri with header and param loads
        for attempt in range(retries):
            try:
                response = self._session.request(method, uri, **dataload)
                response.raise_for_status()

                return response # data received, return response

            except requests.exceptions.RequestException as e:
                e = self.__format_error__(e)
                print(f"Request Failed (Attempt: {attempt + 1}) : {e}")

                if attempt == retries - 1:
                    print("Max Retries Reached.")
                    raise e

                time.sleep(sleep)
                continue # continue until retries are exhausted

            except requests.exceptions.Timeout as e:
                print(f"Request Timed Out (Attempt: {attempt + 1}) : {e}")

                if attempt == retries - 1:
                    print("Max Retries Reached.")
                    raise e

                time.sleep(sleep)
                continue # continue until retries are exhausted


    def get(self, **kwargs) -> Iterable:
        """
        Get the Base Response from an External API Source

        The base response is fetched and the data is returned as
        a JSON/Dictionary object to the enduser. The response can be
        further processed and formatted into a desired structure using
        the IO module.
        """

        return self.make_request("GET", **kwargs).json()


    def close(self) -> None:
        self._session.close()
