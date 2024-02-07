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
    response2 = await ds.client.get("/-/config.json")
    assert response.json() == {}
    if response2.status_code == 200:
        assert response2.json() == {}

    # Now configure it
    ds = Datasette(**kwargs)
    if plugin_config_should_be_in_metadata:
        response3 = await ds.client.get("/-/metadata.json")
        assert response3.json() == {"plugins": {"foo": "bar"}}
    else:
        # Should be in /-/config.json and not /-/metadata.json
        response4 = await ds.client.get("/-/metadata.json")
        response5 = await ds.client.get("/-/config.json")
        assert response4.json() == {}
        assert response5.json() == {"plugins": {"foo": "bar"}}


def test_wait_until_responds():
    wait_until_responds("https://www.example.com/")
