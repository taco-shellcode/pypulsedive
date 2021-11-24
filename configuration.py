import json

class Configuration(object):

    def __init__(self, **kwargs):
        self.api_key = ""
        self.api_url = "https://www.pulsedive.com"

        for keyword_argument in kwargs:
            if hasattr(self, keyword_argument):
                setattr(self, keyword_argument, kwargs[keyword_argument])

    @staticmethod
    def from_dictionary(config_dict: dict):
        return Configuration(**config_dict)

    @staticmethod
    def from_json(config_json: str):
        return Configuration.from_dictionary(json.loads(config_json))