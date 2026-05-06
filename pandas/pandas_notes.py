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
# df =  pd.DataFrame(data)
# print(df)
# print(data['name']) # this is use for print the only data in an object form


# a series is use to know the data type in the diconory like in array 

f =  pd.Series(["subham singh","sanju singh","akash singh"])
# print(f)
data  = {
    "name":["subham singh","sanju singh","akash singh"],
    "age": [24,25,26]
}
g = pd.DataFrame(data)
h = pd.Series(data)
# print(h)



#reading the csv file using pandas
dataa = "D:/download/python assiment/python_learn/annual-enterprise-survey-2024-financial-year-provisional.csv"
s =  pd.read_csv(dataa)
# print(s.head()) # use to print the first 5 rows or colum
# print(s.tail())# use to print the last 5 from data frame
# print(s.info()) # provide the basic informatin like datatypes coloumn names and etc 
# print(s.describe()) # use to show the overall describe information 


data  = {
    "name":["subham singh","sanju singh","akash singh"],
    "age":[24,25,26]

}
df =  pd.DataFrame(data)
s = df.loc[1] #this is use the label indexing
ss =  df.iloc[1] #use for indexing
# print(ss)

result  =  df[df["age"]>24]
# print(result)
# now make a new rowin data frame
df["salary"]  =["2k","3k","4k"]
# print(df)
# df.rename(columns={"name":"A",
#                    "age":"B",
#                    "salary":"C"
# } ,inplace=True)

# d = df.reindex([0,1,2,3,4])# this is use to reindexing the values 

print(d)