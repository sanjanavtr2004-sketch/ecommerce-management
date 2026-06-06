name = input("enter your name: ")
class_name = int(input("enter your class: "))
students =[]
if(class_name in range (1,11)):
    subjects = ["maths", "science", "social science", "hindi", "english"]
    for subject in subjects:
        marks = input(f"enter marks for {subject}: ")
        subjectdata = {
            "subject_name":subject,
            "subject_marks":marks,
            "student_name":name
        }
        students.append(subjectdata)
    print("you are in class"+str(class_name))
elif(class_name in range (11,13)):
    course = input("enter your course: ")
    if(course=="PCM"):
        subjects = ["maths", "physics", "chemistry", "hindi", "english"]
    elif(course=="PCB"):
        subjects = ["biology", "physics", "chemistry", "hindi", "english"]
    elif(course=="commerce"):
        subjects = ["accounts", "efm", "badm", "hindi", "english"]
    for subject in subjects:
        marks = input(f"enter marks for {subject}: ")
        subjectdata = {
            "subject_name":subject,
            "subject_marks":marks,
            "student_name":name
        }
        students.append(subjectdata)
        print("you are in upper class"+str(class_name))
else:
    print("you are in valid class")
    print(students)    






    