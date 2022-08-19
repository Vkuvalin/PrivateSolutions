p = None

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
