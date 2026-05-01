import numpy as np
import matplotlib.pyplot as plt


data={
       "rent":1200,
       "food":450,
       "utilities":200,
       "transport":150,
       "entertainment":300
} 
plt.bar(data)
plt.title("monthly expense breakdown")
plt.xlabel("----categories-----")
plt.ylabel("----amount(usd)-----")
plt.show()