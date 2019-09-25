# -*- coding: utf-8 -*-

"""Get columns tests suite."""

import pandas as pd
from io import StringIO
import pytest
from .context import xsniper

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,cell3
cell4,cell5,cell6""")
    return in_memory_csv

def test_get_one_column(set_csv_file):
    """Should return the desired column."""

    got = xsniper.CSVFile(set_csv_file)

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,cell3
cell4,cell5,cell6""")

    df = pd.read_csv(in_memory_csv, index_col=None, header=0)
    want = df['header2']

    assert got.get_single_column('header2').equals(want)

def test_get_several_columns(set_csv_file):
    """Should returns selected columns."""

    test_src = xsniper.CSVFile(set_csv_file)

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,cell3
cell4,cell5,cell6""")

    df = pd.read_csv(in_memory_csv, index_col=None, header=0)
    h2 = df['header2']
    h3 = df['header3']

    want = pd.concat([h2, h3], ignore_index=False, axis=1)
    got = test_src.get_columns('header2', 'header3')
    assert got.equals(want)

def test_get_column_raise_exception_if_not_found(set_csv_file):
    """Should raise ValueError if the header not found."""

    got = xsniper.CSVFile(set_csv_file)
    with pytest.raises(ValueError):
        got.get_single_column('unknown_header')

def test_get_columns_raise_exception_if_not_found(set_csv_file):
    """Should raise ValueError if one of the headers is not found."""

    got = xsniper.CSVFile(set_csv_file)
    with pytest.raises(ValueError):
        got.get_columns('header1', 'unknown_header', 'header3')

