"""A module that implements CSVFile class, a core class
   that handle cells and columns manipulation.
"""

# pylint: disable=no-self-use

import csv

class CSVFile:
    """A class built on top of csv module that allows cell search
    and columns management.

    Attributes:
        csvFile: a simple csv reader or can be an io.StringIO.
    """

    def __init__(self, csvFile):
        self.content = self.__format_content(csv.reader(csvFile))

    def __format_content(self, reader):
        result = [[cell.strip() for cell in row] for row in reader]
        return result

    def __get_header_index(self, header):
        headers = self.content[0]
        try:
            header_index = headers.index(header)
        except ValueError:
            return -1
        else:
            return header_index

    def __check_parameters(self, cell, header):
        if not cell or not header:
            raise ValueError('cell or header parameters are empty.')

    def __add_header(self, header):
        headers = self.content[0]
        headers.append(header)

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

        self.__check_parameters(cell, header)
        header_index = self.__get_header_index(header)

        if header_index == -1:
            raise ValueError('header: ' + header + ' not found in content: ' + str(self.content))
        for row in self.content[1:]:
            if cell in row:
                return row[header_index]
        raise ValueError('cell not found in content: ' + cell)

    def __edit_value(self, cell, value, header):
        header_index = self.__get_header_index(header)

        for row in self.content:
            if cell in row:
                row[header_index] = value

    def __append_value(self, cell, value):
        for row in self.content:
            if cell in row:
                row.append(value)

    def write(self, file_path):
        """Write self.content to file path.

        Args:
            file_path: a string corresponding to file to edit.
        """

        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.content)

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

        self.__check_parameters(cell, header)
        headers = self.content[0]
        if header in headers:
            self.__edit_value(cell, value, header)
        else:
            self.__add_header(header)
            self.__append_value(cell, value)
