# app/core/use_cases/user_use_case.py
from core.Entity.bill import Bill
from adapters.repositories.billRepository import BillRepository


class CrudBillCase:
    def __init__(self):
        self.BillRepository = BillRepository.getInstance()

    def createBill(self, username: str, concept: str, amount: float, date: str) -> Bill:
        bill = Bill(None, username, concept, amount, date)
        return self.BillRepository.create(bill)

    def getBill(self, billID: int) -> Bill:
        bill = self.BillRepository.get_by_id(billID)
        return bill

    def updateBill(
        self, billID: int, username: str, concept: str, amount: float, date: str
    ) -> Bill:
        bill = self.BillRepository.get_by_id(billID)
        if not bill:
            return None
        bill.username = username
        bill.concept = concept
        bill.amount = amount
        bill.date = date
        return self.BillRepository.update(bill)

    def deleteBill(self, billID: int) -> None:
        self.BillRepository.delete(billID)

    def deleteBillFromUser(self, billUserID: int) -> None:
        self.BillRepository.deletefromuser(billUserID)
