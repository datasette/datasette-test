from datasette_test import (
    Datasette,
    plugin_config_should_be_in_metadata,
    wait_until_responds,
)
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "kwargs",
    ({"plugin_config": {"foo": "bar"}}, {"metadata": {"plugins": {"foo": "bar"}}}),
)
async def test_datasette_plugin_config(kwargs):
    ds = Datasette()
    response = await ds.client.get("/-/metadata.json")
    assert response.json() == {}

    ds = Datasette(**kwargs)
    response2 = await ds.client.get("/-/metadata.json")
    if plugin_config_should_be_in_metadata:
        assert response2.json() == {"plugins": {"foo": "bar"}}
    else:
        assert response2.json() == {}


def test_wait_until_responds():
    wait_until_responds("https://www.example.com/")
