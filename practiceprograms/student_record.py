students = {}

def add_student():

    roll = int(input("Enter Roll Number: "))

    # Check if roll number already exists
    if roll in students:
        print("Student with this Roll Number already exists.")
        return

    name = input("Enter Name: ").title()
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    marks = []

    print("Enter Marks of 5 Subjects")

    for i in range(5):
        mark = int(input(f"Subject {i+1}: "))

        while mark < 0 or mark > 100:
            print("Marks should be between 0 and 100.")
            mark = int(input(f"Subject {i+1}: "))

        marks.append(mark)

    students[roll] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("\nStudent Added Successfully!\n")

add_student()   

print(students)