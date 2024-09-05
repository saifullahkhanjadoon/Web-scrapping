import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter GitHub user:")

url = 'https://github.com/' + github_user
r = requests.get(url)

soup = bs(r.content, 'html.parser')

# Look for the 'avatar-user' class which is commonly used for GitHub profile images
profile_image = soup.find('img', {'class': 'avatar-user'})['src']

print(profile_image)
