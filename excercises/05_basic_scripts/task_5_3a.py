# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

port_type = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: '	)

mode = port_type.count('trunk')

modes = [
['Enter VLAN number: '],
['Enter allowed VLANs: ']
]


vlan = input(' '.join(modes[mode]))



access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

templates = {'access': access_template, 'trunk': trunk_template}

port_type_final = templates.get(port_type)

print('interface {}'.format(interface))
print('\n'.join(port_type_final).format(vlan))
