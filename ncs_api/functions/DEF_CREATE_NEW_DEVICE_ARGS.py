import argparse
import ncs
''' This function create new device, fetch ssh-key and syn-from. To execute this script:
    
    - new_device.py --name <name> --address <ip_address> --desc <description> --auth <authgroup> --nedtype <cli|netconf>
'''

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help="device name", required=True)
    parser.add_argument('--address', help="device address", required=True)
    parser.add_argument('--nedtype', help="cli or netconf", required=True)
    parser.add_argument('--desc', help="device description", default="MAAPI CREATED")
    parser.add_argument('--auth', help="device authgroup", default="default")
    return parser.parse_args()

def new_device(args):
    with ncs.maapi.Maapi() as m:
        with ncs.maapi.Session(m, 'admin', 'python'):
            with m.start_write_trans() as t:
                root = ncs.maagic.get_root(t)

                print("Setting device '%s' configuration..." % args.name)

                # Get a reference to the device list
                new_dev = root.devices.device

                device = new_dev.create(args.name)
                device.address = args.address
                device.description = args.desc
                device.authgroup = args.auth
                
                if args.nedtype == 'cli':
                    dev_type = device.device_type.cli
                    dev_type.ned_id = 'cisco-ios-cli-6.109'
                if args.nedtype == 'netconf':
                    dev_type = device.device_type.netconf
                    dev_type.ned_id = 'cisco-iosxr-nc-25.1'
                
                device.state.admin_state = 'unlocked'

                print('Committing the device configuration...')
                t.apply()
                print("Committed")

                # Clossing this transaction

            #
            # Continue in orignal trasaction to fetch-host-key and sync-from
            #
            root = ncs.maagic.get_root(m)
            device = root.devices.device[args.name]

            print("Fetching SSH keys...")
            output = device.ssh.fetch_host_keys()
            print("Result: %s" % output.result)

            print("Syncing configuration...")
            output = device.sync_from()
            print("Result: %s" % output.result)
            if not output.result:
                print("Error: %s" % output.info)


if __name__ == '__main__':
    new_device(parseArgs())