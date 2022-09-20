from subprocess import Popen
import sys
import threading
import os
import time


start = time.time()
end = None

list_ip = ['СПИСОК IP_ADDRESS']
names_files = list()
flag = False

def main_func():
    
    def read_list_ip():
        for ip in list_ip:
            yield ip

    ip = read_list_ip()

    def print_ip(arg):
        global flag
        global end
        while not flag:
            try:
                next_ip = next(arg)
                tmp_file_name = next_ip.replace('.', '').replace('_', '') + time.strftime("%H%M%S", time.gmtime(time.time())) + 'nmap.xml'
                names_files.append(tmp_file_name)
                process = subprocess.Popen(["powershell.exe", "nmap.exe -O -osscan-guess -sS -sV -p T:22,5985,5986,7738 --host-timeout 60s {} -oX {}".format(next_ip, tmp_file_name)], stdout=sys.stdout)
                process.communicate()
            except:
                flag = True
                
        if flag and end is None:
            end = time.time()
            timetaken = end - start

            fin = open("names_files.txt", "a")
            fin.write("Your program takes: {}".format(timetaken) + '\n')
            fin.write('\n' + ', '.join(names_files))
            fin.close()


    for i in range(39):
        t = threading.Thread(target=print_ip, args=(ip,))
        t.start()


t0 = threading.Thread(target=main_func)
t0.start()