n = int(input())
arr = list(map(int, input().split()))

# Find the most frequent number
max_count = 0
most_freq = arr[0]

for num in arr:
    count = 0
    for x in arr:
        if x == num:
            count += 1
    # Update if this number has higher count, or same count but smaller number
    if count > max_count or (count == max_count and num < most_freq):
        max_count = count
        most_freq = num

print(most_freq)
