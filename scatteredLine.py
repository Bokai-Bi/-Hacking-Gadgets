import random
import time
while True:
    a = random.randint(0,20)
    print(
    ' ' * (random.randint(20-a,20)),
    '/',
    '-' * (random.randint(a,2 * a)),
    '\\',
    sep = '',
    end = '\n' * random.randint(0,3)
    )
    time.sleep(0.1)
