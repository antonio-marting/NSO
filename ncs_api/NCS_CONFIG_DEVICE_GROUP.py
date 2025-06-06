import ncs

''' Script for create one or several device-group in NSO '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    root.ncs__devices.ncs__device_group.create('IOS_XE')
    root.ncs__devices.ncs__device_group['IOS_XE']
    root.ncs__devices.ncs__device_group['IOS_XE'].device_name.create('EDC1')
    root.ncs__devices.ncs__device_group['IOS_XE'].device_name.create('EDC2')

    root.ncs__devices.ncs__device_group.create('IOS_XR')
    root.ncs__devices.ncs__device_group['IOS_XR']
    root.ncs__devices.ncs__device_group['IOS_XR'].device_name.create('EDC1')
    root.ncs__devices.ncs__device_group['IOS_XR'].device_name.create('EDC2')
    
    t.apply()
    print('Successfuly Created devices-group with member devices')

    ''' Listing all device groups and their members '''

    print('Listing all device groups and their members:')
    for dv_grp in root.ncs__devices.ncs__device_group:
        print('Group name: ', dv_grp.name)
        for member in dv_grp.member:
            print('   > ', member)

        
