#coding:utf-8
from pip._vendor.distlib.compat import raw_input

n = int(raw_input('请输入n：(n>=1) '))
up = int((n+1)/2)
down = int((n-1)/2)
for i in range(up):
    print(" "*(up-i) + "*"*(2*(i+1)-1))
for i in range(down):
    print(" "*(i+2) + "*"*(2*down-(2*(i+1)-1)))