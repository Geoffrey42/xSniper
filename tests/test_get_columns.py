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
cell1,cell2,
cell4,cell5,cell6""")
    return in_memory_csv

def test_get_columns(set_csv_file):
    """Should return desired column."""

    got = xsniper.CSVFile(set_csv_file)
    df = pd.read_csv(set_csv_file)
    want = df['header2']
    assert got.get_columns('header2') == want

    