# print("Hello World")
name = "Ram"
faculty = "computer science"
dob = "2004/02/23"
# string concatenation
print("hello,"+name+"!"+"your are a student of "+faculty+"and you date of birth is "+dob)
print(f"hello,{name}! your are a student of {faculty} and you date of birth is {dob}")
# check data types
age = 23
is_student= True
gpa = 3.4
print(f"type of  name:{type(name)}")
print(f"type of  name:{type(faculty)}")
print(f"type of  name:{type(dob)}")
print(f"type of  name:{type(age)}")
print(f"type of  name:{type(is_student)}")
print(f"type of  name:{type(gpa)}")


name,faculty,dob,age,is_student,gpa ="Hari","BCA","2004/02/23",23,True,3.56
print(f"")

x, y = 10, 20
print("Before swap:  x=",x,"y=" ,y)
print("After swap:  x=" ,x,"y=",y)

student_info = ["Charlie",21,88.0]
name,age,score = student_info
print("Unpacked",name,age,score)
name1,others,_= student_info
print("name:",name1)
print("other",others)




# creating list
student_name = ["Alice","bob","Diamon"]
student_scores=[85,92,78,95]
print(f"student name:",student_name)
print(f"student score:",student_scores)
print("\nfirst student:",student_name[0])
print("last student:",student_name[-1])
print("first three:",student_name[0:3])

print("students from insert 1 to end:",student_name[:])
print("even sceond student:",student_name[::2])

# list operations
student_name.append("Eve")
print("\n After adding eve:",student_name)
student_name.insert(1,"Frame")
print("After inserting Frenk:",student_name)
student_name.remove("Alice")
print("remove :",student_name)




passing_scores= [score for score in student_scores if score>=80]
print("\n passing score(>=80);",passing_scores)

print("Number of student:",len(student_name))
print("highest score:",max(student_name))
print("lowers score:",min(student_name))

