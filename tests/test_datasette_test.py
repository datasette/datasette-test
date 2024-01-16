from datasette_test import Datasette, plugin_config_should_be_in_metadata
import pytest


@pytest.mark.asyncio
async def test_datasette_plugin_config():
    ds = Datasette()
    response = await ds.client.get("/-/metadata.json")
    assert response.json() == {}

    ds = Datasette(plugin_config={"foo": "bar"})
    response2 = await ds.client.get("/-/metadata.json")
    if plugin_config_should_be_in_metadata:
        assert response2.json() == {"plugins": {"foo": "bar"}}
    else:
        assert response2.json() == {}
