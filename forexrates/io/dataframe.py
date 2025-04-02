# -*- encoding: utf-8 -*-

"""
Operations to Parse Data as :mod:``pandas.DataFrame`` Object
"""

import datetime as dt

import pandas as pd

def exchangeratesio(data : dict, mode : str = "multiple", **kwargs) -> pd.DataFrame:
    """
    Parse a JSON (DICTIONARY) Response from ExchangeRatesAPI

    The single response is received as a JSON (dictionary equivalent)
    from the API and is parsed as a :mod:``pandas.DataFrame`` object.
    The function provide method to parse a single/multiple responses
    of the module and return a single :mod:``pandas.DataFrame`` object.
    A typical response structure is like:

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

    :type  mode: str
    :param mode: Mode of operation (self explanatory). Either
        ``multiple`` or ``single``. The default value is ``multiple``.


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

    base = data["base"]
    date = data["date"]

    # the data["date"] is a string in the format "%Y-%m-%d"
    # convert it to a datetime object and return parsed dataframe
    date = dt.datetime.strptime(date, "%Y-%m-%d")

    # ! override default column and index names with kwargs
    index = kwargs.get("index", "foreign_exchange_rate")
    column = kwargs.get("column", "target_currency_code")
    basecolumn = kwargs.get("basecolumn", "base_currency_code")
    datecolumn = kwargs.get("datecolumn", "effective_date")


    frame = pd.DataFrame(
        data["rates"], index = [index]
    ).T.reset_index().rename(columns = {"index" : column})

    frame[basecolumn] = base
    frame[datecolumn] = date

    return frame[[datecolumn, basecolumn, column, index]]
