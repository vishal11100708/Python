a =input()
for i in a:
  r=0
  for j in a:
    if i==j:
      r+=1
  if r==1:
    print(i)
    break
        
