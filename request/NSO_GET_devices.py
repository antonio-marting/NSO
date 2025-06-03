import requests

'''https://www.postman.com/ciscodevnet/cisco-devnet-s-public-workspace/collection/09lmnqd/nso-sample-api-requests'''

'''https://developer.cisco.com/docs/nso/single-device-config/'''

url = 'http://172.17.0.2:8888/restconf/data/'
url_resource = 'tailf-ncs:devices/device-group=XR-IOS/ned-id/'
method='get'
app = 'json'
headers = {
    "Content-Type": f"application/yang-data+{app}",
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Accept": f"application/yang-data+{app}"
}

payload = '''
<devices xmlns="http://tail-f.com/ns/ncs">
  <device-group>
    <name>XE-IOS</name>
    <device-name>ios-router-01</device-name>
    <device-name>ios-router-02</device-name>
  </device-group>
  <device-group>
    <name>XR-IOS</name>
    <device-name>xr-router-03</device-name>
    <device-name>xr-router-04</device-name>
  </device-group>
  <device-group>
    <name>ORPHAN</name>
    <device-name>ROUTER_100</device-name>
  </device-group> 
</devices>'''

req = requests.request(
    method=method,
    url=url+url_resource,
    headers=headers,
    data=payload
)

print(req.url, req.status_code, req.reason, req.text)

#with open ('/home/antonio/AutomationTools/docker/NSO_conf.json', 'w') as fw:
#    wr_file = fw.write(req.text)
#    fw.close()