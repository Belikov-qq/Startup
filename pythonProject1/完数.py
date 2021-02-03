n = int(input())
for i in range(3,n+1):
    s = 0
    for x in range(1,i):
        if i % x == 0:
            s += x
    if i == s:
        print(i)