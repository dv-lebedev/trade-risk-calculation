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

import scipy.stats as stats


class RiskParams:
    def __init__(self, b0=.0, b1=.0, r_value=.0, r_squared=.0,
                 weight=.0, trade_volume=.0, risk=.0, commission=.0):
        self.b0 = b0
        self.b1 = b1
        self.r_value = r_value
        self.r_squared = r_squared
        self.weight = weight
        self.trade_volume = trade_volume
        self.risk = risk
        self.commission = commission


class RiskCalculation:
    def __init__(self, historical_prices=None, index_symbol=str(), r_value_min_abs=.0):
        self.index_symbol = index_symbol
        self.historical_prices = historical_prices
        self.r_value_min_abs = r_value_min_abs
        self.risk_params = {}
        self.set_regressions()
        self.set_weights()

    def set_regressions(self):
        index_values = self.historical_prices[self.index_symbol]
        for item in self.historical_prices:
            if item != self.index_symbol:
                prices = self.historical_prices[item]
                beta, alpha, cor, det, std_err = stats.linregress(prices, index_values)
                if abs(cor) >= abs(self.r_value_min_abs):
                    self.risk_params[item] = RiskParams(
                        b0=alpha, b1=beta, r_value=cor, r_squared=det)

    def set_weights(self):
        summary = .0
        for item in self.risk_params:
            self.risk_params[item].weight = 1.0 / (1.0 + abs(self.risk_params[item].b1))
            summary += self.risk_params[item].weight
        for item in self.risk_params:
            self.risk_params[item].weight = self.risk_params[item].weight / summary
