from adapters.out.MailServiceAdapter import MailServiceAdapter


class CreateBillPort:
    def __init__(self):
        self.mailAdapter = MailServiceAdapter()

    def createBill(self, billID, userName, concept, amount, date):
        self.mailAdapter.sendMail(billID, userName, concept, amount, date)
