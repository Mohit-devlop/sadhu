data=bytearray([10,20,30,40,50])

print("original array:")
for value in data:
    print(value,end=" ")
for i in range(len(data)):
    data[i]=data[i]+5

print("\nmodified array:")

for value in data:
     print(value,end=" ")

index=int(input("\n enter value of index(0-4):"))
print("\nvalue at index",index,"is:",data[index])








