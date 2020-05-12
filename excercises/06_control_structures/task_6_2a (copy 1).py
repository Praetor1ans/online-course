# -*- coding: utf-8 -*-
import sys
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#input_ip = input('Запросить у пользователя ввод IP-сети: ')
#ipadd_str = input_ip.split('.')
#~ ipadd = []
#~ i = 0
#~ for idx in ipadd_str:
	#~ i = i + 1
	#~ ipadd.append(int(idx))
	
#~ print(i)

#~ if i != 4:
	#~ print ('Неправильный IP-адрес')
#~ elif ipadd[0] >= 1 and ipadd[0] <=223:
	#~ print ('unicast')
#~ elif  ipadd[0] >= 224 and ipadd[0] <= 239:
	#~ print ('multicast')
#~ elif ipadd[0] == 255 and ipadd[1] == 255 and ipadd[2] == 255 and ipadd[3] == 255:
	#~ print ('local broadcast')
#~ elif ipadd[0] == 0 and ipadd[1] == 0 and ipadd[2] == 0 and ipadd[3] == 0:
	#~ print ('unassigned')
#~ else:
	#~ print ('unused')


input_ip = input('Запросить у пользователя ввод IP-сети: ')
ipadd_str = input_ip.split('.')
ipadd = []

if isdigit(ipadd):
	for idx in [0, 1, 2, 3]:
		ipadd.append(int(ipadd_str[idx]))
			
	if ipadd[0] > 255 and ipadd[1] > 255 and ipadd[2] > 255 and ipadd[3] > 255:
		print ('Неправильный IP-адрес')
	elif ipadd[0] < 0 and ipadd[1] < 0 and ipadd[2] < 0 and ipadd[3] <= 0:
		print ('Неправильный IP-адрес')
	elif ipadd[0] >= 1 and ipadd[0] <=223:
		print ('unicast')
	elif  ipadd[0] >= 224 and ipadd[0] <= 239:
		print ('multicast')
	elif ipadd[0] == 255 and ipadd[1] == 255 and ipadd[2] == 255 and ipadd[3] == 255:
		print ('local broadcast')
	elif ipadd[0] == 0 and ipadd[1] == 0 and ipadd[2] == 0 and ipadd[3] == 0:
		print ('unassigned')
else:
	print ('Неверные данные')



