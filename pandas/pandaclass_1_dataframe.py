# what is panda 
# a panda is a libery of python use for data analysis
# create a data frame
# a data frame is silar like a tabel in excel 
import pandas as pd
#  creat a data frame using a dictionry
data  = {
    "name":["subham singh","sanju singh","akash singh"],
    "age":[24,25,26]

}
df =  pd.DataFrame(data)
print(df)
# print(data['name']) # this is use for print the only data in an object form