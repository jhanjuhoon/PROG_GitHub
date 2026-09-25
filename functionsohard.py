
def calcurate_score(quiz: float, exam: float, bonus: float):
    return ((quiz + exam) / 2 )+ bonus


def print_score(quiz, exam, bonus):
    final_score = calcurate_score(quiz, exam, bonus)
    print(f"Final score : {final_score:.2f}")

    if final_score >= 50:
        print("Result : Pass")
    else:
        print("Result : Fail")

print_score(78.0, 86.0 , 4.0)