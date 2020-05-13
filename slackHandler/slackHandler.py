import requests
import json
def send():
    auth_token=''
    text = input("Please type message content ")
    header = {'Authorization': 'Bearer ' + auth_token}
    data = {"channel" : "CQP9DQM8X", "text": text}
    url = 'https://slack.com/api/chat.postMessage'
    response = requests.post(url, json=data, headers=header)
    print(response)
    print(response.json())
send()