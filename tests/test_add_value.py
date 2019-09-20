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
    return xsniper.CSVFile(in_memory_csv)

def test_add_value(set_csv_file):
    """Should add value to content from a cell from the same row and a existing"""
    got = set_csv_file
    want = "cell3"
    got.add_value("cell1", "header3", want)

    assert got.get_value("cell1", "header3") == want
