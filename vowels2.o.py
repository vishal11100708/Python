a=input("**Enter the string**:")
b=0
count=0
s=0
m=['A','E','I','O','U','a','e','i','o','u']
for i in a:
  if i in m:
    count+=1
  elif i.isalpha():
    s+=1
  else:
    b+=1
print("*others*:",b)
print("*vowels*:",count)  
print("*consonets*:",s)  
