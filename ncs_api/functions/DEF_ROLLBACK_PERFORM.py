import ncs, _ncs

def run_rollback(commit_nmbr):
    rollback_success = False
    id_to_rollback = get_rollback_num(commit_nmbr)
    print('ID to Rollback:', id_to_rollback)
    
    with ncs.maapi.single_write_trans('admin', 'python') as t:
        _ncs.maapi.load_rollback_fixed(t.maapi.msock, t.th, id_to_rollback)
        print('Doing the rollback.....')
        t.apply()
        print(f'Rollback: {id_to_rollback} was SUCCESS...!!!')
        rollback_success = True
    
    return rollback_success

def get_rollback_num(commit_nmbr):
    with ncs.maapi.single_read_trans('admin', 'python') as t:
        rollbacks = _ncs.maapi.list_rollbacks(t.maapi.msock, 100)
        for rollback in rollbacks:
            if rollback.fixed_nr == commit_nmbr:
                return rollback.fixed_nr
    return -1

run_rollback(10162)