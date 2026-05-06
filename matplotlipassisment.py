import numpy as np
import matplotlib.pyplot as plt
print("python assiment ".center(100))

array  = [
    "1.My First Line Plot",
    "2.Favorite Fruits Bar Chart",
    "3.Multi-Plot Layout",
    "4.Customizing Styles",
    "5.The Personal Budget Bar Chart",
    "6.Temperature Analysis with Matplotlib",
]
for i in array:
    print(i)
 

choice_input =  int(input("Enter your choice : "))
while choice_input != 8:
    if choice_input == 1:
        print("1. My First Line Plot")

        days = np.array([1,2,3,4,5])
        height  = np.array([2,4,8,14,20])
        plt.plot(days,height)
        plt.plot(days,height,"o")
        plt.title("Plant Growth Over Time")
        plt.xlabel("days")
        plt.ylabel("height")
        plt.show()
        
    elif choice_input == 2:
        print("2. Favorite Fruits Bar Chart")

        fruit = np.array(["apple","banana","cherry","dates"])
        vote = np.array([10,15,7,12])
        col = np.array(["orange"])
        plt.bar(fruit,vote,color=col)           
        plt.title("Favorite Fruits")
        plt.grid(axis="y")
        plt.xlabel("fruits")
        plt.ylabel("votes")
        plt.show()

    elif choice_input == 3:
        print("3. Multi-Plot Layout")
        data1 =  np.arange(1,6)
        data2 = np.arange(6,11)
        plt.xlabel("marks")
        plt.subplot(1,2,1)
        plt.plot(data1,data2,"o")
        plt.ylabel("year")
        plt.subplot(1,2,2)
        plt.plot(data2,data1,"o")
        plt.tight_layout()
        plt.show()
    elif choice_input == 4:
        print("4. Customizing Styles")
        print("i use option 1 slide hear")
        days = np.array([1,2,3,4,5])
        height  = np.array([2,4,8,14,20])
        plt.plot(days,height)
        plt.plot(days,height,"--")
        plt.title("Plant Growth Over Time")
        plt.xlabel("days")
        plt.ylabel("height")
        plt.legend()
        plt.savefig("plt.png")
        plt.show()
    elif choice_input == 5:
        print("5. Monthly Expense Breakdown")
        data={
       "rent":1200,
       "food":450,
       "utilities":200,
       "transport":150,
       "entertainment":300
    } 
        thing = list(data.keys())
        money =list(data.values())


        plt.bar(thing,money)
        plt.title("monthly expense breakdown")
        plt.xlabel("----categories-----")
        plt.ylabel("----amount(usd)-----")
        plt.show()
    elif choice_input ==6:
        
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

 
    
    choice_input =  int(input("Enter your choice : "))
    