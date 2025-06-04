import ncs, _ncs

''' This script lists the rollbacks available in the NCS system.'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    rollbacks = _ncs.maapi.list_rollbacks(t.maapi.msock, 100)
    
    for rollback in rollbacks:
        print(f'--------- ROLLBACK {rollback.nr} -------------')
        print(rollback)
        
        print('Comment:', rollback.comment)
        print('Label:', rollback.label)
        print('user: ', rollback.creator)
        print('method: ', rollback.via)
        print('Fixed-number: ', rollback.fixed_nr)
        print('date: ', rollback.datestr)
        
            
    
