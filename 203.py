n=int(input())
arr=input().split()#with split we can read strings in one line 
sum=0;
for i in range(n):
    sum+=int(arr[i])# turn string to integers and add them

print(sum)