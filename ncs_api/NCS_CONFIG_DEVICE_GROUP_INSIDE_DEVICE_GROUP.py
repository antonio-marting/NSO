import ncs

''' Script for create device-group inside other device-group in NSO and listing all device-groups and their members '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    root.ncs__devices.ncs__device_group.create('NSO_ALL')
    root.ncs__devices.ncs__device_group['NSO_ALL'].device_group.create('IOS_XE')
    root.ncs__devices.ncs__device_group['NSO_ALL'].device_group.create('IOS_XR')

    t.apply()


    print('Successfuly Created devices-group inside device-device-group')

    ''' Listing all device-groups and their members '''

    print('Listing all device-groups and their members:')
    
    for dv_grp in root.ncs__devices.ncs__device_group:
        if dv_grp.name == 'NSO_ALL':
            print('Group name: ', dv_grp.name)
            for dvg in dv_grp.device_group:
                print('   device_group > ', dvg)
        else:
            print('Group name: ', dv_grp.name)    
            for member in dv_grp.member:
                print('  device > ', member)
 
