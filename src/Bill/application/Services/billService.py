from application.Port.In.crudUseCase import CrudBillCase
from core.Entity.bill import Bill
from adapters.DTO.billDTO import BillDTO
from application.Port.out.notifyBillPort import NotifyBillPort
from application.Port.out.billUpdatePort import UpdateBillPort
from application.Port.out.deleteBillPort import DeleteBillPort
from application.Port.out.validateUserPort import validateUserPort


class BillService:
    def __init__(self):
        self.billUseCase = CrudBillCase()

    def createBill(self, billDTO: BillDTO) -> Bill:
        user = validateUserPort().getUser(billDTO.billUserID)
        if user == None:
            return 404
        createdBill = self.billUseCase.createBill(
            billDTO.billUserID,
            billDTO.billConcept,
            billDTO.billAmount,
            billDTO.billDate,
        )
        if createdBill:
            NotifyBillPort().notifyCreatedBill(
                createdBill.concept, createdBill.amount, createdBill.userID
            )
        return createdBill

    def getBill(self, billDTO: BillDTO) -> Bill:
        return self.billUseCase.getBill(billDTO.billID)

    def updateBill(self, billDTO: BillDTO) -> Bill:
        user = validateUserPort().getUser(billDTO.billUserID)
        if user is not None:
            modifiedBill = self.billUseCase.updateBill(
                billDTO.billID,
                billDTO.billUserID,
                billDTO.billConcept,
                billDTO.billAmount,
                billDTO.billDate,
            )
            return modifiedBill
        else:
            return 404

    def deleteBill(self, billDTO: BillDTO) -> None:
        self.billUseCase.deleteBill(billDTO.billID)
        # DeleteUserPort().deleteUser(billDTO.billID)

    def deleteBillFromUser(self, billDTO: BillDTO) -> None:
        self.billUseCase.deleteBillFromUser(billDTO.billUserID)
        # DeleteUserPort().deleteUser(billDTO.billID)
