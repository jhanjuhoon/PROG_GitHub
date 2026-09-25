name = str(input("Employee name: "))
salary = float(input("Base monthly salary: "))
total_sales = float(input("Total monthly sales: "))

def first_function(total_sales: float, commission_rate: float = 0.05):
    return total_sales * commission_rate

lambda_function = lambda total_sales, sales_target = 50000.0: total_sales >= sales_target

def second_function(base_salary: float, commission: float, bonus: float):
    return base_salary + commission + bonus

def recursive_function(monthly_income: float, months: int):
    if months <= 0:
        return 0.0
    else:
        return monthly_income + recursive_function(monthly_income, months - 1)

def last_function(name, total_sales, commission, bonus, total_income, target_reached):
    print("Sales commission report \n")
    print(f"Employee: {name}")
    print(f"Total sales: {total_sales:.2f} THB")
    print(f"Commission: {commission:.2f} THB")
    print(f"Bonus: {bonus:.2f} THB")
    print(f"Total income: {total_income:.2f} THB")

    if target_reached == True:
        print("Sales target reached: Yes")
    else:
        print("Sales target reached: No")

commission = first_function(total_sales)
target_reached = lambda_function(total_sales)

if target_reached == True:
    bonus = 2000.0
else:
    bonus = 0.0

total_income = second_function(salary, commission, bonus)

last_function(name, total_sales, commission, bonus, total_income, target_reached)

