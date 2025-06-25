import ncs

''' This script CREATE AAA USER for authentication and list the info for new created user.
    This functiooooooooon requiere to pass the next variables:

    - username -> username to create and userd for homedir/ssh_key
    - password -> password for this users
    - id       -> will be used to asign uid/gid

    Before to run this function you can take a look for all existing users/uid/gid running 
    the function list_users()
 '''

def create_user(username,password, id):    
    with ncs.maapi.single_write_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)
        user = root.aaa__aaa.authentication.users.user
        print('------ Creating AAA USER for authentication ------\n')
        user.create(username)
        user[username].uid = id
        user[username].gid = id
        user[username].password = password
        user[username].ssh_keydir = f'/var/ncs/homes/{username}/.ssh'
        user[username].homedir = f'/var/ncs/homes/{username}/'
        print(f'   >>> Done creating AAA USER "{username}" for authentication...\n ')

        print('New User Info: ')
        print('    username:', user[username].name)
        print('        uid:', user[username].uid)
        print('        gid:', user[username].gid)
        print('        password:', user[username].password)
        print('        ssh_keydir:', user[username].ssh_keydir)
        print('        homedir:', user[username].homedir)

        print('------ Commiting changes ------')
        t.apply()
        print('------ Commit Done! ------')
        

create_user('regla','regla', 1002)



















