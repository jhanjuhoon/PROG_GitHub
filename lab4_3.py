name = str(input("Name: "))
job = str(input("Job: "))
level = int(input("Level"))
hp = int(input("HP"))
txt = "MY CHARACTER"
print(f"{txt:=^60}")
print(f"Name:{name:<8} | Job:{job:<8} | Level:{level:<3} | HP:{hp:<6}")
print("="*60)