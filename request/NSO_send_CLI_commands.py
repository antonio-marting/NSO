import requests


url = 'http://172.17.0.2:8888/restconf/data/'
url_resource = 'tailf-ncs:devices/device=ios-router-01/live-status/tailf-ned-cisco-ios-stats:exec/any'
method='post'
headers = {
    "Content-Type": "application/yang-data+json",
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Accept": "application/yang-data+json"
}

payload = '''{
  "input":
  {
    "args": "show ip interface brief"
  }
}'''

req = requests.request(
    method=method,
    url=url+url_resource,
    headers=headers,
    data=payload
)

print(req.status_code, req.reason, req.text)
