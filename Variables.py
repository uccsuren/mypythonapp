n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
#comprehensive list => used dealing with huge data 
list2=[x for x in range(n) if x%2==1]
print(list2)


