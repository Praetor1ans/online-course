# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ipadd = input('Запросить у пользователя ввод IP-сети: ')

ip_template = ''' 
    Network:
    {0:<8}  {1:<8}  {2:<8}  {3:<8} 
    {0:08b}  {1:08b}  {2:08b}  {3:08b} 
    
    Mask:
    {4:<8}  {5:<8}  {6:<8}  {7:<8} 
    {4:08b}  {5:08b}  {6:08b}  {7:08b}
    '''                                                                 
ip_str = ipadd.split('/')
ip_clear = ip_str[0].split('.')

a = int(ip_clear[0])
b = int(ip_clear[1])
c = int(ip_clear[2])
d = int(ip_clear[3])




limit = 2**32
wildmask = int(ip_str[1]) 
mask_clear = bin(limit - 2**wildmask)
finalmask = 32 - wildmask
lastmask = bin(limit - 2**finalmask)

q = int(lastmask[2:10],2)
w = int(lastmask[10:18],2)
e = int(lastmask[18:26],2)
r = int(lastmask[26:33],2)   

x = a & q
y = b & w
z = c & e
v = d & r



print(ip_template.format(x, y, z, v, q, w, e ,r))


