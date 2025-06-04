import ncs

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    device = root.devices.device[device_name].config

    del device.interface.Loopback['44']
    t.apply()
    print(f'Deleted Loopback 44 from device {device_name}')
