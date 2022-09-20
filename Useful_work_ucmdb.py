p = None

"----------------------Передача словаря значений между функциями----------------------------"
# def _createCCIpAddress(ip, num, OSHVResult, description=None, ca_global_id=None, ca_model=None, ca_node_os_name=None,
#                        ca_name=None, ca_serial=None, ca_sm_id=None, ca_node_os_vendor=None, ca_primary_dns_name=None,
#                        ca_device_type=None, ca_firmware=None, ca_rack=None, site=None, ca_vendor=None,
#                        ca_bucket=None, ca_config=None, ca_datacenter=None, ca_dcroom=None,
#                        ca_interface=None, ca_location=None, ca_ids=None):
#     print(ca_device_type)
#     print(ca_bucket)
#     print(ca_interface)
#     print(ca_config)
#     print(ca_location)
#
#
# def incomingDataProcessing(ip, num, OSHVResult, **fufufu):
#     _createCCIpAddress(ip, num, OSHVResult, **fufufu)
#
#
# ca_device_type = '1'
# ca_bucket = '2'
# ca_config = '3'
# ca_interface = '4'
# ca_location = '5'
#
# incomingDataProcessing('IP', 'NUM', "OSH", ca_device_type=ca_device_type, ca_bucket=ca_bucket,
#                        ca_config=ca_config, ca_interface=ca_interface, ca_location=ca_location)



"----------------------Пример лаконичной работы с циклом и функциями------------------------"
# tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
# for t, n, q in tasks:
#     t(n, q)



"----------------------Подсчет маски----------------------------"
# Из 255.255.255.0 >>> 24
# # №1
# def number_of_set_bits(x):
#     x -= (x >> 1) & 0x55555555
#     x = ((x >> 2) & 0x33333333) + (x & 0x33333333)
#     x = ((x >> 4) + x) & 0x0f0f0f0f
#     x += x >> 8
#     x += x >> 16
#     return x & 0x0000003f
#
# # №2
# def number_of_set_bits(x):
#     n = 0
#     while x:
#         n += x & 1
#         x = x >> 1
#     return n


"----------------------Функция наполнения КЕ----------------------------"
# # Функция наполнения КЕ - "installed_software"
# def setting_attr(instSoftOSH, soft_attr):
#     name = soft_attr.get('Name')
#     value = soft_attr.get('Value')
#
#     if value == '' or name == 'Global_id':
#         return instSoftOSH
#
#     # Получаем тип атрибута из XML
#     attr_type = soft_attr.get('Type').split('.')[-1]
#
#     # Добавление атрибутов
#     if attr_type == 'String':
#         instSoftOSH.setStringAttribute(name, value)
#     elif attr_type == 'Integer':
#         value = value.replace(',', '')
#         instSoftOSH.setIntegerAttribute(name, int(value))
#     elif attr_type == 'Boolean':
#         if value == 'True':
#             value = True
#             instSoftOSH.setBoolAttribute(name, value)
#         else:
#             value = False
#             instSoftOSH.setBoolAttribute(name, value)
#     elif attr_type == 'Date':
#         instSoftOSH.setDateAttribute(name, value)
#     elif attr_type == 'StringList':
#         # setListAttribute or addAttributeToList but first want java list to input, second need already exist list?
#         instSoftOSH.setListAttribute(name, [value])
#     return instSoftOSH





"-----------Функция порционной отправки данных в ucmdb-------------"
# def sendObjectsIntoUcmdb(Framework, OSHVResult):
#     for i in range(0, OSHVResult.size(), 15000):
#         limit = i + 15000
#         if limit >= OSHVResult.size():
#             limit = OSHVResult.size()
#
#         vector = OSHVResult.getSubVector(i, limit)
#         Framework.sendObjects(vector)
#         Framework.flushObjects()
#         vector.clear()

"----------------------Обработка ошибок----------------------------"
# if output.find('is not recognized') != -1:
#     errormsg = "NMAP is not installed on Probe machine, or please check the nmap location is configured correctly."
#     logger.error(errormsg)
#     raise ValueError, errormsg


"-------------------Действия с resultVector------------------------"
# for j in resultVector:
#     root_class = j.getAttributeAll()
#     ci_name = j.getAttribute('name')
#
#     if ci_name != None:
#         ci_name = j.getAttribute('name').getStringValue()
#         ci_name = str(ci_name) + '_vlad'
#     j.setStringAttribute('name', ci_name)

"Размер"
# resultsVector.size()

"-----------------------Скачивание файлов--------------------------"
# downloadFileStatus = client.downloadFile("C:\\UCMDB\\DataFlowProbe\\runtime\\temp\\test.xml", "/tmp/test.xml", True)
# putFileStatus = client.putFile("C:\\UCMDB\\DataFlowProbe\\runtime\\temp\\range.xml", "/opt/UCMDB/UCMDBServer/conf/discovery/customer_1")
# logger.debug(downloadFileStatus)
# logger.debug(putFileStatus)

