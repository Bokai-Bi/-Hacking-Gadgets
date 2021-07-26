from time import *
a = 6
up_or_down = 'down'
while True:
    if up_or_down == 'down':
        print(' ' * int(6 - a),'||','-' * a,'|||','-' * a,'||')
        a -= 1
        if a < 0:
            up_or_down = 'up'
            a = 0
        sleep(0.1)
    else:
        print(' ' * int(6 - a),'||','-' * a,'|||','-' * a,'||')
        a += 1
        if a > 6:
            up_or_down = 'down'
            a = 6
        sleep(0.1)
