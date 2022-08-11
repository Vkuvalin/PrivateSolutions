import re
import logger


# Данное убрано за ненадобностью из основной функции.
# Словарь, в котором считается количество одинаковых ip
ip_addresses = dict()
def ipAddressesAddDict(list_ip_addresses):
    for i in list_ip_addresses:
        ip_addresses[i] = ip_addresses.get(i, 0) + 1
        if ip_addresses[i] > 1:
            print('Косяк')


def replace_char_at_index(org_str, index, replacement):
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str


def ip_address_debug_dot(string_ip):
    list_of_indexes = []

    for i in range(len(string_ip) - 1):
        if string_ip[i] == "/" and string_ip[i + 1] == ".":
            list_of_indexes.append(i + 1)

    for i in range(len(list_of_indexes)):
        if i != 0:
            string_ip = replace_char_at_index(string_ip, list_of_indexes[i] - i, '')
        else:
            string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '')

    return string_ip


# Эта функция одноразовая (для одного "случая"). Пока не стал делать универсальной
def ip_address_debug_bracket(string_ip):
    list_of_indexes = []

    for i in range(len(string_ip) - 1):
        if (string_ip[i].isdigit() and string_ip[i + 1] == "(") or (string_ip[i].isdigit() and string_ip[i + 1] == ")"):
            list_of_indexes.append(i + 1)

    for i in range(len(list_of_indexes)):
        if i != len(list_of_indexes)-1:
            if i != 0:
                string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '/')
            else:
                string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '/')
        else:
            string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '')

    return string_ip


def ipFormatting(first_ip_string):

    # Исправление ошибок заполнения по общему шаблону
    first_ip_string = ip_address_debug_dot(first_ip_string)

    list_ip = []
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    result = ' '.join([i.group(0) for i in re.finditer(pattern, first_ip_string)])

    if len(result.split(' ')) > 1:
        for i in result.split(' '):
            list_ip.append(i)
        return list_ip
    else:
        list_ip.append(result)

    ip_first_formate = first_ip_string[first_ip_string.find(result):]

    if len(result) != ip_first_formate and "-" in ip_first_formate and ip_first_formate[
        ip_first_formate.find('-') + 1].isdigit() and '/' not in ip_first_formate:
        num = ip_first_formate[ip_first_formate.find('-') + 1:]
        if len(num) <= 3:
            for i in range(int(list_ip[0].split('.')[-1]) + 1, int(num) + 1):
                result_2 = result.split('.')
                result_2[3] = str(i)
                list_ip.append('.'.join(result_2))

            return list_ip

    if '/' in first_ip_string:
        pattern_1 = r''
        for i in ip_first_formate:
            if i == "/":
                pattern_1 += '\/\d{1,3}'

        flag_range = True
        try:
            result_1 = [i.group(0) for i in re.finditer(pattern_1, first_ip_string)][0][1:].split('/')

            pattern_3 = r'\/\d{1,3}\-\d{1,3}'
            result_3 = [i.group(0) for i in re.finditer(pattern_3, first_ip_string)][0][1:].split('/') or None
            if result_3 and len(result_3) == len(result_1):
                pass
            else:
                flag_range = False

        except Exception as e:
            logger.debug(first_ip_string)
            logger.debug("WARNING-1: ", e)
            pass

        if len(result) != ip_first_formate and "-" in ip_first_formate and ip_first_formate[
            ip_first_formate.find('-') + 1].isdigit() and flag_range:
            list_nums = ip_first_formate[ip_first_formate.find('-') + 1:].split('/')

            for i in list_nums:
                if '-' in i:
                    list_range = i.split('-')

                    for j in range(int(list_range[0]), int(list_range[1]) + 1):
                        result_2 = result.split('.')
                        result_2[3] = str(j)
                        list_ip.append('.'.join(result_2))
                else:
                    for g in range(int(list_ip[0].split('.')[-1]) + 1, int(i) + 1):
                        result_2 = result.split('.')
                        result_2[3] = str(g)
                        list_ip.append('.'.join(result_2))

            return list_ip

        try:
            for i in result_1:
                result_2 = result.split('.')
                result_2[3] = i
                list_ip.append('.'.join(result_2))
        except Exception as e:
            logger.debug(first_ip_string)
            logger.debug("WARNING-2: ", e)
            pass

        try:
            if result_3 is not None:

                for res in result_3:
                    list_range = res.split('-')

                    for j in range(int(list_range[0]) + 1, int(list_range[1]) + 1):
                        result_2 = result.split('.')
                        result_2[3] = str(j)
                        list_ip.append('.'.join(result_2))
        except:
            pass

    if list_ip[0] == '':
        return None

    return list_ip


ip_list = None
if ";" in ip:
    ip_list = ip.split(";")

    # Форматирование каждого элемента
    for i in range(len(ip_list)):
        ip_list[i] = ip_list[i].replace(' ', '')

result = None
if ip_list:
    for ip in ip_list:
        result = ipFormatting(ip)
        if result is None:
            continue

        for clear_ip in result:
            _createCCIpAddressCI(clear_ip)          # Частная функция, для которой чистился ip_address

    if result is None:
        raise Exception("Bad ip addresses", ip_list)
else:
    ip_formatted = ip.replace(' ', '')
    result = ipFormatting(ip_formatted)

    if result is None:
        raise Exception("Bad ip address", ip_formatted)

    for clear_ip in result:
        _createCCIpAddressCI(clear_ip)              # Частная функция, для которой чистился ip_address
