F1, F2 = 1, 1
n = int(input())
for i in range(n-2):
    F1, F2 = F2, F1+F2
    print(F2)
a = input()