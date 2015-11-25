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

from unittest import TestCase
import src.risk_calculation as r
import src.csvdata as data


class TestRiskCalculation(TestCase):

    def test_get_regressions(self):
        prices = data.get_historical_prices("../historical-prices", 0, 4)
        risk_calculation = r.RiskCalculation(prices, 'SP500')

        self.assertEquals(22 - 1, len(risk_calculation.risk_params))

    def test_get_weights(self):
        prices = data.get_historical_prices("../historical-prices", 0, 4)
        risk_calculation = r.RiskCalculation(prices, 'SP500')

        self.assertAlmostEqual(1, sum([val.weight for key, val in risk_calculation.risk_params.items()]))
