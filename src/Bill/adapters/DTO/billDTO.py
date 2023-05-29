class BillDTO:
    def __init__(
        self,
        billID=None,
        billUserID=None,
        billConcept=None,
        billAmount=None,
        billDate=None,
    ):
        self.billID = billID
        self.billUserID = billUserID
        self.billConcept = billConcept
        self.billAmount = billAmount
        self.billDate = billDate

    @staticmethod
    def fromEntity(bill):
        return BillDTO(
            billUserID=bill.billUserID,
            billConcept=bill.billConcept,
            billAmount=bill.billAmount,
            billDate=bill.billDate,
        )
