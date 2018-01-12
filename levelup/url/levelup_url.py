from levelup.levelup import LevelupEnum
from levelup.endpoint.levelup_endpoint import LevelUpEndpointEnum
class LevelUpUrl:
    def __init__(self):
        self.url = LevelupEnum.base_url.value

    def v15(self):
        url = self.url
        url += '/'
        url += LevelupEnum.version.value

        return url

    def access_token(self):

        url = self.v15()
        url += '/'
        url += LevelUpEndpointEnum.access_tokens.value

        return url

