n = int(input())
ss = []

for i in range(2,n+1):
    c = 0
    for x in range(2,i-1):
        if i % x == 0:
            c = 1
    if c != 1:
        ss.append(i)

count = 0
counts = []
while n % 2 == 0:
    for h in range(4, n+1):
        for i in range(len(ss)):
            for x in range(i,len(ss)):
                if ss[i] + ss[x] == h:
                    if h in counts:
                        break
                    else:
                        count += 1
                        counts.append(h)
                        print("THE" + str(count) + "： " + str(h) + " = " + str(ss[i]) + " + " + str(ss[x]))
    break
a = input()