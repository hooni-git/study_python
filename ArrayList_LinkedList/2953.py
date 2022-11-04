all_num = [list(map(int, input().split())) for _ in range(5)]

add = 0;
participant = []

for i in range(5):
    for j in range(4):
        add = add + all_num[i][j]
    participant.append(add)
    add = 0

big = participant[0]
big_index = 0

for k in range(5):
    if big < participant[k]:
        big = participant[k]
        big_index = k

print(big_index+1, big)