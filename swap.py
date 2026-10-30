a=input("Enter the string:")
for i in a:
    if i.islower():
      i=i.upper()
      print(i,end="")
    elif i.isupper():
      i=i.lower()
      print(i,end="")
    elif i.isdigit():
      print(i,end="")
    else:
      continue
