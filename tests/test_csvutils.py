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
import logic.csvutils as csv


class TestCsvData(TestCase):
    def test_read(self):
        csv_data = csv.read("../historical-prices/JPM.txt", 0, 4)
        self.assertEquals(473, len(csv_data))
        first_price = csv_data[0][1]
        last_price = csv_data[472][1]
        self.assertEquals(58.209999, first_price)
        self.assertEquals(66.510002, last_price)

    def test_get_historical_prices(self):
        historical_prices = csv.read_all_files("../historical-prices", 0, 4)
        self.assertEquals(22, len(historical_prices))
        for key, value in historical_prices.items():
            self.assertEquals(473, len(value))
