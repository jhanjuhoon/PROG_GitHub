slices = int(input("Pizza slice: "))
box = slices//8

remainder = slices % 8

print(f"full pizza boxes:{box} ")
print(f"remainder slices:{remainder} ")