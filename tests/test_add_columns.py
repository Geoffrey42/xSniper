# -*- coding: utf-8 -*-

"""Add columns tests suite."""

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

def test_add_single_column():
    """Should add the desired column."""

    test_csv = StringIO("""\
header1,header3
cell1,cell3
cell4,cell6""")

    test_single_column = StringIO("""\
header2
cell2
cell5""")
    got = xsniper.CSVFile(test_csv)
    df = pd.read_csv(test_single_column, index_col=None, header=0)
    want = df['header2']

    got.add_columns(want)
    assert got.get_single_column('header2').equals(want)

def test_add_several_columns():
    """Should add several columns."""

    test_csv = StringIO("""\
header1,header3
cell1,cell3
cell4,cell6""")

    test_single_column = StringIO("""\
header2,header4
cell2,cell7
cell5,cell8""")
    df = pd.read_csv(test_single_column, index_col=None, header=0)
    h2 = df['header2']
    h4 = df['header4']
    want = pd.concat([h2, h4], ignore_index=False, axis=1)

    got = xsniper.CSVFile(test_csv)
    got.add_columns(want)
    assert got.get_columns('header2', 'header4').equals(want)
