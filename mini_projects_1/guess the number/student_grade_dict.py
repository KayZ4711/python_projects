# Create a dictionary that will let you add a student and their grade 
# You will need a while loop to complete the task

student_grades = {}

off = False

while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grades[name] = grade 
    print("Student added sucessfully!")
    print(student_grades)
    add_another = input("Would you like to add another student? Y or N: ").lower()
    if add_another == "y":
        pass
    else:
        off = True