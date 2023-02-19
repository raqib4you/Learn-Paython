
#first i need to import requests module
import requests

#for good view joson data
import pprint


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




#pixabay api

key = "7528421-e4cf646978f7cb7446adb39c9"
keyword = "flowers"
url2 = f"https://pixabay.com/api/?key={key}&q={keyword}&image_type=photo&pretty=true"
res2 = requests.get(url2)
data3 = res2.json()


#pprint.pprint(data3)

photo = data3["hits"]
pprint.pprint(photo)


image = photo[0]
pprint.pprint(image)

for main in image:
    main = image["largeImageURL"]
    print(main)

