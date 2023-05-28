import requests


class MailServiceAdapter:
    def __init__(self):
        self.baseUrl = "baseUrl"

    def changeUsername(self, billID, newUsername):
        endpoint = "/changeUsername/" + str(userID)
        url = self.baseUrl + endpoint

        payload = {"new_username": newUsername}

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Username changed successfully.")
            else:
                print("Failed to change username. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))

    def changeAmmount(self, billID, newAmmount):
        endpoint = "/changeAmmount/" + str(billID)
        url = self.baseUrl + endpoint

        payload = {"new_ammount": newAmmount}

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Ammount changed successfully.")
            else:
                print("Failed to change ammount. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))

    def sendMail(self, billID, userName, concept, amount, date):
        mail = (
            userName
            + " has paid "
            + str(amount)
            + "€ for "
            + concept
            + " on "
            + date
            + "."
        )
        print(mail)

        endpoint = "/sendMail/" + str(billID)
        url = self.baseUrl + endpoint

        payload = {"mail": mail}

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                print("Mail sent successfully.")
            else:
                print("Failed to send mail. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
