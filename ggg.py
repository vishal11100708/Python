a=input()
b=input()
ch_a={}
ch_b={}
for i in a.lower():
    if  i in ch_a:
        ch_a[i]+=1
    else:
        ch_a[i]=1
for i in b.lower():
    if  i in ch_b:
        cha[i]+=1
    else:
        ch_b[i]=1
if ch_a==ch_b:
    print("anagram")
else:
    print("not")
        
        
