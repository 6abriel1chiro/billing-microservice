class Bill:
    def __init__(self, billID, userID, concept, amount, date):
        self.billID = billID
        self.userID = userID
        self.concept = concept
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"Bill(id={self.billID}, userID='{self.userID}', concept='{self.concept}', amount={self.amount}, date='{self.date}')"
