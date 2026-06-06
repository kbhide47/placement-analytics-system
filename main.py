print("Placement Analytics System")

while True:
    print("\n1. Add Student")
    print("2. Add Company")
    print("3. Placement Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Student Added")
    elif choice == "2":
        print("Company Added")
    elif choice == "3":
        print("Generating Report...")
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
