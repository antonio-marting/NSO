import requests

'''VALID for ALL these options:

admin@ncs# devices device ios-router-01 ?
Possible completions:
  add-capability        - This action adds a capability to the list of capabilities.
  capability            - A list of capabilities supported by the device
  check-sync            - Check if the NCS config is in sync with the device
  check-yang-modules    - Check if NCS and the device have compatible YANG modules
  compare-config        - Compare the actual device config with the NCS copy
  config                - NCS copy of the device configuration
  connect               - Connect to the device
  copy-capabilities     - Note: this action overwrites existing list of capabilities.
  delete-config         - Delete the config in NCS without deleting it on the device
  disconnect            - Close all sessions to the device
  find-capabilities     - This action overwrites existing list of capabilities.
  live-status           - Status data fetched from the device
  live-status-protocol  - Additional protocols for the live-tree (read-only)
  migrate               - Migrate the device to a new NED type
  netconf-notifications - NETCONF notifications from the device
  ping                  - ICMP ping the device
  rpc                   - RPCs from the device
  scp-from              - Secure copy file to the device
  scp-to                - Secure copy file to the device
  ssh                   - SSH connection configuration
  sync-from             - Synchronize the config by pulling from the device
  sync-to               - Synchronize the config by pushing to the device
'''

url = 'http://172.17.0.2:8888/restconf/data/'
#url_resource = 'tailf-ncs:devices/device=ios-router-01/ssh/fetch-host-keys'
#url_resource = 'tailf-ncs:devices/device=ios-router-01/sync-from'
url_resource = 'tailf-ncs:devices/device=ios-router-01/check-sync'
method='post'
headers = {
    "Content-Type": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Accept": "application/yang-data+xml"
}

payload = None
req = requests.request(
    method=method,
    url=url+url_resource,
    headers=headers,
    data=payload
)

print(req.status_code, req.reason, req.text)
