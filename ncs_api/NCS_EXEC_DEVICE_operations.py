import ncs

#device_name = 'ios-router-01'
#device_name = 'xr-router-03'
device_name = 'EDC2'

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device[device_name]
    
    sync_fr = device.sync_from().result
    print(f'Result sync-from for "{device_name}" ... {sync_fr}')

    chk_sync = device.check_sync().result
    print(f'Result check-sync for "{device_name}" ... {chk_sync}')

    ssh_fetch = device.ssh.fetch_host_keys().result
    print(f'Result ssh-fetch for "{device_name}" ... {ssh_fetch}') 

    ned_check = device.device_type.netconf
    if ned_check.ned_id == None:
        print(f'NED is type IOS')
        print(10 * '-', 'SHOW COMMANDS', 10 * '-')
        live_command = device.live_status.exec.show.get_input()
        live_command.args = ['ip int brie']
        live_command_output = device.live_status.exec.show(live_command).result
        print(f'Output for {device_name} info ...\n {live_command_output}')

        live_command = device.live_status.exec.show.get_input()
        live_command.args = ['interfaces description']
        live_command_output = device.live_status.exec.show(live_command).result
        print(f'Output for {device_name} info ...\n {live_command_output}')
        
        print(10 * '-', 'CONFIG COMMANDS', 10 * '-')
    else:
        print(f'The NED device for "{device_name}" is XR type and is NOT allowed to run live-status commands')