#coding=utf-8

# Достаёт значения из вложенного словаря по указанному пути.

def dictionary_search(dictionary, path, sep=None):
    path_list = [i for i in path.split(sep)]
    dict_local = dictionary
    try:
        for j in path_list:
            for i in dict_local:
                try:
                    if type(i) == type(j):
                        if i == j:
                            dict_local = dict_local[i]
                    elif i == tuple(j.replace('(', '').replace(')', '').split(',')):
                        if i == tuple(j.replace('(', '').replace(')', '').split(',')):
                            dict_local = dict_local[i]
                    elif i == int(float(j)):
                        if i == int(float(j)):
                            dict_local = dict_local[i]
                    elif i == float(j):
                        if i == float(j):
                            dict_local = dict_local[i]
                except:
                    continue
        if type(dict_local) == dict_local:
            print('Неподходящие ключ словаря. Работает только с str, float, int и tuple с str-значениями.')
            return None
    except:
        raise ValueError('Неподходящие ключ словаря. Работает только с str, float, int.')
    return dict_local


dictionary = {1:"Влад", 2:{2.2: "Андрей", 2.4: "Дима"}}
test = dictionary_search(dictionary, "2-2.2", "-")
print(test) # Выведет "Андрей"