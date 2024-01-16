# datasette-test

[![PyPI](https://img.shields.io/pypi/v/datasette-test.svg)](https://pypi.org/project/datasette-test/)
[![Tests](https://github.com/datasette/datasette-test/actions/workflows/test.yml/badge.svg)](https://github.com/datasette/datasette-test/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-test?include_prereleases&label=changelog)](https://github.com/datasette/datasette-test/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-test/blob/main/LICENSE)

Utilities to help write tests for Datasette plugins and applications

## Installation

Install this library using `pip`:
```bash
pip install datasette-test
```
## Tests that use plugin configuration

Datasette 1.0a8 enforced a configuration change where plugins are no longer configured in metadata, but instead use a configuration file.

This can result in test failures in projects that use the `Datasette(metadata={"plugins": {"...": "..."}})` pattern to test out plugin configuration.

You can solve this using `datasette_test.Datasette`, a subclass that works with Datasette versions both before and after this breaking change:

```python
from datasette_test import Datasette
import pytest

@pytest.mark.asyncio
async def test_datasette():
    ds = Datasette(plugin_config={"my-plugin": {"config": "goes here"})
```
This subclass detects if the underlying plugin needs configuration in metadata or config and instantiates the class correctly either way.

You can also use this class while continuing to pass `metadata={"plugins": ...}` - the class will move that configuration to config when necessary.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-test
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
