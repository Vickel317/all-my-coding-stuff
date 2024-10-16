lloyd = {
"name": "Lloyd",
"homework": [90.0,97.0,75.0,92.0],
"quizzes": [88.0,40.0,94.0],
"tests": [75.0,90.0]
}
alice = {
"name": "Alice",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
tyler = {
"name": "Tyler",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
for s in students:
    print(f"Name: {s['name']} \nHomework Score: {s['homework']} \nQuiz Score: {s['quizzes']} \n"
          f"Test Score: {s['tests']})\n")

def average(x):
    if isinstance(x,list):
        return float(sum(x)) / len(x)
    else: print("TypeError")
    
# print(average(tyler["homework"]))

def get_average(student):
    homework = average(student['homework']) ; quizzes = average(student['quizzes']) ; tests = average(student['tests'])
    return (homework * 0.1) + (quizzes * 0.3) + (tests * 0.6)

# print(get_average(tyler))

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: return "F"

# print(get_letter_grade(get_average(lloyd)))

def get_class_average(students):
    results=[]
    for s in students:
        results.append(get_average(s))
    return average(results)

for s in students:
    print(f"{s['name']}'s average is {get_average(s):.1f}, {get_letter_grade(get_average(s))}")
    print(" ")

print(f"Class average is {get_class_average(students):.1f}, {get_letter_grade(get_class_average(students))}")