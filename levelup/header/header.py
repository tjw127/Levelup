from application.application import Application

class LevelUpHeader:
    def header(self):
        header = {'Content-Type':Application.json.value, 'Accept':Application.json.value}
        return header
    def merhant_header(self, token):
        token_name = 'token merchant='
        token_name += token
        header = {'Content-Type': Application.json.value, 'Accept': Application.json.value, 'Authorization': token_name }

        return header

    def user_header(self, token):
        token_name = 'token user='
        token_name += token
        header = {'Content-Type': Application.json.value, 'Accept': Application.json.value, 'Authorization': token_name }

        return header
