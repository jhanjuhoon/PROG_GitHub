age = int(input("Enter your age: "))
if age < 0:
    print("You are not born yet")
else:
    day = input("Enter weekday or weekend: ")
    if day not in ["weekday", "weekend"]:
        print("Please enter only weekday or weekend")
        exit()
    if age <= 12:
        print("You are an Child")
        if day == "weekday":
            print("Your ticket is $6 on weekdays")
        elif day == "weekend":
            print("Your ticket is $8 on weekends")
        else:
            print("Please enter weekday or weekend")

    elif age <= 64:
        print("You are an Adult")
        if day == "weekday":
            print("Your ticket is $11 on weekdays")
        elif day == "weekend":
            print("Your ticket is $14 on weekends")
        else:
            print("Please enter weekday or weekend")
    else:
        print("You are an Elder")
        if day == "weekday":
            print("Your ticket is $8 on weekdays")
        elif day == "weekend":
            print("Your ticket is $10 on weekends")
        else:
            print("Please enter weekday or weekend")