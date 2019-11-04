import re

import yaml
import pytest
import task_19_2b
import sys
sys.path.append('..')

from common_functions import check_function_exists


correct_return_value = (
{'ip http server': 'config term\n'
                   'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                   'R1(config)#ip http server\n'
                   'R1(config)#',
 'logging buffered 20010': 'config term\n'
                           'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                           'R1(config)#logging buffered 20010\n'
                           'R1(config)#'},
{'i': 'config term\n'
      'Enter configuration commands, one per line.  End with CNTL/Z.\n'
      'R1(config)#i\n'
      '% Ambiguous command:  "i"\n'
      'R1(config)#',
 'logging': 'config term\n'
            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
            'R1(config)#logging\n'
            '% Incomplete command.\n'
            '\n'
            'R1(config)#',
 'logging 0255.255.1': 'config term\n'
                       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                       'R1(config)#logging 0255.255.1\n'
                       '                   ^\n'
                       "% Invalid input detected at '^' marker.\n"
                       '\n'
                       'R1(config)#'})


def test_functions_created():
    check_function_exists(task_19_2b, 'send_config_commands')


def test_function_return_value(capsys, first_router_from_devices_yaml):
    commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
    correct_commands = ['logging buffered 20010', 'ip http server']
    test_commands = commands_with_errors + correct_commands

    return_value = task_19_2b.send_config_commands(
        first_router_from_devices_yaml, test_commands, verbose=False)

    # проверяем возвращаемое значение
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple, "Функция должна возвращать кортеж"
    assert len(return_value) == 2 and all(type(item) == dict for item in return_value),\
            "Функция должна возвращать кортеж с двумя словарями"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert return_good.keys() == correct_good.keys() and \
            return_bad.keys() == correct_bad.keys(),\
            "Функция возвращает неправильное значение"

@pytest.mark.parametrize("error,command", [
    ('Invalid input detected', 'logging 0255.255.1'),
    ('Incomplete command', 'logging'),
    ('Ambiguous command', 'i')
])
def test_function_stdout(error, command, capsys, first_router_from_devices_yaml):
    return_value = task_19_2b.send_config_commands(
        first_router_from_devices_yaml, [command], verbose=False)

    # Проверяем вывод информации об ошибках в stdout
    # во входящих данных три команды с ошибками
    # при каждой ошибке, должна выводиться информация:
    # ошибка, IP устройства, команда
    # в тесте проверяется наличие этих полей
    out, err = capsys.readouterr()
    ip = first_router_from_devices_yaml['ip']
    assert error in out, "В сообщении об ошибке нет самой ошибки"
    assert command in out, "В сообщении об ошибке нет выполняемой команды"
    assert ip in out, "В сообщении об ошибке нет IP-адреса устройства"


