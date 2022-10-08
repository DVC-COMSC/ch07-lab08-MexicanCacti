# ******************************
# Make your Code
# ******************************
index = 0
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
insertion_value = int(input())

for i in range(len(numbers)):
    if numbers[i] < insertion_value:
        index = i + 1
    if numbers[i] > insertion_value:
        break

numbers.insert(index,insertion_value)
print(numbers)