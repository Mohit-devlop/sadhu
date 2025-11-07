l1=[10,30,50,40,20]
l2=[10,60,50,40,70]

common=[]
for i in l1:
    if i in l2:
        common.append(i)

not_common=[]
for i in l1+l2:
    if(i not in l1)or(i not in l2):
        not_common.append(i)

print("list one :",l1)
print("list two :",l2)
print("Common number  :",common)
print("NotCommon number   :",not_common)