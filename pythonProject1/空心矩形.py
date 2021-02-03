#coding:utf-8
from pip._vendor.distlib.compat import raw_input

rows = int(raw_input('输入行数： '))
column = int(raw_input('输入列数： '))
i = j = k = 1
print("空心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        if i != 0 and i != rows - 1:
            if k == 0 or k == rows - 1:
                print(" * "),
            else:
                 print("   "),
        else:
            print(" * "),
        k += 1
    i += 1
    print("\n")