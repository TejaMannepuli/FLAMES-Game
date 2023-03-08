print("just for fun")
name1=input()
name2=input()
name1=name1.replace(" ","")
name2=name2.replace(" ","")
name1=list(name1)
name2=list(name2)
for i in name1:
    if i in name2:
        name1.remove(i)
        name2.remove(i)
len1=len(name1)+len(name2)
l=["friends","love","affection","marrige","enemy","sibling"]
while(len(l)>1):
    index=len1%(len(l)-1)
    if(index>0):
        right=l[index+1:]
        left=l[:index]
        l=right+left
    else:
        l=l[:len(l)-1]
print(l)
