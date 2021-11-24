from .configuration import Configuration
from .api import Indicator, InfoApi


config = Configuration()

def search_for_indicator(indicator: str) -> Indicator:
    if not config.api_key:
        raise ValueError("ERROR - No API key was provided.")

    info_api = InfoApi(config)

    return info_api.get_indicator_by_value(indicator)


__all__ = [
    "config",
    "search_for_indicator"
]