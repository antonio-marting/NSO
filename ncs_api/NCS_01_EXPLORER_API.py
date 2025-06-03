import ncs

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    #for entry in root:
    #    print(entry)
    device = root.devices.device_group['ORPHAN'].location
    print(device.altitude)

    #for option in device:
    #    if option.name == 'NSO_ALL':
    #        for i in (option.location):
    #            print(i.latitude)
            
