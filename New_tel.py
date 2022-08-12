import json, requests

def get_user(d):
    data = []
    for i in d:
        if i['countryCode'] == 'UZ':
            data.append({'name':i['name'], 'callingCode':i['callingCode'], 'countryCode':i['countryCode']})
    return data
url = 'https://randommer.io/api/Phone/Countries'
d = {'X-Api-Key':'3ad41b2a1ece4d749d0e240af917af2d'}
r = requests.get(url, headers=d)
r1 = r.json()
x = get_user(r1)
with open('json.json', 'w') as file:
    json.dump(x, file, indent=2)