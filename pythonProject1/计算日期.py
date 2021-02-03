from pip._vendor.distlib.compat import raw_input

n = raw_input().split()
c = 0
m = [31,28,31,30,31,30,31,31,30,31,30,31]
if int(n[0]) % 400 ==0 or ( int(n[0]) % 4 == 0 and int(n[0]) % 100 != 0):
    m[1] = 29
for i in range(int(n[1])-1):
    c += m[i]
c += int(n[2])
print(c)