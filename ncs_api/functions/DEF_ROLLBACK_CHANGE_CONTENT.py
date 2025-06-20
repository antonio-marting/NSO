import ncs

'''This script show the content of one especific ROLLBACK operation,
    you must pass the change number realive to fixed-number as integer 
'''

def rollback_content(change_nbr):
    with ncs.maapi.single_read_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)

        rollback_params = root.rollback_files.get_rollback_file.get_input()
        rollback_params.fixed_number = change_nbr

        show_rollback = root.rollback_files.get_rollback_file(rollback_params)
        print(f'Rollback File Content for {rollback_params.fixed_number}: \n {show_rollback.content}')

rollback_content(10169)










    



            

