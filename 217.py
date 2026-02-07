n = int(input())# input number of phone numbers
contact = []# list to store all phone numbers

for i in range(n):
    contact.append(input())#read each number and add it to the list

counted = []#phone numbers that have already counted
tnum = 0#number of phone numbers that appear exactly 3 times

for i in range(n):#outer loop : choose one phone number to count
    if contact[i] in counted:
        continue #if this number was already counted skip to avoid countiing again

    cnt = 0 
    for j in range(n): #inner loop:scan the whole list 
        if contact[i] == contact[j]:
            cnt += 1

    if cnt == 3:
        tnum += 1

    counted.append(contact[i])#mark this number as counted

print(tnum)

