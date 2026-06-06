print("=" * 40)
print("PLACEMENT ANALYTICS SYSTEM")
print("=" * 40)

students = []
companies = []

while True:
    print("\n1. Add Student")
    print("2. Add Company")
    print("3. View Statistics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        cgpa = float(input("Enter CGPA: "))

        students.append({
            "name": name,
            "branch": branch,
            "cgpa": cgpa
        })

        print("Student record added successfully!")

    elif choice == "2":
        company = input("Enter Company Name: ")
        package = float(input("Enter Package (LPA): "))

        companies.append({
            "company": company,
            "package": package
        })

        print("Company record added successfully!")

    elif choice == "3":
        print("\n----- Placement Statistics -----")

        print("Total Students:", len(students))
        print("Total Companies:", len(companies))

        if companies:
            highest = max(companies, key=lambda x: x["package"])
            avg_package = sum(c["package"] for c in companies) / len(companies)

            print("Highest Package:", highest["package"], "LPA")
            print("Average Package:", round(avg_package, 2), "LPA")

    elif choice == "4":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice")
