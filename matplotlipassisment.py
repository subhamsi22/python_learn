import numpy as np
import matplotlib.pyplot as plt
print("python assiment ".center(100))

array  = [
    "1.My First Line Plot",
    "2.Favorite Fruits Bar Chart",
    "3.Multi-Plot Layout",
    "4.Customizing Styles",
]
for i in array:
    print(i)
 

choice_input =  int(input("Enter your choice : "))
while choice_input != 5:
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
    elif choice_input == 4:
        print("4. Customizing Styles")
    else:
        print("Invalid choice")
    choice_input =  int(input("Enter your choice : "))
    