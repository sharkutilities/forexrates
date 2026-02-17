# -*- encoding: utf-8 -*-

"""
Operations to Parse Data as :mod:``pandas.DataFrame`` Object
"""

import datetime as dt

from typing import Iterable

import pandas as pd

from forexrates.io.base import BaseIO

class ExchangeRatesIO(BaseIO):
    """
    An IO Parser for the API Response from ExchangeRatesAPI

    The IO parser transforms the API response into a desired format
    by calling any internal methods or processes.

    A single response is received as a JSON (dictionary equivalent)
    from the API and is parsed in a desired format.A typical response
    structure is like:

    .. code-block:: json

        {
            "base" : "EUR",
            "date" : "2020-01-01",
            "rates" : {
                "USD" : 1.2345,
                "INR" : 1.2345,
                [...]
            }
        }

    In case of multiple response parsed under a single call, the
    function is adjusted with parameter to handle such a response. A
    sample response is like:

    .. code-block:: json

        [
            {
                "base" : "EUR",
                "date" : "2020-01-01",
                "rates" : {
                    "USD" : 1.2345,
                    "INR" : 1.2345,
                    [...]
                }
            },
            [...]
        ]

    :type  data: dict
    :param data: A single JSON response from the ExchangeRatesAPI.
        More information about the reponse is available here:
        https://exchangeratesapi.io/documentation/.
    """

    def __init__(self, data : dict | Iterable[dict]) -> None:
        super().__init__(data)


    def dataframe(self, verbose : bool = False, **kwargs) -> pd.DataFrame:
        """
        Parse a JSON (DICTIONARY) Response from ExchangeRatesAPI

        The function provide method to parse a single/multiple
        responses of the module and return a single
        :mod:``pandas.DataFrame`` object.

        :type  verbose: bool
        :param verbose: If set to ``True``, the function will print
            additional information about the parsed dataframe.

        Keyword Arguments
        -----------------
        Currently only setting the column and index names are supported
        using keyword arguments. More control is available in the future
        release and changes over dataframe.

            * **index** (*str*): Name of the index column for parsed
                dataframe. Defaults to ``foreign_exchange_rate``.
            * **column** (*str*): Name of the column for parsed dataframe.
                Defaults to ``target_currency_code``.
            * **basecolumn** (*str*): Name of the base currency column for
                parsed dataframe. Defaults to ``base_currency_code``.
            * **datecolumn** (*str*): Name of the date column for parsed
                dataframe. Defaults to ``effective_date``.


        :rtype:  :mod:``pandas.DataFrame``
        :return: A :mod:``pandas.DataFrame`` object with parsed data.
        """

        index = kwargs.get("index", "foreign_exchange_rate")
        column = kwargs.get("column", "target_currency_code")
        basecolumn = kwargs.get("basecolumn", "base_currency_code")
        datecolumn = kwargs.get("datecolumn", "effective_date")

        frames = []
        for data in self.data:
            base = data["base"]
            date = data["date"]

            # the data["date"] is a string in the format "%Y-%m-%d"
            # convert it to a datetime object and return parsed frame
            date = dt.datetime.strptime(date, "%Y-%m-%d")

            frame = pd.DataFrame(
                data["rates"], index = [index]
            ).T.reset_index().rename(columns = {"index" : column})

            frame[basecolumn] = base
            frame[datecolumn] = date

            frames.append(frame[[datecolumn, basecolumn, column, index]])

        frames = pd.concat(frames, ignore_index = True)

        if verbose:
            print(f"Total Parsed Records: {frames.shape[0]:,}")

            min_ = frames[datecolumn].min().date()
            max_ = frames[datecolumn].max().date()
            print(f"  >> Date Range: {min_} - {max_}")

            unique_bases_= frames[basecolumn].unique()
            n_unique_targets_ = frames[column].nunique()
            print(f"  >> Base Currency: {unique_bases_}")
            print(f"  >> # UQ Targets: {n_unique_targets_:,}")

        return frames
