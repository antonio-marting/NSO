import ncs

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device[device_name].config

    device.username.create('antonio')
    device.username['antonio'].password.type = '0'
    device.username['antonio'].password.secret = 'antonio'
    device.username['antonio'].privilege = 15
    
    t.apply()

    for entry in device.username:
        print(entry.name)
