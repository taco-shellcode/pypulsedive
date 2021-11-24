import requests
import urllib.parse

from .models import Indicator
from ..configuration import Configuration

class InfoApi(object): 

    def __init__(self, config: Configuration):
        self._config = config

    def get_indicator_by_value(self, indicator):
        api_response = requests.get(
            url = urllib.parse.urljoin(self._config.api_url, f"/api/info.php?indicator={urllib.parse.quote_plus(indicator)}&key={self._config.api_key}"),
        )

        #if api_response.status_code == 404: #and "indicator not found." in (api_response.content["error"]).lower():
            #print(api_response.content.error)


        response_json = api_response.json()
        #indicator = Indicator.from_dictionary(response_json)
        #return indicator
        return response_json