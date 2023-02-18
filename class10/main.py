
#first i need to import requests module
import requests

#api data url
url = "https://api.ipify.org/?format=json"

#need to check status code id it 200 then ok
res = requests.get(url)
print(res.status_code)

data = res.json()
print(data)

ip = data["ip"]
print("your ip address is", ip)


#now we find location using this ip
iplocation_url = f"https://ipapi.co/{ip}/json/"

r = requests.get(iplocation_url)
data2 = r.json()
print(data2)