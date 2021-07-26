from random import *
from time import *
from sys import argv
lisst = ['!','@','#','$','%','^','&','*','+','=',';','/','\\','|','[','>','<','0','1','9','5']

try:
    script, lines = argv
    lines = int(lines)
except:
    lines = 40

while True:
    for matrix in range(lines):
        print(choice(lisst), end = '')
    print('')
    sleep(0.1)
