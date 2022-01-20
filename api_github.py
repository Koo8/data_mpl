import json
import pprint

import requests

url= 'https://api.github.com/users/TheAlgorithms'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers) # a response has 3 parts, status, header and body
response_json = r.json()
# pprint.pprint(response_json[0]['description'])
# print(len(response_json)) # 30 repos are displayed
# with open('github_user.json','w') as file:
#     json.dump(response_json,file, indent=4)
repos_descriptions = []
for repo in response_json:
    repos_descriptions.append(repo['description'])

# print(repos_descriptions)

with open('github_description.json','w') as file:
    for l in repos_descriptions:
        file.write(str(l) + '\n')