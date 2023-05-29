import requests


class UserAdminAdapter:
    def __init__(self):
        self.baseUrl = "https://65db-181-177-183-178.ngrok-free.app/"

    def getUserInfo(self, userID):
        endpoint = "/users/" + str(userID)
        url = self.baseUrl + endpoint

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("User exists.")
                data = response.json()
                return data
            else:
                print("Failed to get username. Status code:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
