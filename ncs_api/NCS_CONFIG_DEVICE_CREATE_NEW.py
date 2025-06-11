import ncs

''' This script LIST all devices in NSO and shows their attributes.'''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    
    ''' Create device as NETCONF'''
    root.devices.device.create('IOS-XR-02-NC')
    root.devices.device['IOS-XR-02-NC'].ncs__address = '192.168.2.217'
    root.devices.device['IOS-XR-02-NC'].ncs__authgroup = 'cisco-ios-xr'
    root.devices.device['IOS-XR-02-NC'].ncs__description = 'IOS-XR-02-NC'
    root.devices.device['IOS-XR-02-NC'].ncs__device_type.netconf.ned_id = 'cisco-iosxr-nc-25.1:cisco-iosxr-nc-25.1'
    root.devices.device['IOS-XR-02-NC'].ncs__state.admin_state = 'unlocked'
    root.ncs__devices.ncs__device_group['IOS_XR'].device_name.create('IOS-XR-02-NC')

    ''' Create device as CLI'''
    root.devices.device.create('EDC3')
    root.devices.device['EDC3'].ncs__address = '192.168.2.217'
    root.devices.device['EDC3'].ncs__authgroup = 'cisco-ios-xe'
    root.devices.device['EDC3'].ncs__description = 'EDC3'
    root.devices.device['EDC3'].ncs__device_type.cli.ned_id = 'cisco-ios-cli-6.109:cisco-ios-cli-6.109'
    root.devices.device['EDC3'].ncs__state.admin_state = 'unlocked'
    root.ncs__devices.ncs__device_group['IOS_XE'].device_name.create('EDC3')

    t.apply()

    print(root.devices.device['IOS-XR-02-NC'].name)
    print('    IPv4: >', root.devices.device['IOS-XR-02-NC'].address)
    print('    Auth_grp: >', root.devices.device['IOS-XR-02-NC'].authgroup)
    for dvc_grp in root.devices.device['IOS-XR-02-NC'].device_group:
        print('    Device_grp: >', dvc_grp)
    if root.devices.device['IOS-XR-02-NC'].device_type.ne_type == 'netconf':
        print('    NED type: >', root.devices.device['IOS-XR-02-NC'].device_type.ne_type)
        print('    NED ID: >', root.devices.device['IOS-XR-02-NC'].device_type.netconf.ned_id)
    if root.devices.device['IOS-XR-02-NC'].device_type.ne_type == 'cli':
        print('    NED type: >', root.devices.device['IOS-XR-02-NC'].device_type.ne_type)
        print('    NED ID: >', root.devices.device['IOS-XR-02-NC'].device_type.cli.ned_id)
    print('    Platform: >', root.devices.device['IOS-XR-02-NC'].platform.name)
    print('    Platform model: >', root.devices.device['IOS-XR-02-NC'].platform.model)
    print('    Platform verson: >', root.devices.device['IOS-XR-02-NC'].platform.version)
    print('    Platform S/N: >', root.devices.device['IOS-XR-02-NC'].platform.serial_number)
    print('    Alarms: >', root.devices.device['IOS-XR-02-NC'].al__alarm_summary.criticals)