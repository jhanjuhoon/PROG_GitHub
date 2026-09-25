numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even is : {even_count}")
print(f"Odd is : {odd_count}")
