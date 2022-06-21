"""
    Mocks database queries
"""

import csv
from typing import Tuple

# Default page size
DEFAULT_PAGE_SIZE = 20


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


def get_usage_data(usage_stat_name: str, 
                   page_number: int, page_size: int) -> Tuple[list, list]:
    """
        Retrieves all available data by statistics name
        :param str usage_stat_name: Name of the statistics
        :param int page_number: Number of page to access
        :param int page_size: Page size
        :return: tuple of lists of datetime and usage values
    """
    if usage_stat_name == 'meterusage':
        datetime, values = read_data_from_file()

        # Default value for page_size if nothing provided
        if page_size == 0:
            page_size = DEFAULT_PAGE_SIZE

        # Query with provided page number and size of a page
        start = page_number * page_size
        end = page_number * page_size + page_size

        # Flag to show that we have data to load
        data_length = len(datetime)
        more = True
        if page_number * page_size + page_size >= data_length:
            more = False

        return datetime[start:end], values[start:end], more
    else:
        return [], []
