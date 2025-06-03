import ncs

device_grp_name = 'XE-IOS'
#device_grp_name =  = 'XR-IOS'
#device_grp_name =  = 'NSO_ALL'

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device_grp = root.devices.device_group[device_grp_name]
    
    print(10 * '-', ' SYNC-FROM ', 10 * '-')
    sync_fr = device_grp.sync_from().sync_result
   
    for router in sync_fr:
        print(f' Resultado de device "{router.device}" sync-from is "{router.result}" \n---INFO:  {router.info}')
        
    print(10 * '-', ' CHECK- SYNC ', 10 * '-')
    chk_sync = device_grp.check_sync().sync_result
    
    for router in chk_sync:
        print(f' Resultado de device "{router.device}" check-sync is "{router.result}" \n---INFO:  {router.info}')
    
    print(10 * '-', ' FETCH-KEYS ', 10 * '-')

    ssh_fetch = device_grp.fetch_ssh_host_keys().fetch_result
    for router in ssh_fetch:
        print(f' Resultado de device "{router.device}" ssh-fetch is "{router.result}" \n---INFO:  {router.info}')

    print(10 * '-', ' LIVE-STATUS ', 10 * '-')
#
    #ned_check = device.device_type.netconf
    #if ned_check.ned_id == None:
    #    print(f'NED is type IOS')
    #    live_command = device.live_status.exec.show.get_input()
    #    live_command.args = ['version']
    #    live_command_output = device.live_status.exec.show(live_command).result
    #    print(f'Output for {device_name} info ...\n {live_command_output}')
    #else:
    #    print(f'The NED device for "{device_name}" is XR type and is NOT allowed to run live-status commands')