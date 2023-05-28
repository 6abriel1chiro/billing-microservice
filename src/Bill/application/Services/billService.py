from application.Port.In.crudUseCase import CrudBillCase
from core.Entity.bill import Bill
from adapters.DTO.billDTO import BillDTO
from application.Port.out.createBillPort import CreateBillPort
from application.Port.out.billUpdatePort import UpdateBillPort
from application.Port.out.deleteBillPort import DeleteBillPort


class BillService:
    def __init__(self):
        self.billUseCase = CrudBillCase()

    def createBill(self, billDTO: BillDTO) -> Bill:
        createdBill = self.billUseCase.createBill(
            billDTO.billUserName,
            billDTO.billConcept,
            billDTO.billAmount,
            billDTO.billDate,
        )
        return createdBill

    def getBill(self, billDTO: BillDTO) -> Bill:
        return self.billUseCase.getBill(billDTO.billID)

    def updateBill(self, billDTO: BillDTO) -> Bill:
        modifiedBill = self.billUseCase.updateBill(
            billDTO.billID,
            billDTO.billUserName,
            billDTO.billConcept,
            billDTO.billAmount,
            billDTO.billDate,
        )
        return modifiedBill

    def deleteBill(self, billDTO: BillDTO) -> None:
        self.billUseCase.deleteBill(billDTO.billId)
        DeleteUserPort().deleteUser(billDTO.billId)