"-----------Получить список атрибутов всех связанных КЕ-----------"
# interfaces = Framework.getTriggerCIDataAsList('mac_address')
# interfacesList = []
# for interface in interfaces:
#     interfacesList.append(interface)

"------------------Работа с файлами (изменение)-------------------"
# import re
#
# with open('C:\\Users\\CUSTOM_USER\\Desktop\\range.xml', 'r') as f:
#     old_data = f.read()
#
# pattern = r'\<attribute name="domain_protocollist" type="as400protocol.+(<attribute name="name")'
# result = re.finditer(pattern, old_data)
# for i in result:
#     s = i.group(0)
#
# new_data = old_data.replace(s, '')
#
# with open('C:\\Users\\CUSTOM_USER\\Desktop\\range.xml', 'w') as f:
#     f.write(new_data)

"-------------------------Создание клиента----------------------"
"http"
# http_client = DefaultHttpClient()
# http_context = BasicHttpContext()
# http_context.setAttribute(HttpClientContext.COOKIE_STORE, BasicCookieStore())

# user = 'nickname'
# passwd = 'password'
# jmx_authorization(ucmdb_url, http_client, http_context, user, passwd)
#
# # Подключение
# def jmx_authorization(url, http_client, http_context, user, passwd):
#     url_sc = url + '/jmx-console/j_security_check'
#     payload = {
#         'j_username': user,
#         'j_password': passwd,
#         'submit': 'Login'
#     }
#     rest_requests.post(url_sc, verify=False, data=payload, http_client=http_client, http_context=http_context)
#     return

"credentials"
# credentials = Framework.getAvailableProtocols('ssh')
# for cred_id in credentials:
#     client = Framework.createClient(cred_id)

"Что-то уже не помню"
# from com.hp.ucmdb.discovery.library.clients import ClientsConsts
# from shellutils import ShellFactory
#
# client = Framework.createClient(ClientsConsts.LOCAL_SHELL_PROTOCOL_NAME)
# shell = ShellFactory().createShell(client)

"Работа с клиентом. Функция. Описание внутри"
# from java.util import Properties
# from com.hp.ucmdb.discovery.common import CollectorsConstants
#
# def create_client(framework, ip):
#     """
#     функция создаёт ssh подключение
#     возвращает эксзепляр ssh клиента, если найдеты credentials с указанным user_label
#     иначе возвращает None
#     """
#     credentials = netutils.getAvailableProtocols(framework, ClientsConsts.SSH_PROTOCOL_NAME, ip)
#     props = Properties()
#     props.setProperty(CollectorsConstants.DESTINATION_DATA_IP_ADDRESS, ip)
#
#     for cred_id in credentials:
#         user_label = framework.getProtocolProperty(cred_id, CollectorsConstants.PROTOCOL_ATTRIBUTE_USER_LABEL, '')
#         if user_label == "ucmdb_server":
#             client = framework.createClient(cred_id, props)
#             return client
#     return None

"------------------------Работа с CMD--------------------------"
# client.executeCmd('ss -t4n state listening')

"-------------------------Редактирование строки (убираются ненужные символы по индексу)----------------------"
# def replace_char_at_index(org_str, index, replacement):
#     new_str = org_str
#     if index < len(org_str):
#         new_str = org_str[0:index] + replacement + org_str[index + 1:]
#     return new_str
#
#
# def ip_address_debug_dot(string_ip):
#     list_of_indexes = []
#
#     for i in range(len(string_ip) - 1):
#         if string_ip[i] == "/" and string_ip[i + 1] == ".":
#             list_of_indexes.append(i + 1)
#
#     for i in range(len(list_of_indexes)):
#         if i != 0:
#             string_ip = replace_char_at_index(string_ip, list_of_indexes[i] - i, '')
#         else:
#             string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '')
#
#     return string_ip

# # Эта функция одноразовая (для одного "случая"). Пока не стал делать универсальной
# def ip_address_debug_bracket(string_ip):
#     list_of_indexes = []
#
#     for i in range(len(string_ip) - 1):
#         if (string_ip[i].isdigit() and string_ip[i + 1] == "(") or (string_ip[i].isdigit() and string_ip[i + 1] == ")"):
#             list_of_indexes.append(i + 1)
#
#     for i in range(len(list_of_indexes)):
#         if i != len(list_of_indexes)-1:
#             if i != 0:
#                 string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '/')
#             else:
#                 string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '/')
#         else:
#             string_ip = replace_char_at_index(string_ip, list_of_indexes[i], '')
#
#     return string_ip
