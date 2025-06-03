import ncs

''' Esto vale para condfigurar y ver el estado de cualquier interface Ethernet, ya sea Fast, Giga, TenGiga, etc...'''

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device[device_name].config

    device.interface.GigabitEthernet['0/3'].ip.address.primary.address = "10.10.10.10"
    device.interface.GigabitEthernet['0/3'].ip.address.primary.mask = "255.255.255.0"
    device.interface.GigabitEthernet['0/3'].description = "Provisined with NCS.MAAPI"
    del device.interface.GigabitEthernet['0/3'].shutdown

    ''' para poner en shutdown la interface '''
    #device.interface.GigabitEthernet['0/3'].shutdown
    
    t.apply()
    
    ''' Ver el estado de todas las interfaces Ethernet configuradas en el dispositivo '''
    for entry in device.interface['GigabitEthernet']:
        print('Giga', entry.name)
        print(entry.ip.address.primary.address, ' / ' , entry.ip.address.primary.mask, ' / ', entry.description)
    
    ''' Ver el estado de una interface Ethernet en concreto '''
    device_g_0_0_ip = device.interface.GigabitEthernet['0/0'].ip.address.primary.address
    device_g_0_0_mask = device.interface.GigabitEthernet['0/0'].ip.address.primary.mask
    print(device_g_0_0_ip, '/', device_g_0_0_mask)


