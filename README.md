# TRACE FRED Example

This example is intended for use with https://github.com/transparency-certified/trs-example/ to demonstrate implementation of a TRACE System using the [tro-utils](https://github.com/transparency-certified/tro-utils/) toolkit.

This simple example is intended to demonstrate the following scenario:

> A researcher is preparing to submit a manuscript to a journal with strict transparency and reproducibility requirements. Their manuscript includes a plot of the S&P500 obtained using the Federal Reserve Economic Data (FRED) API. The FRED API terms of use prevent the author from sharing their private API key. The data underlying their plot is protected by copyright and S&P Down Jones, LLC, prohibits redistribution without permission.

To run this example:
* [Obtain a FRED API key](https://fred.stlouisfed.org/docs/api/api_key.html) and save to a file named `fred_apikey.txt`.
* `pip install -r requirements.txt` (virtual environment recommended)
* Execute the `run.sh` script
