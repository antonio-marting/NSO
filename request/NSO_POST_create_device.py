import requests

url = 'http://172.17.0.2:8888/restconf/data/'
url_resource = 'tailf-ncs:devices'
method='post'
headers = {
    "Content-Type": "application/yang-data+xml",
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Accept": "application/yang-data+xml"
}
params = 'dry-run=native'
payload = '''
<device>
  <name>ROUTER_200</name>
  <address>10.0.0.2</address>  
  <ssh>
    <host-key>
      <algorithm>ssh-rsa</algorithm>
      <key-data>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWw8SJJiyo5cHbSXuIzM6iXEvMidM+XTUBV3AeX5M4Z+MEq41/1KMU7bT8MKBTBWMshzCAp1hqciGWEgcv8in64quSzQvcLDNZHl+sqw1PDo3r1bFpo9WYc7P5zkGhuO95n4opM6AQRJY8NGv1ElouGpEDSaryJPLWbeMVBqjZb2n43sr/6t92UMdpQ2ZnMTQfcyuRkQakhlyc6j+2RUKFgtkaNRj0oNOSVqZi6fdjaYqVV1cTzWjJzz8XYSniFqx0YFwn2+lJBD3iNSZPYTUqYSkjPYQUH+ZuFJYlZBjzkxpigCWY6aNv786/2a4KLWW5jNXpxvs0FBauE6nOBCHT root@buildkitsandbox</key-data>
    </host-key>
  </ssh>
  <state>
    <admin-state>unlocked</admin-state>
  </state>
  <authgroup>default</authgroup>
  <device-type>
    <cli>
    <ned-id>cisco-ios-cli-6.43:cisco-ios-cli-6.43</ned-id>  
    </cli>
  </device-type>
</device>
'''
req = requests.request(
    method=method,
    url=url+url_resource,
    headers=headers,
    data=payload,
    params=params
)

print(req.status_code, req.reason, req.text)
