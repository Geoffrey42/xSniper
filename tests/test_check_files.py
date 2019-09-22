# -*- coding: utf-8 -*-

"""Check file tests suite."""

from io import StringIO
import pytest
from .context import xsniper

def test_check_files_when_both_exist(fs):
    """Should return True if both files exist."""

    test_files = ["/var/data/src.csv", "/var/data/target.csv"]

    for single_file in test_files:
        fs.create_file(single_file)
    got = xsniper.check_files(test_files[0], test_files[1])

    assert got == True

def test_check_files_when_one_does_not_exist(fs):
    """Should return False if both files exist."""

    exist = "/var/data/src.csv"
    does_not_exist = "/var/data/target.csv"

    fs.create_file(exist)
    got = xsniper.check_files(exist, does_not_exist)

    assert got == False