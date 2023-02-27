import time
import re
import subprocess
import distutils.spawn
import win32com.client


# Вводная часть, описывающая принцип взаимодействия с программой
def description(num):
    if num == 1:
        print("###################################################################################")
        print('##################################### Привет! #####################################')
        print('# Пока что весь функционал программы направлен лишь на работу со скриптом:')
        print('# - Сброс конфига в начало инициализирующего периода;')
        print('# - Движение вперед относильно актуальной даты в скрипте (дени, месяцы, годы);')
        print('# - Актуализация крайней большей даты на сегодняшнюю дату;')
        print('# - После отработки автоматически копирует скрипт в буфер обмена и жмет alt+tab;')
        print('# - Программа зациклена, что позволяет легко использовать её многоразово;')
        print('# - Работает, как уже видно, через батник, который должен быть рядом со скриптом;')
        print('# - Батник нужен, чтобы можно было использовать консоль;')
        print('# - Для выхода: напиши "exit" вместо парамметра, либо используй "крестик";')
        print('# - Установить дату больше настояшей нельзя - выдаст ошибку/предупреждение;')
        print('# - Пока могут иногда возникать ошибки, но большую часть я постарался обработать;')
        print('# - Должен обрабатывать все типы скриптов. Если встретишь новый - пиши мне!;')
        print('# - Чтобы отключить описание: в скрипте замени значение description с 1 на 0;')
        print('# - Остальное будет потихоньку дорабатываться.')
        print('# ------------ По всем предложениям и багам обращаться к VTB70181029 -------------')
        print("###################################################################################")
        print('# Как работать с программой?')
        print("# ---------------------------------------------------------------------------------")
        print("# 1. Нужно сунуть скрипт, который сразу будет разложен на имеющиеся в нем даты;")
        print("# 2. Дальше просит ввести параметры в формате число+буква (15d):")
        print("#    * d - день")
        print("#    * w - месяц")
        print("#    * y - год")
        print("#    После чего большая дата будет соответсвенно увеличена, а меньшая = большей")
        print("#    Постарайся корректно вводить значения, тк я тут особо не делал проверок пока.")
        print("#")
        print("#    Также есть ещё два режима (вводить как параметр без цифры):")
        print("#    * l - актуализация крайней большей даты на сегодняшнюю дату")
        print("#    * i - установка инициализирующего периода (1899-01-01 и 1899-01-02)")
        print("###################################################################################")

# Актуальная системная дата
t = time.localtime()
current_time = str(time.strftime("%Y-%m-%d", t)) + "T00:00:00"

# Имитация нажатия клавиш (имитирует нажатие ALT+TAB после выполения алгоритма)
def keystroke_simulation():
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.SendKeys('%{TAB}')

# Проверка на актуальность даты
def date_check(date):
    if date.split('T')[0] > current_time.split('T')[0]:
        print("Нет-нет, братишка, дата не может быть больше настоящей. Если нужна последняя, то напиши 'l' ")
        return 0
    else:
        return 1

# Добавляет текст в буфер обмена (кросплатформенный вариант)
def addToClipBoard(text):
    if distutils.spawn.find_executable("xclip"):
        # for Linux
        subprocess.run(["xclip", "-i"], input=text.encode("utf8"))
    elif distutils.spawn.find_executable("xsel"):
        # for Linux
        subprocess.run(["xsel", "--input"], input=text.encode("utf8"))
    elif distutils.spawn.find_executable("clip"):
        # for Windows
        subprocess.run(["clip"], input=text.encode("utf8"))
    else:
        import pyperclip
        pyperclip.copy(text)

# Формирует новый конфиг
def create_new_script(text, old_min, old_max, min, max):
    return text.replace(old_max, max).replace(old_min, min)

# Переворачивает дату
def reverse_date(date):
    if "." in date:
        return "-".join(list(date.split('.').__reversed__()))
    if "-" in date:
        return ".".join(list(date.split('-').__reversed__()))

# Создает новые даты на основе переданных ей параметров
def move_the_date(C, T, max):
    date_min = None
    date_max = None
    if T == 'y':
        date_min = max
        date_max = None
        year = int(max.split('-')[0]) + int(C)
        date_max = f"{str(year)}-{max.split('-')[1]}-{max.split('-')[2]}"
    elif T == 'w':
        date_min = max
        date_max = None
        month = int(max.split('-')[1]) + int(C)
        year = int(max.split('-')[0]) + (int(month / 12) if month > 12 else 0)
        if month > 12:
            month = month - 12 * int(month / 12)
            if month == 0:
                month = 1
        date_max = f"{str(year)}-{str(0) + str(month) if month < 10 else str(month)}-{max.split('-')[2]}"
    elif T == 'd':
        date_min = max
        date_max = None
        year = int(max.split('-')[0])
        day = int(max.split('-')[2]) + int(C)
        month = int(max.split('-')[1]) + int(day / 28)
        if day >= 28:
            day = day - 28 * int(day / 28)
            if day == 0:
                day = 1
        if month > 12:
            year = int(max.split('-')[0]) + (int(month / 12) if month > 12 else 0)
            month = month - 12 * int(month / 12)
            if month == 0:
                month = 1
        date_max = f"{year}-{str(0) + str(month) if month < 10 else str(month)}-{str(0) + str(day) if day < 10 else str(day)}"
    else:
        print("Невервый параметр")
        return None
    return date_min + "T00:00:00", date_max + "T00:00:00"

