import ncs

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices

    commit_params = ncs.maapi.CommitParams()

    commit_params


    '''
    commit_params = ncs.maapi.CommitParams()

    commit_params.dry_run_cli()
    commit = t.apply_params(True, commit_params)
    print("Commiting Dry-Run NSO CLI Style: ")
    print(commit)
    print (commit.get("local-node"))
    '''


