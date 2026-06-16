students=[
    {"name": "tanisha",
      "age": 20,
     "grade": 85},
     {"name": "sara",
      "age": 22,
     "grade": 90}
]
def add_student():
    name=input("enter student name:")
    age=int(input("enter student age:"))
    grade=int(input("enter student grade:"))
   
    student= {"name": name,
             "age": age,
             "grade": grade }
    students.append(student)
    print("student added successfully!")

def display_students():
    for student in students:
        print(student["name"], "-", student["age"],
               "years old, Grade:",
                 student["grade"])
    if len(students)==0:
        print("no students to display")

def  search_student():
    name=input("enter student name to search:")
    for student in students:
        if student["name"].lower()==name.lower():
            print("\nStudent found:")
            print("name:", student["name"])
            print("age:", student["age"])
            print("grade:", student["grade"])
            return
    print("student not found")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        display_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        print("goodbye!")
        break
    else:
        print("invalid choice, please try again.")