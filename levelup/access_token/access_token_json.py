class AccessTokenJSON:

    def __init__(self, json):
        self.json = json

    def access_token(self):

        return self.json['access_token']

    def app_id(self):

        app_id = self.access_token()['app_id']

        return app_id

    def merchant_id(self):

        merchant_id = self.access_token()['merchant_id']

        return merchant_id

    def token(self):

        token = self.access_token()['token']

        return token

    def user_id(self):

        user_id = self.access_token()['user_id']

        return user_id