class Registration:


    def getRegistrationObject(self, app_name, description, facebook):
        return {'registration':{'app_name':app_name, 'description':description, 'facebook':facebook}}