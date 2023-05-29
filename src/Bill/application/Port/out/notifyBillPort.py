from adapters.out.MailServiceAdapter import MailServiceAdapter


class NotifyBillPort:
    def __init__(self):
        self.mailAdapter = MailServiceAdapter()

    def notifyCreatedBill(self, concept, amount, userID):
        self.mailAdapter.notifyCreatedBill(concept, amount, userID)
