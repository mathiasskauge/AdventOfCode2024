input_file = open('input2.txt', 'r')
input = input_file.readlines()

#Convert to lists of numbers
nums = [[int(num) for num in line.split()] for line in input]

def check_safety(row):
    safe = True
    for i in range(len(row)-1):
        if row[i] != row[i+1] and 3 >= abs(row[i] - row[i+1]) and (row == sorted(row) or row == sorted(row, reverse=True)):
            continue
        else:
            safe = False
    return safe

result1 = sum(1 for i in range(len(nums)) if check_safety(nums[i]))

print(f"First answer: {result1}")

##############################

result2 = 0
for i in range(len(nums)):
    if check_safety(nums[i]):
        result2 += 1
    else:
        for j in range(len(nums[i])):
            temp_list = nums[i].copy()
            temp_list.pop(j)
            if check_safety(temp_list):
                result2 += 1
                break

print(f"Second answer: {result2}")