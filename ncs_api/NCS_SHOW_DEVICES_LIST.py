import ncs

''' This script LIST all devices in NSO .'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    devices = root.devices.device
    print('-' * 60)
    print('| {0:20} | {1:15} | {2:15} |'.format('DEVICE', 'IPv4 ADDRESS', 'AUTHGROUP'))
    print('-' * 60)
    for dev_data in devices:
        print('| {0:20} | {1:15} | {2:15} |'.format(dev_data.name, dev_data.address, dev_data.authgroup))
            