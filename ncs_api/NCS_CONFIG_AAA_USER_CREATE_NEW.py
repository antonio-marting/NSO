import ncs

''' This script CREATE AAA USER for authentication and lists all AAA users '''

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    print('------ Creating AAA USER for authentication ------')
    root.aaa__aaa.authentication.users.user.create('antonio')
    root.aaa__aaa.authentication.users.user['antonio'].uid = 1001
    root.aaa__aaa.authentication.users.user['antonio'].gid = 1001
    root.aaa__aaa.authentication.users.user['antonio'].password = '$6$XpKvpg57D6argms.$fyiNDHUrp.CbEoVvpQWLAdTzmYjyKNo2CqEXdhOeLXtPEfwz066koXFS6O/9YT4jZuVrFq/kPmnyWc.N1LavL.'
    root.aaa__aaa.authentication.users.user['antonio'].ssh_keydir = '/var/ncs/homes/antonio/.ssh'
    root.aaa__aaa.authentication.users.user['antonio'].homedir = '/var/ncs/homes/antonio/'
    print('   >>> Done creating AAA USER for authentication...')

    t.apply()
    print('------ Commiting changes ------')
    
    print('------ LIST OF AAA USERS in NSO ------')
    for user in root.aaa__aaa.authentication.users.user:
        print('username:', user.name)
        print('    uid:', user.uid)
        print('    gid:', user.gid)
        print('    homedir:', user.homedir)
        print('    ssh_keydir:', user.ssh_keydir)
