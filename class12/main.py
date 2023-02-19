
from requests import get
from pprint import pprint

api_key = "7528421-e4cf646978f7cb7446adb39c9"

keywords = input("write your keyword")
keyword = keywords.replace(" ", "-")
print(keyword)


api_url = f"https://pixabay.com/api/?key={api_key}&q={keyword}&image_type=photo&pretty=true"
res = get(api_url)

rawdata = res.json()

data = rawdata.get("hits")

#for data in data:
    #url = data.get("largeImageURL")
    #print(url)
    #file = open("allurl.txt", "a+")
    #file.writelines(url+"\n")
    #file.close()


i = 0
for data in data:
    urls = data.get("largeImageURL")
    photos3 = get(urls)
    file2 = open(f"{keyword}{i}.jpg", "wb")
    file2.write(photos3.content)
    i= i+1
    file2.close()
