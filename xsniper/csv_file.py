"""A module that implements CSVFile class, a core class
   that handle cells and columns manipulation.
"""

import csv

class CSVFile:
    """A class built on top of csv module that allows cell search
    and columns management.

    Attributes:
        csvFile: a simple csv reader or can be an io.StringIO.
    """
    def __init__(self, csvFile):
        self.csv_file = csv.reader(csvFile)

    def __get_header_index(self, header):
        if header == "":
            raise ValueError
        headers = iter(self.csv_file).__next__()
        for index, element in enumerate(headers):
            print(element)
            if header == element:
                return index
        raise ValueError

    def get_value(self, cell, header):
        """Get a value (a cell) from its header and
        any other cell in the same row.

        Args:
            cell: Any cell in targeted value's same row.
            header: Targeted value's header.

        Returns:
            A string corresponding to the targeted value.

        Raises:
            ValueError: if cell is incorrect or header an empty
            string.
        """
        try:
            header_index = self.__get_header_index(header)
        except ValueError as error:
            raise error

        for row in self.csv_file:
            if cell in row:
                return row[header_index]
        raise ValueError
