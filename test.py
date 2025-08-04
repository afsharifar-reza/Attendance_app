import requests
ip = requests.get("https://smsapi.pishgamrayan.com/api/Message/GetIp").text
print("Your IP:", ip)
