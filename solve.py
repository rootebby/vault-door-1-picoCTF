from os import system,name
import numpy as np
from time import sleep


if name == 'nt':
    system("cls")
else:
    system("clear")


print("""
                 _    ____       _     _           
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/ 
                                                   
""")
sleep(2)
i=1
print("Dont forget to make your file !!!!")
print("Creating array with zeros")
arr = np.empty(32, dtype=object)
sleep(2)
filename = input("Enter your file name with extension (press enter for data.txt) : ")
if len(filename) == 0:
    filename = 'data.txt'
with open(filename,"r",encoding="UTF-8") as data:
    for line in data:
        start = line.index('(')
        stop = line.index(')')
        num = int(line[start+1:stop])
        dat = line[-6:-5:]
        print("On line {} , index determined as {} , letter determined as {}".format(i,num,dat))
        i+=1
        arr[num] = str(dat)
        sleep(0.05)

my_data = ''.join(i for i in arr)
print("FLAG DECODED !!!! :\t",my_data)
print("Ready to go  :   picoCTF{"+my_data+"}")
