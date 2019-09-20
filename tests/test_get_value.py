# -*- coding: utf-8 -*-

"""Get value tests suite."""

from io import StringIO
import pytest
from .context import xsniper

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""
    in_memory_csv = StringIO("""\
header1,header2,
cell1,cell2,cell3
cell4,,cell6""")

    return xsniper.CSVFile(in_memory_csv)

def test_get_value(set_csv_file):
    """ Should return value from correct row and header """
    target = set_csv_file
    value = target.get_value("cell1", "header2")

    assert value == "cell2"

def test_get_empty_value(set_csv_file):
    """ Should return empty value as well """
    target = set_csv_file
    value = target.get_value("cell4", "header2")

    assert value == ""

def test_get_from_empty_cell(set_csv_file):
    """ Should return from empty cell as well """
    target = set_csv_file
    value = target.get_value("", "header1")

    assert value == "cell4"

def test_raise_if_empty_header(set_csv_file):
    """ Should raise an exception if header argument is an empty string """
    target = set_csv_file
    with pytest.raises(ValueError):
        target.get_value("cell1", "")

def test_raise_if_cell_arg_not_found(set_csv_file):
    """ Should raise an exception if cell argument is not found """

    target = set_csv_file
    with pytest.raises(ValueError):
        target.get_value("unknownCell", "header2")

def test_raise_if_header_arg_not_found(set_csv_file):
    """ Should raise an exception if header argument is not found """

    target = set_csv_file
    with pytest.raises(ValueError):
        target.get_value("cell1", "unknownHeader")
