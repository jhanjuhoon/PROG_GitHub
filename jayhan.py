scores = [85, -1, 90, -1, 78, 12, 54, 66, 31, -1, 56, -1]

for i in range(len(scores)):
    if scores[i] == -1:
        continue
    print(f"Score is : {scores[i]}")
