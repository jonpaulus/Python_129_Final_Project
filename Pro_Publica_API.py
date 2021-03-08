import requests, json

pro_publica_req = requests.get('https://api.propublica.org/congress/v1/senate/votes/recent.json', headers ={"X-API-Key" : ""})
print(pro_publica_req)

if (int(pro_publica_req.status_code) == 200):
    pro_republica_response = json.loads(pro_publica_req.text)
    print (pro_republica_response)
