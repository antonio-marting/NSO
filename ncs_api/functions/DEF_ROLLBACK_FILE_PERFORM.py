import ncs

''' This function perform Rollback to a change with a especific fixed-number,
    must pass the change fixed-number to run the rollback.
'''

def run_rollback_file(change_nbr):
    with ncs.maapi.single_read_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)

        rollback_apply_params = root.rollback__rollback_files.rollback__apply_rollback_file.get_input()
        rollback_apply_params.fixed_number = change_nbr
        rollback_apply_params.comment = f'Comment Maapi APPLY_ROLBACK_FILES {rollback_apply_params.fixed_number}'
        rollback_apply_params.label = f'Label Maapi APPLY_ROLBACK_FILES {rollback_apply_params.fixed_number}'  


        apply_rollback = root.rollback__rollback_files.rollback__apply_rollback_file(rollback_apply_params)
        print(f'Rollback change # {rollback_apply_params.fixed_number} .... Done...!!!')
        print(apply_rollback.ncs_rollback__cli.local_node.data)

run_rollback_file(10169)