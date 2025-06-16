import pandas as pd
import ncs
''' This function create a serie of new devices where the info is defined in a .CSV file.
    The CSV file will be defined with this estructure example:
        
        name;address;description;authgroup;dev_grp;ned;admin-state;vendor
        def_pd_xr_01;192.168.2.217;def_pd_xr_01;cisco-ios-xr;IOS_XR;netconf;unlocked;iosxr
        def_pd_xe_01;192.168.2.210;def_pd_xe_01;cisco-ios-xe;IOS_XE;cli;unlocked;iosxe

'''
def onboard_devices():
    
    # Opening .CSV file to read device info 
    df = pd.read_csv('/home/antonio/AutomationTools/docker/NSO/ncs_api/functions/device_list.csv', sep=';')
    
    # Open Mapaapi Session
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            for row in df.index:
                device_name = df.loc[row]['name']
                address = df.loc[row]['address']
                description = df.loc[row]['description']
                authgroup = df.loc[row]['authgroup']
                dev_grp = df.loc[row]['dev_grp']
                ned = df.loc[row]['ned']
                admin_state = df.loc[row]['admin-state']
                vendor = df.loc[row]['vendor']                              

                # Open writable Transaction for creating devices
                with m.start_write_trans() as t:
                    root = ncs.maagic.get_root(t)
                    device = root.devices.device
                    device.create(device_name)
                    device[device_name].ncs__address = address
                    device[device_name].ncs__authgroup = authgroup
                    device[device_name].ncs__description = description
                    
                    if vendor == 'iosxe':
                        device[device_name].ncs__device_type.cli.ned_id = 'cisco-ios-cli-6.109:cisco-ios-cli-6.109'
                    if vendor == 'iosxr':
                        device[device_name].ncs__device_type.netconf.ned_id = 'cisco-iosxr-nc-25.1:cisco-iosxr-nc-25.1'
                    
                    device[device_name].ncs__state.admin_state = admin_state
                    root.ncs__devices.ncs__device_group[dev_grp].device_name.create(device_name)
                    
                    print(f'Committing the device configuration for {device_name}...')
                    t.apply()
                    print("    Committed")

                # Open Read Transaction for syncing and fetching-key for each device
                with m.start_read_trans() as t:      
                    root = ncs.maagic.get_root(t)
                    device = root.devices.device            
                    print('    Fetching SSH keys...')
                    dev_fetch = device[device_name].ssh.fetch_host_keys()
                    print(f'        Result: {dev_fetch.result}')
                    print('    Syncing configuration...')
                    dev_sync = device[device_name].sync_from()
                    print(f'        Result: {dev_sync.result} {dev_sync.info}')

onboard_devices()