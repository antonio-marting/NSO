import ncs

''' This function create new device, fetch ssh-key and syn-from. To execute this script:
    You must pass the next vars:

    name, ipv4, authgroup, description, , device_type <cli|netconf>, device_group
'''

def new_device(name, ip, auth, desc, dev_type, dev_grp):
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            with m.start_write_trans() as t:
                root = ncs.maagic.get_root(t)
                device = root.devices.device

                device.create(name)
                device[name].ncs__address = ip
                device[name].ncs__authgroup = auth
                device[name].ncs__description = desc

                if dev_type == 'cli':
                    device[name].ncs__device_type.cli.ned_id = 'cisco-ios-cli-6.109:cisco-ios-cli-6.109'
                if dev_type == 'netconf':
                    device[name].ncs__device_type.netconf.ned_id = 'cisco-iosxr-nc-25.1:cisco-iosxr-nc-25.1'

                device[name].ncs__state.admin_state = 'unlocked'
                root.ncs__devices.ncs__device_group[dev_grp].device_name.create(name)

                print(f'Committing the device configuration for {name}...')
                t.apply()
                print("Committed")

            with m.start_read_trans() as t:      
                root = ncs.maagic.get_root(t)
                device = root.devices.device            

                print('Fetching SSH keys...')
                dev_fetch = device[name].ssh.fetch_host_keys()
                print(f'    Result: {dev_fetch.result}')

                print('Syncing configuration...')
                dev_sync = device[name].sync_from()
                print(f'    Result: {dev_sync.result} {dev_sync.info}')

                print('NEW device Info: ')
                print(root.devices.device[name].name)
                print('    IPv4: >', root.devices.device[name].address)
                print('    Auth_grp: >', root.devices.device[name].authgroup)
                for dvc_grp in root.devices.device['IOS-XR-02-NC'].device_group:
                    print('    Device_grp: >', dvc_grp)
                if root.devices.device[name].device_type.ne_type == 'netconf':
                    print('    NED type: >', root.devices.device[name].device_type.ne_type)
                    print('    NED ID: >', root.devices.device[name].device_type.netconf.ned_id)
                if root.devices.device[name].device_type.ne_type == 'cli':
                    print('    NED type: >', root.devices.device[name].device_type.ne_type)
                    print('    NED ID: >', root.devices.device[name].device_type.cli.ned_id)
                print('    Platform: >', root.devices.device[name].platform.name)
                print('    Platform model: >', root.devices.device[name].platform.model)
                print('    Platform verson: >', root.devices.device[name].platform.version)
                print('    Platform S/N: >', root.devices.device[name].platform.serial_number)
                print('    Alarms: >', root.devices.device[name].al__alarm_summary.criticals)
new_device('DEF_DEV_01', '192.168.2.217', 'cisco-ios-xr', 'DEF_DEV_01', 'netconf', 'IOS_XR')