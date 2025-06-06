import ncs

''' Script for create device-group with members inside other device-group in NSO and listing all device-groups and their members '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    ''' Creating child device-groups with device members'''
    root.ncs__devices.ncs__device_group.create('IOS_XE')
    root.ncs__devices.ncs__device_group['IOS_XE']
    root.ncs__devices.ncs__device_group['IOS_XE'].device_name.create('EDC1')
    root.ncs__devices.ncs__device_group['IOS_XE'].device_name.create('EDC2')

    root.ncs__devices.ncs__device_group.create('IOS_XR')
    root.ncs__devices.ncs__device_group['IOS_XR']
    root.ncs__devices.ncs__device_group['IOS_XR'].device_name.create('EDC1')
    root.ncs__devices.ncs__device_group['IOS_XR'].device_name.create('EDC2')

    ''' Creating parent device-group with child device-groups inside it '''
    root.ncs__devices.ncs__device_group.create('NSO_ALL')
    root.ncs__devices.ncs__device_group['NSO_ALL'].device_group.create('IOS_XE')
    root.ncs__devices.ncs__device_group['NSO_ALL'].device_group.create('IOS_XR')

    t.apply()

    print('Successfuly Created devices-group estructure with members inside other device-groups')

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
 
