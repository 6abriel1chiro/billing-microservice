class BillDTO:
    def __init__(
        self,
        billID=None,
        billUserName=None,
        billConcept=None,
        billAmount=None,
        billDate=None,
    ):
        self.billID = billID
        self.billUserName = billUserName
        self.billConcept = billConcept
        self.billAmount = billAmount
        self.billDate = billDate

    @staticmethod
    def fromEntity(bill):
        return BillDTO(
            billUserName=bill.billUserName,
            billConcept=bill.billConcept,
            billAmount=bill.billAmount,
            billDate=bill.billDate,
        )
