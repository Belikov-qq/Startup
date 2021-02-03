n = int(input())
a = {}
for i in range(1,n+1):
    a[i] = i * i
print(a)

ans = {i : i * i for i in range(1,n+1)}
print(ans)