
numbers = [
 [5, 10, 15],
 [20, 3, 7],
 [8, 12, 10],
 [30, 5, 2]
]

max_sum = max(sum(row) for row in numbers)

print(f"Max sum of row is : {max_sum}")

