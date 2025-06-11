import ncs

''' This script LIST all devices in NSO and shows their attributes.'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device


    ''' Listar los devices en NSO y mostrar sus atributos '''
    for entry in device:
        print(entry.name)
        print('    IPv4: >', entry.address)
        print('    Auth_grp: >', entry.authgroup)
        for dvc_grp in entry.device_group:
            print('    Device_grp: >', dvc_grp)
        if entry.device_type.ne_type == 'netconf':
            print('    NED type: >', entry.device_type.ne_type)
            print('    NED ID: >', entry.device_type.netconf.ned_id)
        if entry.device_type.ne_type == 'cli':
            print('    NED type: >', entry.device_type.ne_type)
            print('    NED ID: >', entry.device_type.cli.ned_id)
        print('    Platform: >', entry.platform.name)
        print('    Platform model: >', entry.platform.model)
        print('    Platform verson: >', entry.platform.version)
        print('    Platform S/N: >', entry.platform.serial_number)
        print('    Alarms: >', entry.al__alarm_summary.criticals)
            