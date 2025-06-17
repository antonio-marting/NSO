import ncs

with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    alarms = root.al__alarms
    
    print('---------------------------- ALARMS SUMMARY -------------------------')
    print('Warnings:', alarms.al__summary.al__warnings)
    print('Criticals:', alarms.al__summary.al__criticals)
    print('Indeterminates:', alarms.al__summary.al__indeterminates)
    print('Majors:', alarms.al__summary.al__majors)
    print('Minors:', alarms.al__summary.al__minors)
    

    print('---------------------------- ALARMS LIST ----------------------------------------------------')
    print('-' * 109)
    print('| {0:18} | {1:10} | {2:33} | {3:25} | {4:7} |'.format(' DEVICE ', 'SEVERITY', 'DATE', 'ISSUE', 'CLEARED'))
    print('-' * 109)
    for alarm in alarms.al__alarm_list.al__alarm:
        print('| {0:18} | {1:10} | {2:33} | {3:25} | {4:7} |'.format(
            alarm.device, str(alarm.last_perceived_severity), alarm.last_status_change, alarm.type, alarm.is_cleared))
    print(' -------- ALARM TEXT -------------')
    for alarm in alarms.al__alarm_list.al__alarm:
        print('% >', alarm.last_alarm_text)
