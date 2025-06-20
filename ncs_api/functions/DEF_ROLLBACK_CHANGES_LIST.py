import ncs

''' This function list the Rollback file info  change with a especific fixed-number
    giving info as:
    - change number: fixed-number and id
    - change date
    - label
    -comment
'''
def rollback_changes_list():
    with ncs.maapi.single_read_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)

        rollback_listing = root.rollback__rollback_files.file

        for roll_file in rollback_listing:
            if roll_file.label or roll_file.comment != None:
                print('change# {0:7} |  id: {1:3} |  date: {2:20} | Label: {3:40} | Comment: {4:40}'.format(roll_file.fixed_number, roll_file.id, roll_file.date, roll_file.label, roll_file.comment))      
            else:
                print('change# {0:7} |  id: {1:3} |  date: {2:20} | Label: {3:40} | Comment: {4:40}'.format(roll_file.fixed_number, roll_file.id, roll_file.date, 'None', 'None'))

rollback_changes_list()











    



            

