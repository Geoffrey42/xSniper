# -*- coding: utf-8 -*-

"""Add value tests suite."""

from io import StringIO
import pytest
from xsniper.csv_file import CSVFile
from xsniper.main import perform_cell

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""

    src_csv = StringIO("""\
header1,header2,header3
cell1,cell2,
cell4,cell5,cell6""")

    target_csv = StringIO("""\
header1,header2,header3
cell1,cell2,cell3
cell4,cell5,cell6""")

    args = {
        "<common-key>": "cell1",
        "--target-header": "header3",
        "<value-header>": "header3"
    }

    src = CSVFile(src_csv, args["<common-key>"])
    target = CSVFile(target_csv, args["<common-key>"])
    return src, target, args

def test_return_CSVFile_object(set_csv_file):
    """Should return a CSVFile object with identical content with target."""

    src, target, args = set_csv_file

    perform_cell(args, src, target)
    assert src.content == target.content