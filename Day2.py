lines = []
with open('input2') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())

# A Rock, B Paper, C Scissors
# X Rock, Y Paper, Z Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# Ro = 65, Pp = 66, Sc = 67
# Ro = 88, Pp = 89, Sc = 90
myTotal = 0
for i in lines:
    opp = ord(i[0])
    me = ord(i[2])
    score = me - 87
    if me - opp == 21 or me - opp == 24:
        score += 6
    elif me - opp == 23:
        score += 3
    myTotal += score
    # print(i[0], i[2], score)

print(myTotal)

# X must lose, Y must draw, Z must win
myTotal = 0
for i in lines:
    me = 0
    opp = ord(i[0])
    result = ord(i[2])
    score = (result - 88) * 3
    if score == 0:
        me = ((opp - 64) + 2) % 3
        if me == 0:
            me = 3
    elif score == 3:
        me = opp - 64
    elif score == 6:
        me = ((opp - 64) + 1) % 3
        if me == 0:
            me = 3
    score += me
    myTotal += score
    # print(i[0], i[2], me, score)

print(myTotal)
