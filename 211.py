n,l,r=map(int,input().split())
a=list(map(int,input().split()))
sub=a[l-1:r] # create a sublist that has elements from l-1 to r
sub.reverse() # reverse the elements
a[l-1:r]=sub # replace original elements with reversed one

print(*a)#unpacking 


