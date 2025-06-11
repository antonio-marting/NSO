import ncs

''' This script CREATE AAA USER for authentication '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    print('------ LIST OF AAA USERS in NSO ------')
    for user in root.aaa__aaa.authentication.users.user:
        print('username:', user.name)
        print('    uid:', user.uid)
        print('    gid:', user.gid)
        print('    homedir:', user.homedir)
        print('    ssh_keydir:', user.ssh_keydir)