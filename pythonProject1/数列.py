n = int(input())
a0 = -1
s = 0
if n %2 == 0:
    a0 = 0
for i in range(n+1):
    s += 1/(a0+2)
print(s)


def jishu(x):
    s = 0
    for i in range(1,2*x+2,2):
        s += 1/i
    return s

def oushu(x):
    s = 0
    for i in range(2,2*x+1,2):
        s += 1/i
    return s

n = int(input())
if n%2 == 0:
    s = oushu(n)
else:
    s = jishu(n)
