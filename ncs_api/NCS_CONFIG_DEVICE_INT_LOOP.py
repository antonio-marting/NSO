import ncs

''' Diferentes acciones de configuracion para unicamente interfaces de tipo Loopback'''

#device_name = 'ios-router-01'
device_name = 'EDC1'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device[device_name].config

    ''' To Create a new Loopback and configure'''
    device.interface.Loopback.create('44')
    device.interface.Loopback['44'].ip.address.primary.address="44.44.44.44"
    device.interface.Loopback['44'].ip.address.primary.mask="255.255.255.255"
    
    t.apply()
    
    ''' To Modifiy Config to Loopback interface'''
    device.interface.Loopback['44'].ip.address.primary.address="33.33.33.33"
    device.interface.Loopback['44'].ip.address.primary.mask="255.255.255.255"
    
    t.apply()

    ''' To delete a Loopback interface'''
    del device.interface.Loopback['44']

    t.apply()

    ''' To Get All the Loopback interfaces and some config, in this case IP and MASK'''
    for entry in device.interface['Loopback']:
        print('Loopback', entry.name)
        print(entry.ip.address.primary.address + ' / ' + entry.ip.address.primary.mask)

