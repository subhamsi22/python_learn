#Ek string me sabse zyada repeat hone wala character find karo.
a = "subham singhh"

# yaha pe h reapeat horhaein 3 time 
#usko find krna h 
min_char = ""
max_count = 0
for i in a:
   count  = a.count(i)
if count > max_count:
    max_count = count
    max_char = i
print(max_char)
print(max_count)

