from matplotlib import pyplot as plt

# input = list(range(1,1000))
# output = [x**2 for x in input]
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.scatter(input,output,c=output,cmap=plt.cm.Blues, s=10)
# ax.set_title('Scatter Plot', fontsize=24)
# ax.set_xlabel('X', fontsize= 14)
# ax.set_ylabel('Y', fontsize = 14)
# ax.axis([0,1001,0,1100000])
# ax.tick_params(axis='both', labelsize=12)
#
# plt.savefig('squares_plt.png', bbox_inches = 'tight')

x_value = [x for x in range(5000)]
y_value = [x**3 for x in x_value]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c='red', s= 10)
ax.set_title("Cubic Plot", fontsize=24)
ax.set_xlabel('value', fontsize=10)
ax.set_ylabel('cubic value', fontsize=10)
ax.tick_params(axis='both', labelsize=12)
ax.axis([1,5001,1,130000000000]) # define axis boundry
plt.savefig('cubic_plt.png',bbox_inches='tight')

plt.show()
