import ncs

''' This script creates an authgroup in NSO '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices

    device.authgroups.group.create('cisco-ios-nexus')
    device.authgroups.group['cisco-ios-nexus'].default_map.create()
    device.authgroups.group['cisco-ios-nexus'].default_map.remote_name = 'cisco'
    device.authgroups.group['cisco-ios-nexus'].default_map.remote_password = 'cisco'

    t.apply()

    ''' Listar todos los authgroups creados'''
    for entry in device.authgroups.group:
       print(entry.name)
