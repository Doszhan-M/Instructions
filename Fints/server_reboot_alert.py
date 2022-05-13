import requests
url = "https://api.telegram.org/bot1986627459:AAG04-Gffa3S47d1J9N9MZSXTEPJexKRw38/sendMessage?chat_id=-523535813&text=Server was rebooted"
response = requests.request("GET", url,)
print(response.text)
