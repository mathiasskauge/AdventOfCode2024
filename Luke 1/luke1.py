text_file = open('input1.txt', 'r')
text = text_file.readlines()

first = []
second = []
for i in range(len(text)):
    first.append(text[i].split()[0])
    second.append(text[i].split()[1])

first.sort()
second.sort()

sum = 0
for i in range(len(text)):
    sum += abs(int(second[i]) - int(first[i]))

print(f"First answer: {sum}")

#############

similarity = 0
for i in range(len(text)):
    cur = first[i]
    count = 0
    for i in range(len(text)):
        if second[i] == cur:
            count += 1
    similarity += int(cur) * count

print(f"Second answer: {similarity}")