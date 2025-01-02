# -*- encoding: utf-8 -*-

"""
Base API Class Wrapper and Structure for API Integration

The base class is designed to be uniform for all integrated external
data sources with abstract class methods and properties.
"""

import time
import requests

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


    def get(self, **kwargs) -> requests.Response:
        return self.make_request("GET", **kwargs)


    def close(self) -> None:
        self._session.close()
