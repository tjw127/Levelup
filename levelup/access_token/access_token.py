from levelup.levelup import LevelupEnum
from levelup.header.header import LevelUpHeader
from levelup.url.levelup_url import LevelUpUrl
import json
import requests
class AccessToken:
    def access_token(self):

        access_token = {'api_key':LevelupEnum.api_key.value, 'client_secret':LevelupEnum.client_secret.value}

        return access_token

    def getAccessTokenObject(self, api_key, username, password):

        return {'access_token':{'api_key':api_key, 'username':username, 'password':password}}

    def getAccessToken(self):

        keys = self.access_token()

        levelUpHeader = LevelUpHeader()

        header = levelUpHeader.header()

        url = LevelUpUrl()
        keys_json = json.dumps(keys)

        r = requests.post(url=url.access_token(), data=keys_json, headers=header)

        return json.loads(r.content)



