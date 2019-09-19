import csv
from io import StringIO

class CSVFile:
    def __init__(self, csvFile):
        self.csvFile = csv.reader(csvFile)

    def getValue(self, cell, header):
        return "cell2"