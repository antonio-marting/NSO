import ncs

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    device = root.devices.device[device_name].config

    ''' To Create a new Loopback and configure'''
    device.interface.Loopback.create('44')
    device.interface.Loopback['44'].ip.address.primary.address = "44.44.44.44"
    device.interface.Loopback['44'].ip.address.primary.mask = "255.255.255.255"
    device.interface.Loopback['44'].description = "created by NSC.MAAPI Python script"

    ''' Commit the changes in Dry-Run Mode '''
    commit_params = ncs.maapi.CommitParams()
    commit_params.dry_run_cli()
    commit = t.apply_params(True, commit_params)
    
    print("Commiting Dry-Run NSO CLI Style: ")
    print(commit)
    print (commit.get("local-node"))


    print(''' Diferent options for .get() method ''')
    for entry in commit:
        print(f'Commit result: {entry}')