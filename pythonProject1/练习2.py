profit = int(input("Please print your profit:"))
bonus = 0
qujian = [100000,100000,200000,200000,400000]
rate = [0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(qujian)):
    if profit <= qujian[i]:
        bonus += profit * rate[i]
        profit = 0
        break
    else:
        bonus += qujian[i]*rate[i]
        profit -= qujian[i]
    bonus += profit * rate[-1]

print(bonus)