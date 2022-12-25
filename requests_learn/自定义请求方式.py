import json

import requests

url = "http://192.168.5.93:8068/browse/find"

payload = json.dumps(
    {
        "key": "88616218-5bfd-11ec-9790-e0d55eeff354",
        "secret": "2ece56bedccd8535fb7a2bddc23ff7c505e5541c4924ed90befc02db9504d75e",
        "app_id": "b73378d8750b11ec9e28e0d55eeff354",
        "sales_id": "1",
        "page": 1,
        "size": 10,
    }
)
headers = {"Content-Type": "application/json"}

response = requests.request("POSTT", url, headers=headers, data=payload)

print(response.text)
