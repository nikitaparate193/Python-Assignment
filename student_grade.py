dic = {}

while True:
    print("\n1. Add student\n2. Update grade\n3. Print all\n4. Exit")
    number = input("Enter number: ")
    
    if number == "1":
        name = input("Student Name: ")
        grade = input("Grade: ")
        dic[name] = grade
    elif number == "2":
        name = input("Student name update: ")
        if name in dic:
            dic[name] = input("New grade: ")
        else:
            print("Student name not found.")
    elif number == "3":
        for name, grade in dic.items():
            print(f"{name}: {grade}")
    elif number == "4":
        break
    else:
        print("invalid number!")