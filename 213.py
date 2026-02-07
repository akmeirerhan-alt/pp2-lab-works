n=int(input())

if n<=1:
    print("No")
else:
    for i in range(2,n):
        if n%i==0:#prime number can only divided by itself and 1 
            print("No")
            break
    else:
        print("Yes")