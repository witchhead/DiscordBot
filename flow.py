import requests
import json

id_url = "https://api.pubg.com/shards/steam/players?filter[playerNames]="
match_url = "https://api.pubg.com/shards/steam/matches/"

header = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxZGU1MDA4MC00NzU2LTAxMzktYWUxOS0wNWJlYjRhNDA1NTYiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjEyMjUwODg2LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6IndpdGNoaGVhZGJvdCJ9.k44aFAz1MSkDu7G9z0lJlLZ_TTDIVf5MLgkdhI2COqg",
  "Accept": "application/vnd.api+json"
}
p_Name = 'Blackwalk'
url = id_url + p_Name
req = requests.get(url, headers=header)
id_json = req.json()
app_id = id_json['data'][0]['id']
data = id_json['data'][0]['relationships']['matches']['data']
for i in range(0, 1):
    url = match_url + data[i]['id']
    req = requests.get(url, headers=header)
    m_json = req.json()
    print(m_json['data'])