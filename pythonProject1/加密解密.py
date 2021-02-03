def zip(x):
    n = x.split()
    s = 0
    for i in range(len(n)):
        n[i] = int(n[i]) + 5
        s += n[i]
    s = str(s % 10)
    n = s.split()
    n[0], n[3] = n[3], n[0]
    n[1], n[2] = n[2], n[1]
    for i in range(len(n)):
        print(n[i],end='')

zip("1234")