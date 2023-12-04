caloriesList = []
with open('input1') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        caloriesList.append(-1 if line == "" else int(line))

elves = []
cal = 0
for i in caloriesList:
    if i > -1:
        cal += i
    else:
        elves.append(cal)
        cal = 0

elves.sort()
print(elves[-1])
print(elves[-1] + elves[-2] + elves[-3])
