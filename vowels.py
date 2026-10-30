a=str(input("enter string:"))
count=0
m=['A','E','I','O','U','a','e','i','o','u']
for i in a:
    if i in m:
        count+=1
    print(count)
