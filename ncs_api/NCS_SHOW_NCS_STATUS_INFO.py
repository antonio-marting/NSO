import ncs

''' This script SHOW the NCS Version, NED installer and package version.'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    print('NCS Version:', root.tfnm__ncs_state.tfnm__version)
    print(f'NCS WebUI is: {root.tfnm__ncs_state.tfnm__webui.listen}') 
    for proto in root.tfnm__ncs_state.tfnm__webui.listen:
        print(f'      over protocol {proto}')
    print('NCS daemon Status:', root.tfnm__ncs_state.tfnm2__daemon_status)
    print('Patches DIR:', root.tfnm__ncs_state.tfnm__patches.tfnm__patches_directory)

    print('Internal CDB DataStore Info:')    
    for datastore in root.tfnm__ncs_state.tfnm__internal.tfnm__cdb.tfnm__datastore:
        print('Datastore Name:', datastore.name)
        print('     disk size:', datastore.disk_size)
        print('     ram size:', datastore.ram_size)
        print('     transaction id:', datastore.transaction_id)
    
    print('Internal CDB Client Info:')
    for client in root.tfnm__ncs_state.tfnm__internal.tfnm__cdb.tfnm__client:
        print(f'     Client name: {client.name}, tipo: {client.type}')
    
    print('Internal PACKAGES Info:')   
    for package in root.ncs__packages.ncs__package:
        print('     ', package.name, package.package_version, package.directory, package.oper_status.ncs__status, package.oper_status.ncs__error_info)


