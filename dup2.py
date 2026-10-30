a=input("enter the string:")
count=0
for i in set(a):
     if a.count(i)>1:
       count+=1
       print(i)
print("the total reapiting charecter is",count)
