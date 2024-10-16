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
for item in students:
    print (f'Name: {item["name"]} \nHomework: {item["homework"]} \nQuizzes: {item["quizzes"]} \nTests: {item["tests"]}')

def average(lists):
    return float((sum(lists))/len(lists))

def get_average(stu):
    homework = average(stu['homework']) ; quizzes= average(stu['quizzes']) ; tests = average(stu['tests'])
    return (homework * 0.1) + (quizzes* 0.3) + (tests*0.6)

llooo=(get_average(lloyd))
print(llooo)