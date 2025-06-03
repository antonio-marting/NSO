import ncs

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device['ios-router-01'].config.system.mtu
    #for option in device:
    #    print(option)

    print(device.size)
    #print(device.ios__cdp.run)
    #print(device.ios__cdp.holdtime)

        
        