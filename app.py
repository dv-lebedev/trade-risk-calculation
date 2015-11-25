"""
Copyright 2015 Denis Lebedev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from src import risk_calculation as rc
from src import csvdata as d
import pandas as pd


def get_param(name):
    try:
        value = float(input("{} : ".format(name)))
        if value > 0:
            return value
        else:
            print("{} should be more than zero.".format(name))
            return get_param(name)
    except ValueError:
        print("Incorrect input. Please, try again.")
        return get_param(name)


def get_index_code(historical_prices):
    index_symbol = input("Index symbol : ").upper()
    if index_symbol in historical_prices.keys():
        print("Selected index symbol : {}".format(index_symbol))
        return index_symbol
    else:
        print("Index '{}' not found.".format(index_symbol))
        return get_index_code()


def main():
    working_directory = "historical-prices"
    date_time_index = 0
    prices_index = 4

    balance = get_param("Balance $")
    risk = get_param("Risk %")
    commission = get_param("Commission %")

    prices = d.get_historical_prices(working_directory, date_time_index, prices_index)
    index_symbol = get_index_code(prices)

    risk_calculation = rc.RiskCalculation(prices, index_symbol)

    print()

    symbols = risk_calculation.risk_params.keys()

    data = {
        'b1': [i.b1 for i in risk_calculation.risk_params.values()],
        'r_value': [i.r_value for i in risk_calculation.risk_params.values()],
        'weight': [i.weight for i in risk_calculation.risk_params.values()],
        'balance': [balance * i.weight for i in risk_calculation.risk_params.values()],
        'risk_limit': [balance * i.weight * risk / 100.0 for i in risk_calculation.risk_params.values()],
        'commission': [balance * i.weight * commission / 100.0 for i in risk_calculation.risk_params.values()]
    }

    df = pd.DataFrame(data, index=symbols)

    cols = ['b1', 'r_value', 'weight', 'balance', 'risk_limit', 'commission']

    df = df[cols]

    print(df)

    print()

    input("\npush 'ENTER' to exit.")


if __name__ == '__main__':
    main()
