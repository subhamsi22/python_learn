# a series is use to know the data type in the diconory like in array 
import pandas as pd
f =  pd.Series(["subham singh","sanju singh","akash singh"])
# print(f)
data  = {
    "name":["subham singh","sanju singh","akash singh"],
    "age": [24,25,26]
}
g = pd.DataFrame(data)
h = pd.Series(data)
print(h)