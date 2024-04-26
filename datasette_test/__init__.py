from datasette.app import Datasette as _Datasette
from datasette.version import __version_info__
import time
import httpx


plugin_config_should_be_in_metadata = __version_info__ < ("1", "0a8")


class Datasette(_Datasette):
    def __init__(self, *args, **kwargs):
        plugin_config = kwargs.pop("plugin_config", None)
        if plugin_config is not None:
            if plugin_config_should_be_in_metadata:
                metadata = kwargs.pop("metadata", None) or {}
                metadata["plugins"] = plugin_config
                kwargs["metadata"] = metadata
            else:
                config = kwargs.pop("config", None) or {}
                config["plugins"] = plugin_config
                kwargs["config"] = config
        elif (
            "plugins" in (kwargs.get("metadata") or {})
            and not plugin_config_should_be_in_metadata
        ):
            # Move plugins to config anyway
            plugin_config = kwargs["metadata"].pop("plugins")
            kwargs["config"] = kwargs.get("config") or {}
            kwargs["config"]["plugins"] = plugin_config
        super().__init__(*args, **kwargs)


def wait_until_responds(url: str, timeout: float = 5.0):
    start = time.time()
    while time.time() - start < timeout:
        try:
            httpx.get(url)
            return
        except httpx.ConnectError:
            time.sleep(0.1)
    raise AssertionError("Timed out waiting for {} to respond".format(url))


def actor_cookie(datasette, actor):
    if hasattr(datasette.client, "actor_cookie"):
        return datasette.client.actor_cookie({"id": "root"})
    else:
        return datasette.sign({"a": actor}, "actor")
