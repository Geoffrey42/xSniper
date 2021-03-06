# xSniper

[![Build Status](https://travis-ci.com/Geoffrey42/xSniper.svg?branch=develop)](https://travis-ci.com/Geoffrey42/xSniper)
[![codecov](https://codecov.io/gh/Geoffrey42/xSniper/branch/develop/graph/badge.svg)](https://codecov.io/gh/Geoffrey42/xSniper)
[![Updates](https://pyup.io/repos/github/Geoffrey42/xSniper/shield.svg)](https://pyup.io/repos/github/Geoffrey42/xSniper/)
[![Python 3](https://pyup.io/repos/github/Geoffrey42/xSniper/python-3-shield.svg)](https://pyup.io/repos/github/Geoffrey42/xSniper/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Just a little CSV columns and cells utility.


## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
  * [From command line](#from-command-line)
  * [Examples](#examples)
* [Contributing](#contributing)
* [License](#license)

## Prerequisites

* [pip](https://pip.pypa.io/en/stable/)
* [virtualenv](https://pypi.org/project/virtualenv/)

## Installation

```bash
git clone git@github.com:Geoffrey42/xSniper.git
cd /xSniper
virtualenv venv
source venv/bin/activate
```

You should now see your prompt prefixed by:

```bash
(venv) $
```

The first time, run:

```bash
pip install -r requirements.txt
```

## Usage

### From command line

```text
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
```

### Examples

#### Cell mode

![cell mode](./assets/xSniper_cell_charts_00.png)

#### Column mode

![cell mode](./assets/xSniper_column_charts_00.png)

## Contributing

Pull requests are welcome.
For more details, please refers to our [contributing file](.github/CONTRIBUTING/contributing.md).

## License

[MIT](./LICENSE)
