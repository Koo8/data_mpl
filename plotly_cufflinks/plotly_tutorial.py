import matplotlib.pyplot as plt

# set style before anything else
plt.style.use('seaborn')

x_value= range(1,101)
y_value = [x**2 for x in x_value]
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=2, c=x_value,cmap=plt.cm.Blues, marker='x', alpha=0.75)
ax.set_title('Squares Chart')
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Squared Value', fontsize=14)
ax.tick_params(axis='x', labelsize=12, colors='red')
ax.axis([0,120,1,11000])
# list all styles from plt
styles = plt.style.available
print(styles)

plt.style.use('dark_background')
plt.show()





