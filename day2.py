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
