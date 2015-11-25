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
import src.csvdata as d


class TestCsvData(TestCase):

    def test_get_historical_prices(self):
        historical_prices = d.get_historical_prices("../historical-prices", 0, 4)

        self.assertEquals(22, len(historical_prices))

        for key, value in historical_prices.items():
            self.assertEquals(473, len(value))