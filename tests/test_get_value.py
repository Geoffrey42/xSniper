# -*- coding: utf-8 -*-

from .context import xSniper

import pytest
from io import StringIO


@pytest.fixture
def setCSVFile():
    inMemoryCSV = StringIO("""\
header1,header2,
cell1,cell2,cell3
cell4,,cell6""")

    return xSniper.CSVFile(inMemoryCSV)

def test_get_value(setCSVFile):
    """ Should return value from correct row and header """
    target = setCSVFile
    value = target.getValue("cell1", "header2")

    assert value == "cell2"

def test_get_empty_value(setCSVFile):
    """ Should return empty value as well """
    target = setCSVFile
    value = target.getValue("cell4", "header2")

    assert value == ""

def test_get_from_empty_cell(setCSVFile):
    """ Should return from empty cell as well """
    target = setCSVFile
    value = target.getValue("", "header1")

    assert value == "cell4"

def test_raise_if_empty_header(setCSVFile):
    """ Should raise an exception if header argument is an empty string """
    target = setCSVFile
    with pytest.raises(ValueError):
        target.getValue("cell1", "")

def test_raise_if_cell_arg_not_found(setCSVFile):
    """ Should raise an exception if cell argument is not found """

    target = setCSVFile
    with pytest.raises(ValueError):
        target.getValue("unknownCell", "header2")

def test_raise_if_header_arg_not_found(setCSVFile):
    """ Should raise an exception if header argument is not found """

    target = setCSVFile
    with pytest.raises(ValueError):
        target.getValue("cell1", "unknownHeader")