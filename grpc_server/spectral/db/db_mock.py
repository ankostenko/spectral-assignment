"""
    Mocks database queries
"""

import csv
import os
from typing import Tuple


def read_data_from_file() -> Tuple[list, list]:
    """
        Reads data from csv file and returns as two tuple of two lists
        :return: Tuple of lists with datetime and usage values
    """

    with open('spectral/data/meterusage.csv') as f:
        datetime = []
        values = []

        # Iterate over the csv file and fill datetime and values lists
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # Assuming datetime in the first position and values in the second
            datetime.append(row[0])
            values.append(row[1])

        return datetime, values


def get_usage_data(usage_stat_name: str) -> Tuple[list, list]:
    """
        Retrieves all available data by statistics name
        :param str usage_stat_name: Name of the statistics
        :return: tuple of lists of datetime and usage values
    """
    if usage_stat_name == 'meterusage':
        return read_data_from_file()
    else:
        return [], []
