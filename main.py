import json
import requests
from datetime import datetime
from requests.exceptions import HTTPError

from account import ACCOUNT

API = "https://pixe.la/v1/users/"
INTERVAL = 5

# ACCOUNT = {
#     "token": <yourTokenAsString>,
#     "username": <yourUsernameAsString>,
#     "graph": "howlongitran",
# }

now = str(datetime.now())
log = {now: {}}

class MyPixelaAccount:
    def __init__(self, account):
        self.token = account["token"]
        self.username = account["username"]
        self.graph = account["graph"]
        self.update_pixel(datetime.now().strftime("%Y%m%d"))

    def create(self):
        global log
        endpoint = API
        parameters = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        try:
            response = requests.post(url=endpoint, json=parameters)
            log[now]["create"] = response.text
            response.raise_for_status()
        except:
            pass
    
    def create_graph(self):
        global log
        endpoint = API + f"{self.username}/graphs"
        header = {"X-USER-TOKEN": self.token}
        parameters = {
            "id": self.graph,
            "name": "How Long My Computer Ran",
            "unit": "minutes",
            "type": "int",
            "color": "momiji",
        }
        try:
            response = requests.post(url=endpoint, headers=header, json=parameters)
            log[now]["graph"] = response.text
            response.raise_for_status()
        except:
            self.create()
            self.create_graph()
    
    def create_pixel(self, date):
        global log
        endpoint = API + f"{self.username}/graphs/{self.graph}"
        header = {"X-USER-TOKEN": self.token}
        parameters = {
            "date": date,
            "quantity": str(INTERVAL),
        }
        try:
            response = requests.post(url=endpoint, headers=header, json=parameters)
            log[now]["post"] = response.text
            response.raise_for_status()
        except:
            self.create_graph()
            self.create_pixel(date)

    def update_pixel(self, date):
        global log
        endpoint = API + f"{self.username}/graphs/{self.graph}/{date}"
        header = {"X-USER-TOKEN": self.token}
        try:
            response = requests.get(url=endpoint, headers=header)
            response.raise_for_status()
        except HTTPError:
            log[now]["update"] = response.text
            self.create_pixel(date)
        else:
            log[now]["update"] = "OK"
            actual_data = int(response.json()["quantity"])
            new_data = actual_data + INTERVAL
            parameters = {"quantity": str(new_data)}
            response = requests.put(url=endpoint, headers=header, json=parameters)


my_account = MyPixelaAccount(ACCOUNT)

print(log)
try:
    with open("log.json", "r") as log_file:
        data = json.load(log_file)
except FileNotFoundError:
    data = log
else:
    data.update(log)
finally:
    with open("log.json", "w") as log_file:
        json.dump(data, log_file, indent=4)
