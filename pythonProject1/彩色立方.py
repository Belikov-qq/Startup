import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
# mpl.rcParams['axes.unicode_minus'] = False #
x_value = list(range(1,5001))
y_value = [x**3 for x in x_value]
plt.title('5000以内立方数',fontsize=20)
plt.xlabel('Value',fontsize=15)
plt.ylabel('立方数',fontsize=15)
plt.axis([0,6000,0,125000000000])
plt.tick_params(axis='both', labelsize=15)
plt.scatter(x_value, y_value, s=0.1, c=y_value, cmap=plt.cm.Reds)
plt.savefig('立方数.png')