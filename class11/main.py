
from requests import get
from pprint import pprint

base_url = "https://mobile-price-bd.com/wp-json/wp/v2/posts"

response = get(base_url)

data = response.json()

for post in data:
    posts = post.get("title").get("rendered")
    print(posts)
