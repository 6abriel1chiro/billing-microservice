import mysql.connector
from core.Entity.bill import Bill
import yaml


class BillRepository:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    @staticmethod
    def getInstance():
        configFile = "src/Bill/config/billRepository.yaml"

        with open(configFile) as f:
            config = yaml.safe_load(f)
        host = config["host"]
        username = config["username"]
        password = config["password"]
        database = config["database"]
        return BillRepository(host, username, password, database)

    def __connectToDB__(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database,
        )
        return connection

    def create(self, bill: Bill) -> Bill:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        insert_query = (
            "INSERT INTO bills (userID, concept,  amount, date) VALUES (%s, %s, %s, %s)"
        )
        values = (bill.userID, bill.concept, bill.amount, bill.date)
        print("!!!!!!!!!!!!!!!!!!")
        print(insert_query, values)
        cursor.execute(insert_query, values)
        billID = cursor.lastrowid
        bill.billID = billID
        connection.commit()
        cursor.close()
        connection.close()
        return bill

    def get_by_id(self, billID: int) -> Bill:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        select_query = (
            "SELECT userID, concept, amount, date FROM bills WHERE billID = %s"
        )
        cursor.execute(select_query, (billID,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            userID, concept, amount, date = result
            return Bill(billID, userID, concept, amount, date)
        return None

    def update(self, bill: Bill) -> Bill:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        update_query = "UPDATE bills SET userID = %s, concept = %s, amount = %s, date = %s WHERE billID = %s"
        values = (
            bill.userID,
            bill.concept,
            bill.amount,
            bill.date,
            bill.billID,
        )
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return bill

        connection = self.__connectToDB__()

    def delete(self, billID: int) -> None:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        delete_query = "DELETE FROM bills WHERE billID = %s"
        cursor.execute(delete_query, (billID,))
        connection.commit()
        cursor.close()
        connection.close()

    def deletefromuser(self, userID: int) -> None:
        connection = self.__connectToDB__()
        print("!!!!!!!!!!!!!!")
        print(userID)

        cursor = connection.cursor()
        delete_query = "DELETE FROM bills WHERE userID = %s"
        cursor.execute(delete_query, (userID,))
        connection.commit()
        cursor.close()
        connection.close()
