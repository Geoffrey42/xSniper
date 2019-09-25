"""xSniper is just a small utility of CSV file columns and cells.

Usage:
    xSniper cell <src.csv> <target.csv> <common-key> [--target-header=<key-header>] (<value-header> | --new-header=<name>) [--output=<output.csv> | -o=<output.csv>]
    xSniper column <src.csv> <target.csv> (<target-header>... | -a | --all) [--output=<output.csv> | -o=<output.csv>]
    xSniper (--help | -h)
    xSniper (--version | -v)

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    cell            if -o is present: write value found in <target.csv>
                    with content from <src.csv> under <value-header> or --new-header in <output.csv>. If not, write in <src.csv>. <common-key must be present in both *.csv files>
    column          if -o is present: write entire <target-header>'s <target.csv> in <output.csv>. If not, write in <result.csv>
"""

import os, sys

path = os.path.dirname(os.path.dirname(__file__)) 
sys.path.append(path)

from docopt import docopt
from xsniper.csv_file import CSVFile

# pylint: skip-file

def perform_cell(args, src, target):
    """Execute xSniper in cell mode.
    In this mode, xSniper add a value to an existing CSVFile (src)
    from another one (target).

    Args:
        args: docopt dictionnary.
        src: CSVFile object containing <src.csv>.
        target: CSVFile object containing <target.csv>

    Returns:
        src with some value from target.
    """

    value = target.get_value(args["--target-header"])
    src.add_value(args["<value-header>"], value)
    return src

def open_files(args, mode):
    """Open both src and target csv files.

    Args:
        args: docopt dictionnary.
        mode: string whom value can be either 'cell' or 'column.
        Depending on prefered mode.

    Returns:
        src and target CSVFile objects.
    """

    with open(args["<src.csv>"], 'rt') as src_file, open(args["<target.csv>"], 'rt') as target_file:
        if mode == "cell":
            src = CSVFile(src_file, args["<common-key>"])
            target = CSVFile(target_file, args["<common-key>"])
            return src, target
        elif mode == "column":
            src = CSVFile(src_file)
            target = CSVFile(target_file)
            return src, target

if __name__ == "__main__":
    args = docopt(__doc__, version='xSniper 1.0')

    if args["cell"]:
        src, target = open_files(args, "cell")
        src = perform_cell(args, src, target)
    elif args["column"]:
        src, target = open_files(args, "column")
        src = perform_column(args, src, target)

    if args["--output"]:
        src.write(args["--output"])
    else:
        src.write(args["<src.csv>"])
