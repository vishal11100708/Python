a=str(input("enter string: "))
b=str(input("enter single char: "))
count=0
for i in a:
    if i in b:
        count+=1
print(count)
