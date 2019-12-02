# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

#Парсим command1 и делаем множество
com1split = command1.split() 
vlan1= set(com1split[-1].split(','))

#Парсим command2  и делаем множество
com2split = command2.split() 
vlan2= set(com2split[-1].split(','))

#Делаем из множества список пересечений между vlan1 и vlan2
result = list(sorted(vlan1 & vlan2))
