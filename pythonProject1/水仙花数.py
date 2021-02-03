a = list(input())
b = list(map(int, a))
for i in range(1,b[0]+1):
    for h in range(b[1]+1):
        for x in range(b[2]+1):
            A = i * 100 + h *10 + x
            if i ** 3 + h ** 3 + x ** 3 == A:
                print(A, end=' ')