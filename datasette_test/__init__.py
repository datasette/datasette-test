from datasette.app import Datasette as _Datasette
import time
import httpx


try:
    from datasette.utils import fail_if_plugins_in_metadata

    plugin_config_should_be_in_metadata = False
except ImportError:
    plugin_config_should_be_in_metadata = True


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
