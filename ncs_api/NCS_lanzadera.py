import ncs

device_name = 'ios-router-01'
#device_name = 'EDC1'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device[device_name].config

    #device.interface.Loopback['44'].delete()
    device.interface.GigabitEthernet['0'].ip.address.primary.address="10.10.10.10"
    device.interface.GigabitEthernet['0'].ip.address.primary.mask="255.255.255.0"
    device.interface.GigabitEthernet['0'].description="Provisined with NCS.MAAPI"
    #del device.interface.Loopback['44']
    t.apply()
        
    #for entry in device.interface.GigabitEthernet['0']:
    #    print(entry)
    #    #print(entry.ip.address.primary.address + ' / ' + entry.ip.address.primary.mask)

    for entry in device.interface['GigabitEthernet']:
        print('Giga', entry.name)
        print(entry.ip.address.primary.address, ' / ' , entry.ip.address.primary.mask)
