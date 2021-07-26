from time import *
from random import *
class zhuangbi(object):
    def __init__(self, zb):
        self.zb = zb
    def printzb(self):
        print(self.zb, end = '')

a = zhuangbi('Initializing sequence')
b = zhuangbi('Getting default gateway')
c = zhuangbi('Port scanning')
d = zhuangbi('Checking for SQL injection')
e = zhuangbi('Infecting system folder')
f = zhuangbi('Launching a memory corruption')
g = zhuangbi('Changing host file')
h = zhuangbi('Hacking default DNS server')
i = zhuangbi('Opening webshell')
j = zhuangbi('Getting administrator privilage')
k = zhuangbi('Locking down users')
l = zhuangbi('Cracking MD5 encryption for admin password')
m = zhuangbi('Gathering random data')
n = zhuangbi('Analyzing firewall')
o = zhuangbi('Detecting hardware version')
p = zhuangbi('Trying to close port 80 & 443')
q = zhuangbi('Deleting logs')
r = zhuangbi('Opening proxy tunnel on port 1823')
s = zhuangbi('Uploading critical information')
t = zhuangbi('Scanning for leaked information')
u = zhuangbi('Forcing to close security system')
v = zhuangbi('Planting forkbomb')
w = zhuangbi('Deleting root account')
x = zhuangbi('Loading backup data')
y = zhuangbi('Shutting down network')
z = zhuangbi('Closing anti-virus system')
listt = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
suc = ['Successful', 'Failed']
while True:
    obj = choice(listt)
    obj.printzb()
    for a1 in range(randint(2,7)):
        print('.', end = '')
        sleep(0.4)
    b1 = choice(suc)
    if b1 == 'Successful':
        print(b1)
        print('')
    else:
        print(b1)
        print('Error code: ',randint(0,100))
        print('')
