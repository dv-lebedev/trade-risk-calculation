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

import os
from os import listdir
from dateutil import parser


def read(path, datetime_index, price_index):
    with open(path, 'r') as file:
        data = []
        for line in file:
            items = line.split(',')
            dt = parser.parse(items[datetime_index])
            price = float(items[price_index])
            data.append((dt, price))
    return data


def read_all_files(working_directory, datetime_index, price_index):
    historical_prices = {}
    for file in listdir(working_directory):
        if file.endswith(".txt") or file.endswith(".csv"):
            name = file.replace(".txt", "").replace(".csv", "").upper()
            file_path = os.path.join(working_directory, file)
            values = read(file_path, datetime_index, price_index)
            historical_prices[name] = [float(i[1]) for i in values]
    return historical_prices
