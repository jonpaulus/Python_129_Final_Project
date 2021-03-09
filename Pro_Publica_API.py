import requests, json

with open("pro_publica_api.txt") as f:
    pro_publica_key = f.read()

pro_publica_req = requests.get('https://api.propublica.org/congress/v1/senate/votes/recent.json', headers ={"X-API-Key" : pro_publica_key})
print(pro_publica_req)

if (int(pro_publica_req.status_code) == 200):
    pro_republica_response = json.loads(pro_publica_req.text)
    print (pro_republica_response)
