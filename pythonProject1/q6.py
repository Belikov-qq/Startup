import math
D = input()
d = D.split(',')
C = 50 ; H = 30
q = []
for i in d:
    Q = math.sqrt((2*C*int(i))/H)
    q.append(int(Q))
print(*(x for x in q),sep=',')