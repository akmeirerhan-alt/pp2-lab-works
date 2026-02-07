n=int(input())
my_dict={} #creating empty dictionary

for i in range(n):
    s,t=input().split() # inputing strings in one line
    if s not in my_dict: # if we don't have s key in dictionary
        my_dict[s]=int(t) #s key-value t
    else:
        my_dict[s]+=int(t) #if we have add their value together 
a=dict(sorted(my_dict.items())) #dictionary sorting with dict(), sorted(), items() function

for key, value in a.items(): #outputing dictionary element with items() and format
    print(f"{key} {value}")