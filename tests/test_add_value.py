# -*- coding: utf-8 -*-

"""Add value tests suite."""

from io import StringIO
import pytest
from .context import xsniper

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,
cell4,cell5,cell6""")
    return in_memory_csv

def test_add_value_when_its_header_exists(set_csv_file):
    """Should add value to content from a cell from the same row and a existing"""

    got = xsniper.CSVFile(set_csv_file, "cell1")
    want = "cell3"
    got.add_value("header3", want)

    assert got.get_value("header3") == want

def test_add_value_when_its_header_does_not_exist(set_csv_file):
    """Should add value to content even if it's header does not exist yet"""

    got = xsniper.CSVFile(set_csv_file, "cell1")
    want = "cell3"
    got.add_value("header4", want)

    assert got.get_value("header4") == want

def test_raise_exception_when_cell_is_empty(set_csv_file):
    """Should raise ValueError if cell argument is empty"""

    got = xsniper.CSVFile(set_csv_file, "")
    with pytest.raises(ValueError):
        got.add_value("header3", "value")

def test_raise_exception_when_header_is_empty(set_csv_file):
    """Should raise ValueError if header argument is empty"""

    got = xsniper.CSVFile(set_csv_file, "cell4")
    with pytest.raises(ValueError):
        got.add_value("", "value")

def test_add_empty_value_when_header_exists(set_csv_file):
    """Should add empty value when its header exists"""

    got = xsniper.CSVFile(set_csv_file, "cell1")
    want = ""
    got.add_value("header3", want)

    assert got.get_value("header3") == want

def test_add_empty_value_when_header_does_not_exists(set_csv_file):
    """Should add empty value when its header doesn't exists"""

    got = xsniper.CSVFile(set_csv_file, "cell1")

    want = ""
    got.add_value("header4", want)

    assert got.get_value("header4") == want