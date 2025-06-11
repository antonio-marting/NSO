import ncs

''' This script CREATE NACM RULE-LIST and SHOW config for NACM RULE-LIST'''

    # El usuario para el que se crea la NACM debe existir previamente
    # si no existe crearlo ejecutando el script:
    # 'NCS_CONFIG_AAA_USER_CREATE_NEW.py'

with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
  
    print('------ Asign AAA USER to NACM Groups ------')
    root.nacm__nacm.groups.group['ncsantonio'].user_name.create('antonio')
    print('   >>> Done asigning AAA USER to NACM Groups...')
    
    print('------ ADD / MODIFY RULE-LIST ------')
    root.nacm__nacm.rule_list.create('antonio')
    root.nacm__nacm.rule_list['antonio'].group.create('ncsantonio')
    root.nacm__nacm.rule_list['antonio'].rule.create('any-access')
    root.nacm__nacm.rule_list['antonio'].rule['any-access'].action = 'permit'
    root.nacm__nacm.rule_list['antonio'].tacm__cmdrule.create('any-command')
    root.nacm__nacm.rule_list['antonio'].tacm__cmdrule['any-command'].action = 'permit'
    print('   >>> Done adding / modifying RULE-LIST...')

    t.apply()
    print('------ Commiting changes ------')

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
