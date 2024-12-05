input_file = open('input3.txt', 'r')
input = input_file.read()

chars = list(input)

new_list = []

temp_digits = ""

# Iterate through the list of characters
for char in chars:
    if char.isdigit():
        temp_digits += char
    else:
        if temp_digits:
            new_list.append(temp_digits)  
            temp_digits = "" 
        new_list.append(char)  

if temp_digits:
    new_list.append(temp_digits)
    

result1 = 0
for i in range(len(new_list)):
    if new_list[i] == "m" and new_list[i+1] == "u" and new_list[i+2] == "l" and new_list[i+3] == "(" and (new_list[i+4]).isdigit() and new_list[i+5] == "," and (new_list[i+6]).isdigit() and new_list[i+7] == ")":
        result1 += (int(new_list[i+4])*int(new_list[i+6]))

print(f"First answer: {result1}")


####################
active = True
result2 = 0

for i in range(len(new_list)):
    if new_list[i] == "d" and new_list[i+1] == "o" and new_list[i+2] == "(" and new_list[i+3] == ")":
        active = True
    if new_list[i] == "d" and new_list[i+1] == "o" and new_list[i+2] == "n" and new_list[i+3] == "'" and new_list[i+4] == "t" and new_list[i+5] == "(" and new_list[i+6] == ")":
        active = False
    if active and new_list[i] == "m" and new_list[i+1] == "u" and new_list[i+2] == "l" and new_list[i+3] == "(" and (new_list[i+4]).isdigit() and new_list[i+5] == "," and (new_list[i+6]).isdigit() and new_list[i+7] == ")":
        result2 += (int(new_list[i+4])*int(new_list[i+6]))


print(f"Second answer: {result2}")