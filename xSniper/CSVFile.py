import csv
from io import StringIO

class CSVFile:
    """A class built on top of csv module that allows cell search
    and columns management.

    Attributes:
        csvFile: a simple csv reader or can be an io.StringIO.
    """
    def __init__(self, csvFile):
        self.csvFile = csv.reader(csvFile)

    def __getHeaderIndex(self, header):
        if header == "":
            raise ValueError
        headers = iter(self.csvFile).__next__()
        for index, element in enumerate(headers):
            print(element)
            if header == element:
                return index
        raise ValueError

    def getValue(self, cell, header):
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
            headerIndex = self.__getHeaderIndex(header)
        except ValueError as e:
            raise e

        for row in self.csvFile:
            if cell in row:
                return row[headerIndex]
        raise ValueError