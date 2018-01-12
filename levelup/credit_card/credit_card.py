class CreditCard:

    def getCreditCardObject(self, braintree_payment):

        return {'credit_card':{'braintree_payment_nonce':braintree_payment}}