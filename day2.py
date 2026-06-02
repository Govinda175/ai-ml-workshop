course_A = {"Alice","bob","diana","charle"}
course_B = {"Charlie","dianal","eve","frank"}
print("course A student:" , course_A)
print("course B student:" , course_B)

print("\n student in both courses:",course_A & course_B)
print("student in either course:",course_A | course_B)
print("only in course A:",course_A-course_B)
print("only in one course :",course_A^course_B)

scores_with_douplicates = [85,92,85,78,92,95,85]
unique_scores= list(set(scores_with_douplicates))
print("\norigin scores:",scores_with_douplicates)
print("unique scores:",unique_scores)


student = {
    "name":"alice",
    "age":20,
    "scores":[85,92,78],
    "Hobbies":"footbaal",
    "department":"Computer Science",
    "is_active":True
}
print("Student Dictionary:")
print(student)

print("\nStudent name:", student['name'])
print("Student age:", student['age'])
print("Student scores:", student['scores'])
print("Student hobbies:", student['age'])
print("Average  score :",sum(student['scores'])/len(student['scores']))

# Update dictionary
student["grade"] = "A"
student["age"] = 21

print("\nAfter update:")
print(student)

alice_score = student['scores'][0]
print("First score:", alice_score)





# Grade Calculator

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [95, 85, 75, 65, 55]

for score in test_scores:
    grade = get_grade(score)
    print("Score:", score, "-> Grade:", grade)

