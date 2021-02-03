str = input("")
list1= []
list2= []
for i in str:
    if i.isdigit() == True:
        list2.append(int(i))
    if i.isalpha() == True:
        list1.append(i.upper())
print(list2[0:])
for i in list1:
    print(i)
#string.isdigit():检测字符串string是否全由数字组成
#string.isalpha():检测字符串string是否全由字母组成
