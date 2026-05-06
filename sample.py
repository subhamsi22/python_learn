import matplotlib.pyplot as plt 

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 

low = [23,25,24,26,28,27,29]
high = [28,29,30,27,26,28,29]
plt.plot(days,low,color="blue",marker="o",label="low")
plt.plot(days,high,color="red",linestyle="--",marker="s",label="high")
plt.title("weekly temprature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()