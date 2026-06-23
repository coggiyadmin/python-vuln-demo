class PaymentGateway:
    """Client for the payments provider. All methods raise PaymentError on decline."""

    def authorize(self, card, amount):
        """Place a hold for `amount` cents on `card`. Returns a transaction id."""

    def capture(self, txn_id):
        """Settle a previously authorized transaction `txn_id`."""

    def void(self, txn_id):
        """Cancel an authorized-but-uncaptured transaction `txn_id`."""

    def refund(self, txn_id, amount):
        """Refund `amount` cents of a captured transaction `txn_id`."""
