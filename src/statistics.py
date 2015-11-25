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

import math


def get_standard_deviation(values):
    average = sum(values) / float(len(values))
    return math.sqrt(sum([(i - average) ** 2 for i in values]) / float(len(values)))


def pow_values(values):
    return sum([pow(i, 2) for i in values])


def multiply_values(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])


def get_regression(x, y):
    x_average = sum(x) / float(len(x))
    y_average = sum(y) / float(len(y))

    s2x = (pow_values(x) / len(x)) - pow(x_average, 2)
    cov_xy = multiply_values(x, y) / len(x) - x_average * y_average

    beta = cov_xy / s2x
    alpha = y_average - beta * x_average

    cor = beta * (get_standard_deviation(x) / get_standard_deviation(y))
    det = pow(cor, 2)

    return alpha, beta, cor, det
    