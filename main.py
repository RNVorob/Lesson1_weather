import requests

url1 = "https://wttr.in/Лондон?nTqmM&lang=ru"
url2 = "https://wttr.in/Шереметьево?nTqmM&lang=ru"
url3 = "https://wttr.in/Череповец?nTqmM&lang=ru"

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)

print(response1.text, response2.text, response3.text, sep='\n')
