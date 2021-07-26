from random import randint
from time import *
from sys import argv
try:
    script, start, end, size = argv
    size = int(size)
    start = int(start)
    end = int(end)
except:
    size = 30
    start = 0
    end = 1
while True:
    for a in range(size):
        print(randint(start,end), end = ' ')
    sleep(0.2)
    print('')
