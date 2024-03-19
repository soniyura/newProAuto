import requests
import json

prefix = "/Users/urakaterinenko/PycharmProjects/newProAuto"
resources_folder = "resources"
file_name = "variables.json"

#resources/variables.json

with open(f"{prefix}/{resources_folder}/{file_name}", "r") as f:
    pass
    variables = json.load(f)
    print(variables)

data = {
    "username": "Post_user",
    "email": "post@user.data",
    "groups": []
}

for user, password in variables["users"].items():
    print(user, password)
    resp = requests.get(variables['urls']['main'])
    break

print(resp.text)






# password = variables["users"]["admin"]
# user = variables["users"]["admin"].key()
#
# resp = requests.get(variables['urls']['main'], auth=(user, password))