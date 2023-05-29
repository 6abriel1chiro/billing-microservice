import requests


class MailServiceAdapter:
    def __init__(self):
        self.baseUrl = "https://de6b-200-87-92-94.ngrok-free.app/"

    def notifyCreatedBill(self, concept, amount, userID):
        endpoint = "/send_mail/new_bill_info"
        url = self.baseUrl + endpoint

        payload = {"concept": concept, "amount": amount, "userID": userID}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("bill sent successfully.")
            else:
                print("Failed to send bill. Status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
