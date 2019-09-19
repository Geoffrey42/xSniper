# -*- coding: utf-8 -*-

from .context import xSniper

import pytest
from io import StringIO


class TestSuiteGetValue:
    """Get value test cases."""

    def test_get_value(self):
        """ Should return value from correct row and header """
        inMemoryCSV = StringIO("""\
            header1,header2,header3
            cell1,cell2,cell3
            cell4,cell5,cell6""")
        target = xSniper.CSVFile(inMemoryCSV)
        value = target.getValue("cell1", "header2")

        assert value == "cell2"