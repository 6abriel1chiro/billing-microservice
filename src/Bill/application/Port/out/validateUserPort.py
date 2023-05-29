from adapters.out.UserAdminAdapter import UserAdminAdapter


class validateUserPort:
    def __init__(self):
        self.validationAdapter = UserAdminAdapter()

    def getUser(self, userID):
        return self.validationAdapter.getUserInfo(userID)
