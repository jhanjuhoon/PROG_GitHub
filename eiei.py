import random

grid = []

for i in range(3):
    row = []
    for j in range(3):
        num = random.randint(1, 100)
        row.append(num)
    grid.append(row)
print(grid)

