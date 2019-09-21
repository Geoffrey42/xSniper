"""Some valuable helpers for CSV parsing and manipulation."""

import os

def check_files(file_1, file_2):
    """Check files existence in user file system.

    Args:
        file_1: A file path as a string.
        file_2: Same thing.
    Returns:
        True or False whether both files exist or one, at least, doesn't.
    """

    files = [file_1, file_2]
    for single_file in files:
        if not os.path.isfile(single_file):
            return False
    return True
