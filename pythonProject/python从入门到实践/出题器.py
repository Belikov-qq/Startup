import random
op = ['+','-','*','/']
while True:
    a = random.randint(0,99)
    b = random.randint(0,99)
    s = random.choice(op)
    print('请计算%d %s %d' % (a,s,b) + ' =')
    question = input('请输入答案：（输入exit退出）\n')
    if s == '+':
        res = a + b
    elif s == '-':
        res = a - b
    elif s == '*':
        res = a * b
    elif s == '/':
        res = a / b
    if question == str(res):
        print('回答正确！')
    elif question == 'exit':
        break
    else:
        print('回答错误，答案是' + str(res))
