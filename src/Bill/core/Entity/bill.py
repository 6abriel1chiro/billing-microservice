class Bill:
    def __init__(self, billID, username, concept, ammount, date):
        self.billID = billID
        self.username = username
        self.concept = concept
        self.ammount = ammount
        self.date = date

    def __repr__(self):
        return f"Bill(id={self.billID}, username='{self.username}', concept='{self.concept}', ammount={self.ammount}, date='{self.date}')"
