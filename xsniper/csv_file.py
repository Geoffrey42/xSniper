"""A module that implements CSVFile class, a core class
   that handle cells and columns manipulation.
"""

# pylint: disable=no-self-use

import csv
from itertools import islice
import pandas as pd

class CSVFile:
    """A class built on top of csv module that allows cell search
    and columns management.

    Attributes:
        csvFile: a simple csv reader or can be an io.StringIO.
    """

    def __init__(self, csvFile, common_key=None):
        self.common_key = common_key
        if common_key is not None:
            self.content = self.__format_content(csv.reader(csvFile))
        else:
            self.df_content = pd.read_csv(csvFile)

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

    def __check_parameters(self, header):
        if not self.common_key or not header:
            raise ValueError('cell or header parameters are empty.')

    def __add_header(self, header):
        headers = self.content[0]
        headers.append(header)

    def __edit_value(self, value, header):
        header_index = self.__get_header_index(header)

        for row in self.content:
            if self.common_key in row:
                row[header_index] = value

    def __append_value(self, value):
        for row in self.content:
            if self.common_key in row:
                row.append(value)

    def get_value(self, header):
        """Get a value (a cell) from its header and
        any other cell in the same row.

        Args:
            header: Targeted value's header. Must not be empty.

        Returns:
            A string corresponding to the targeted value.

        Raises:
            ValueError: if a header an empty
            string.
        """

        self.__check_parameters(header)
        header_index = self.__get_header_index(header)

        if header_index == -1:
            raise ValueError('header: ' + header + ' not found in content: ' + str(self.content))
        for row in self.content[1:]:
            if self.common_key in row:
                return row[header_index]
        raise ValueError('cell not found in content: ' + self.common_key)

    def write(self, file_path):
        """Write self.content to file path.

        Args:
            file_path: a string corresponding to file to edit.
        """

        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.content)

    def add_value(self, header, value):
        """Add a value (a cell) based on another cell in the same row
        and value's header.

        Args:
            header: Targeted value's header.

        Raises:
            ValueError: if header is an empty
            string.
        """

        self.__check_parameters(header)
        headers = self.content[0]
        if header in headers:
            self.__edit_value(value, header)
        else:
            self.__add_header(header)
            self.__append_value(value)

    def get_single_column(self, header):
        """Get a single column.

        Args:
            header: Desired headers.

        Returns:
            The desired columns in pandas dataframe format.

        Raises:
            ValueError: if header not found.
        """

        try:
            result = self.df_content[header]
        except KeyError:
            raise ValueError("Header not found: " + header)
        return result

    def get_columns(self, *args):
        """Get wholes columns.

        Args:
            header: Desired headers.

        Returns:
            The desired columns in pandas dataframe format.

        Raises:
            ValueError: if header not found.
        """

        result = self.get_single_column(args[0])
        for arg in islice(args, 1, None, 1):
            column = self.get_single_column(arg)
            result = pd.concat([result, column], ignore_index=False, axis=1)
        return result

    def add_columns(self, columns):
        """Add columns to self.df_content.

        Args:
            columns: pandas dataframe columns to add.
        """

        self.df_content = pd.concat([self.df_content, columns], ignore_index=False, axis=1)
