import ncs

''' This script SHOW the NACM RULE-LIST for all users.'''

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)

    ''' To See the rule-list defined on NSO'''
    print('-----------NACM USERS AND GROUPS -----------')
    for group in root.nacm__nacm.groups.group:
        print('Grupo: ', group.name)
        for user in group.user_name:            
            print('     User: ', user)
    
    print('-----------NACM RULE-LIST -----------')
    for entry in root.nacm__nacm.nacm__rule_list:
        print('rule-list for user:', entry.name)
        for rule in entry.rule:
            print('    rule:', rule.name)
            print('          module_name :  ', rule.module_name)
            print('          path:  ', rule.path)
            print('          access_operation:  ', rule.access_operations)
            print('          action:  ', rule.action)
        for cmd_rule in entry.tacm__cmdrule:
            print('    cmdrule:', cmd_rule.name)
            print('          command:', cmd_rule.command)
            print('          action:', cmd_rule.action)
