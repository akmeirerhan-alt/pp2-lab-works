n=int(input())
names=[]
cnt=0
for i in range(n):
    name=input()
    names.append(name)

uniquename=set(names)
print(len(uniquename))