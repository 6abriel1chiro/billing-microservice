from adapters.out.MailServiceAdapter import MailServiceAdapter


class DeleteBillPort:
    def __init__(self):
        self.mailingAdaper = MailServiceAdapter()

    def deleteBill(self, billID):
        self.mailingAdaper.deleteBill(billID)
