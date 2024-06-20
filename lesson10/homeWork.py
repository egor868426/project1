import requests

response = requests.get("https://example.com")
print(response.text)




import requests

params = {"param1": "value1", "param2": "value2"}
response = requests.post("https://example.com", params=params)
print(response.url)
print(response.text)




import requests
data = {"username", "example", "password"}
response = requests.post("https://example.com", data=data)
print(response.text)




import requests
response = requests.get("https://example.com")
print("Headers:", response.headers)
print("Content:", response.content)




import requests

try:
    response = requests.get("https://example.com")
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(f"HTTP error occurred: {error}")




import requests

response = requests.get("https://example.com")

with open("output.html", "w", encoding='utf-8') as file:
    file.write(response.text)