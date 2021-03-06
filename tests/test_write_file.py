# -*- coding: utf-8 -*-

"""Write content to file tests suite."""

import unittest
import pytest
from unittest.mock import patch, mock_open
from io import StringIO
from .context import xsniper

@pytest.fixture
def set_csv_file():
    """Instantiate CSVFile object as a setup for every test."""

    in_memory_csv = StringIO("""\
header1,header2,header3
cell1,cell2,
cell4,cell5,cell6""")
    return in_memory_csv

def test_file_opened_in_w_mode(set_csv_file):
    """Should have opened a file in write mode."""

    got = xsniper.CSVFile(set_csv_file, "cell1")
    fake_file_path = "fake/file/path"
    with patch('xsniper.csv_file.open', mock_open()) as mocked_file:
        got.write(fake_file_path)
    
    mocked_file.assert_called_once_with(fake_file_path, 'w')

def test_write_called_with_content(set_csv_file):
    """Should call write with content."""

    got = xsniper.CSVFile(set_csv_file, "cell1")
    fake_file_path = "fake/file/path"
    with patch('xsniper.csv_file.open', mock_open()) as mocked_file:
        got.write(fake_file_path)

    called_number = mocked_file().write.call_count

    assert called_number == 3
