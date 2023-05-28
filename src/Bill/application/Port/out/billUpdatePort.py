from adapters.out.MailServiceAdapter import MailServiceAdapter


class UpdateBillPort:
    def __init__(self):
        self.mailingAdapter = MailServiceAdapter()

    def updateBill(self, billID, newUsername):
        self.mailingAdapter.changeUsername(billID, newUsername)
