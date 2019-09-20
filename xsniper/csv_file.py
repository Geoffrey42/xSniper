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

    def __get_header_index(self, header):
        if header == "":
            raise ValueError

    def get_value(self, cell, header):
        """Get a value (a cell) from its header and
        any other cell in the same row.

        Args:
            cell: Any cell in targeted value's same row. Must not be empty.
            header: Targeted value's header. Must not be empty.

        Returns:
            A string corresponding to the targeted value.

        Raises:
            ValueError: if cell is incorrect or header an empty
            string.
        """
        if cell == "":
            raise ValueError
        try:
            header_index = self.__get_header_index(header)
        except ValueError as error:
            raise error

            if cell in row:
                return row[header_index]
        raise ValueError

    def add_value(self, cell, header, value):
        """Add a value (a cell) based on another cell in the same row
        and value's header.

        Args:
            cell: Any cell in targeted value's same row.
            header: Targeted value's header.

        Raises:
            ValueError: if cell is incorrect or header an empty
            string.
        """
