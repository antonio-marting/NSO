import ncs

''' This script list the Rollback changes availables in NSO'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    rollback_listing = root.rollback__rollback_files.file
    
    for roll_file in rollback_listing:
        if roll_file.label or roll_file.comment != None:
            print('{0:10} | change# {1:7} | id: {2:3} | Label: {3:40} | Comment: {4:40}'.format(roll_file.name, roll_file.fixed_number, roll_file.id, roll_file.label, roll_file.comment))        
        else:
            print('{0:10} | change# {1:7} | id: {2:3} | Label: {3:40} | Comment: {4:40}'.format(roll_file.name, roll_file.fixed_number, roll_file.id, 'None', 'None'))