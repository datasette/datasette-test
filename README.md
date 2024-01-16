# datasette-test

[![PyPI](https://img.shields.io/pypi/v/datasette-test.svg)](https://pypi.org/project/datasette-test/)
[![Tests](https://github.com/datasette/datasette-test/actions/workflows/test.yml/badge.svg)](https://github.com/datasette/datasette-test/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-test?include_prereleases&label=changelog)](https://github.com/datasette/datasette-test/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-test/blob/main/LICENSE)

Utilities to help write tests for Datasette plugins and applications

## Installation

Install this library using `pip`:

    pip install datasette-test

## Usage

Usage instructions go here.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd datasette-test
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
