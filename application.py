"""
Copyright 2015-2016 Denis Lebedev

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

import pandas as pd
import logic.risk_calculation as risk_calc
from logic import csvutils as csv


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
        return index_symbol
    else:
        print("Index '{}' not found.".format(index_symbol))
        return get_index_code(historical_prices)


def main():
    working_directory = "historical-prices"
    date_time_index = 0
    prices_index = 4

    balance = get_param("Balance $")
    risk = get_param("Risk %")
    commission = get_param("Commission %")

    prices = csv.read_all_files(working_directory, date_time_index, prices_index)
    index_symbol = get_index_code(prices)

    rc = risk_calc.RiskCalculation(prices, index_symbol, r_value_min_abs=0.6)
    print()

    symbols = rc.risk_params.keys()

    risk_params = rc.risk_params.values()

    data = {
        'b1': [i.b1 for i in risk_params],
        'r_value': [i.r_value for i in risk_params],
        'weight': [i.weight for i in risk_params],
        'trade_volume': [balance * i.weight for i in risk_params],
        'risk_limit': [balance * i.weight * risk / 100.0 for i in risk_params],
        'commission': [balance * i.weight * commission / 100.0 for i in risk_params]
    }

    df = pd.DataFrame(data, index=symbols)

    cols = ['b1', 'r_value', 'weight', 'trade_volume', 'risk_limit', 'commission']

    df = df[cols]

    print(df)

    print()

    input("\npush 'ENTER' to exit.")


if __name__ == '__main__':
    main()
