import ncs

#device_name = 'ios-router-01'
device_name = 'EDC2'
#device_name = 'xr-router-03'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    device = root.devices.device[device_name].config

    #del device.interface.Loopback['44']
    #t.apply()

    ''' To Create a new Loopback and configure'''
    device.interface.Loopback.create('44')
    device.interface.Loopback['44'].ip.address.primary.address = "44.44.44.44"
    device.interface.Loopback['44'].ip.address.primary.mask = "255.255.255.255"
    device.interface.Loopback['44'].description = "created by NSC.MAAPI Python script"
    
    ''' Commit the changes in no-networking Mode '''
    commit_params = ncs.maapi.CommitParams()
    commit_params.no_networking()
    commit = t.apply_params(True, commit_params)
    
    print("Commiting NSO NO-NetWorking ... ")
    print(commit, 'Changes Committed Successfully as no-networking')
    
