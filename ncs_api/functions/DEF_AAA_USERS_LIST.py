import ncs

''' This function LIST ALL AAA USER for authentication  '''

def list_users():
    with ncs.maapi.single_read_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)
        print('------ LIST OF AAA USERS in NSO ------')
        for user in root.aaa__aaa.authentication.users.user:
            print('username:', user.name)
            print('    uid:', user.uid)
            print('    gid:', user.gid)
            print('    homedir:', user.homedir)
            print('    ssh_keydir:', user.ssh_keydir)
                 
list_users()
  