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
import logic.statistics as stat


class TestStatistics(TestCase):

    def test_standard_deviation(self):

        values = [1, 3, 5, 7, 9, 11, 15, 17]
        result = stat.get_standard_deviation(values)
        self.assertAlmostEqual(5.2678, result, places=4)

        values = [-3, -5, -8, -13, -35, -57]
        result = stat.get_standard_deviation(values)
        self.assertAlmostEqual(19.5824, result, places=4)

    def test_pow_values(self):

        values = [12, 65, 83, 55, 100, 248, 201, 0, 0, -3, -255]
        result = stat.pow_values(values)
        self.assertEqual(191222, result)

    def test_multiple_values(self):

        x = [1, 3, 5, 7, 9, 11, 15, 17, 19, 35]
        y = [-1001, 2, 6, 98, 23, -56, -34, 56, -345, 7]
        result = stat.multiply_values(x, y)
        self.assertEquals(-6556, result)

    def test_regression(self):

        x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]

        alpha, beta, cor, det = stat.get_regression(x, y)

        self.assertEquals(1, cor)
        self.assertEquals(1, det)
        self.assertEquals(59, alpha)
        self.assertEquals(1, beta)