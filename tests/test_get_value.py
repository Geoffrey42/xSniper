# -*- coding: utf-8 -*-

"""Get value tests suite."""

from io import StringIO
import pytest
from .context import xsniper

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,
cell4,cell5,cell6
cell7,,cell9""")
    return in_memory_csv

def test_get_value(set_csv_file):
    """ Should return value from correct row and header """

    target = xsniper.CSVFile(set_csv_file, "cell1")
    value = target.get_value("header2")

    assert value == "cell2"

def test_get_empty_value(set_csv_file):
    """ Should return empty value as well """

    target = xsniper.CSVFile(set_csv_file, "cell7")
    value = target.get_value("header2")

    assert value == ""

def test_raise_if_empty_cell(set_csv_file):
    """ Should return from empty cell as well """

    target = xsniper.CSVFile(set_csv_file, "")
    with pytest.raises(ValueError):
        target.get_value("header1")

def test_raise_if_empty_header(set_csv_file):
    """ Should raise an exception if header argument is an empty string """

    target = xsniper.CSVFile(set_csv_file, "cell1")
    with pytest.raises(ValueError):
        target.get_value("")

def test_raise_if_cell_arg_not_found(set_csv_file):
    """ Should raise an exception if cell argument is not found """

    target = xsniper.CSVFile(set_csv_file, "unknownCell")
    with pytest.raises(ValueError):
        target.get_value("header2")

def test_raise_if_header_arg_not_found(set_csv_file):
    """ Should raise an exception if header argument is not found """

    target = xsniper.CSVFile(set_csv_file, "cell1")
    with pytest.raises(ValueError):
        target.get_value("unknownHeader")