# Управляющая функция формирования даты
def delta_change(f_date, s_date):
    if f_date == s_date:
        print('Ошибка: даты равны!')
        return None

    min_date_old = None
    max_date_old = None
    if f_date > s_date:
        min_date_old = s_date
        max_date_old = f_date
    else:
        min_date_old = f_date
        max_date_old = s_date

    if f_date != max_date_old or s_date != min_date_old:
        print('Ошибка: даты в обратном порядке! Нужна проверка.')
        return None
    print("###################################################################################")
    print(f"# max_date: {max_date_old}, min_date: {min_date_old}")
    print("# ---------------------------------------------------------------------------------")
    print("# Схема: число+буква ---> d - день, w - месяц, y - год | l - акт. дата, i - первич.")
    range = str(input("# Введи параметры: "))
    print("###################################################################################")

    if range == 'l':
        return max_date_old + "T00:00:00", current_time

    if range == 'i':
        return "1899-01-01" + "T00:00:00", "1899-01-02" + "T00:00:00"

    count = ''.join([i for i in range if i.isdigit()])
    type = ''.join([i for i in range if not i.isdigit()])
    return move_the_date(count, type, max_date_old)

description(1)
text_script = None
while text_script != 'exit':
    try:
        text_script = f"""{input("Дай сюда скрипт: ")}"""
        new_min_date, new_max_date, old_date_min, old_date_max, new_text_script = None, None, None, None, None

        # Получение ключевых дат с помощью регулярных выражений
        if "algos" in text_script:
            first_pattern_1 = r'"dataset_max_date_to"\W*\"(\S*)\"'  # Большая
            first_pattern_2 = r'"wf_dataset_max_date_to"\W*\"(\S*)\"'  # Меньшая
            old_date_max = [i.group(1) for i in re.finditer(first_pattern_1, text_script)][0]
            old_date_min = [i.group(1) for i in re.finditer(first_pattern_2, text_script)][0]
            new_min_date, new_max_date = delta_change(old_date_max.split('T')[0], old_date_min.split('T')[0])
            new_text_script = text_script.replace(old_date_max, new_max_date).replace(old_date_min, new_min_date)
            if date_check(new_max_date) != 1:
                continue
        elif "left_bound" and "right_bound" in text_script:
            second_pattern_1 = r'"left_bound"\D*"ods_wf_max_date_to"\W*\"(\S*)\"'  # Меньшая
            second_pattern_2 = r'"right_bound"\D*"ods_wf_max_date_to"\W*\"(\S*)\"'  # Большая
            old_date_min = [i.group(1) for i in re.finditer(second_pattern_1, text_script)][0]
            old_date_max = [i.group(1) for i in re.finditer(second_pattern_2, text_script)][0]
            new_min_date, new_max_date = delta_change(old_date_max.split('T')[0], old_date_min.split('T')[0])
            new_text_script = text_script.replace(old_date_max, new_max_date).replace(old_date_min, new_min_date)
            if date_check(new_max_date) != 1:
                continue
        elif "clause_dinamic" in text_script:
            third_pattern_1 = r'to_date\D*\'(\d{2}\.\d{2}\.\d{4})'
            result = [i.group(1) for i in re.finditer(third_pattern_1, text_script)]
            old_date_min, old_date_max = reverse_date(result[0]), reverse_date(result[1])
            new_min_date, new_max_date = delta_change(old_date_max.split('T')[0], old_date_min.split('T')[0])
            if date_check(new_max_date) != 1:
                continue
            new_min_date = reverse_date(new_min_date.split('T')[0])
            new_max_date = reverse_date(new_max_date.split('T')[0])
            new_text_script = text_script.replace(result[1], new_max_date).replace(result[0], new_min_date)
        else:
            if text_script != "exit":
                print("Не узнаю скрипт. Придется ручками)")
                print("Если хочешь выйти, то напиши: exit")
            continue

        print(f"# max_date: {new_max_date}, min_date: {new_min_date}.")
        print("###################################################################################")
        addToClipBoard(new_text_script)
        keystroke_simulation()
    except:
        print("Что-то пошло не так...")
        continue