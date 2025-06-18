import ncs

'''This script show the content of the especific ROLLBACK operation '''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    rollback_list = root.rollback__rollback_files.file

    rollback_params = root.rollback_files.get_rollback_file.get_input()
    rollback_params.fixed_number = 10163

    show_rollback = root.rollback_files.get_rollback_file(rollback_params)
    print(f'Rollback File Content for {rollback_params.fixed_number}: \n {show_rollback.content}')