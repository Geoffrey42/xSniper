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
        self.content = list(csv.reader(csvFile))

    def __get_header_index(self, header):
        if header == "":
            raise ValueError
        headers = self.content[0]
        return headers.index(header)

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

        for row in self.content[1:]:
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

        header_index = self.__get_header_index(header)
        for row in self.content:
            if cell in row:
                row[header_index] = value
