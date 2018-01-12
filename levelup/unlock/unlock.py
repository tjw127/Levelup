class Unlock:

    def campaign_unlocking(self, target_campaign_id, user_id, expires_at):

        return {'campaign_unlocking':{'target_campaign_id':target_campaign_id, 'user_id':user_id, 'expires_at':expires_at}}