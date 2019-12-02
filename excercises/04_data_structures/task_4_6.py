# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

data = ospf_route.split()  
ospf_keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

d = {key: ospf_keys[0] for key in data[0]} 


2 способ

data = ospf_route.split() 

template = ''' 
    ...: Protocol:             {}  
    ...: Prefix:               {} 
    ...: AD/Metric:            {} 
    ...: Next-hop:             {} 
    ...: Last update:          {} 
    ...: Outbound Interface:   {} 
    ...: '''             
    
print(template.format('OSPF', data[1], data[2][1:-1], data[4][:-1], data[5][:-1], data[6]))      
