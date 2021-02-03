n = input().split()
for i in range(len(n)):
    a = list(n[i])
    a[0] = chr(ord(a[0]) - 32)
    for x in range(len(a)):
        print(a[x],end='')
    print(" ",end='')