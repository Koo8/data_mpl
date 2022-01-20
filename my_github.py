from pprint import pprint
import requests
from github import Github

# pip install pygithub to access github module
username = 'koo8'
g = Github()
user = g.get_user(username)
# url = f'https://api.github.com/users/{username}'
# my_repos = requests.get(url).json()
# pprint(my_repos)

for repo in user.get_repos():
    # print(repo) # Repository(full_name="Koo8/2DSpriteGame") .... I have 43 right now
    print(repo.full_name)
    print(repo.description)
    print('---------------------------------')