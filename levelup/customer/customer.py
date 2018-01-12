class Customer:

    def getCustomerPaymentObject(self, token):

        return {'customer':{'payment_token_data':token}}