# Lab 15 - Student Information Management System

# 1. Initial Data Setup: Store at least 3 default students in a main dictionary 'students'[cite: 25]
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karen",
        "Branch": "BCA AI",
        "Semester": 1,
        "Marks": [74, 80, 82]
    }
}

# 2. Control Flow: Use a while true loop displaying choices 1 through 7[cite: 25, 26]
while True:
    print("\n" + "=" * 65)
    print("             STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 65)
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == '1':
        # Choice 1 (View All): Iterate through students.items()
        print("\n--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']}")
            print(f"  | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")
        
    elif choice == '2':
        # Choice 2 (Search): Perform safe record lookup using .get()[cite: 25, 26]
        roll = input("Enter Roll Number to search: ")
        student_record = students.get(roll)
        if student_record:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"Name     : {student_record['Name']}")
            print(f"Branch   : {student_record['Branch']}")
            print(f"Semester : {student_record['Semester']}")
            print(f"Marks    : {student_record['Marks']}")
        else:
            print(f"\n[ERROR] Record for Roll No {roll} not found.")
            
    elif choice == '3':
        # Choice 3 (Register): Prompt for details, check if roll number already exists[cite: 26]
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Student with Roll No {roll} already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            semester = int(input("Enter Semester: "))
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("Subject 1: "))
            m2 = int(input("Subject 2: "))
            m3 = int(input("Subject 3: "))
            
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": [m1, m2, m3]
            }
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            
    elif choice == '4':
        # Choice 4 (Update): Prompt for Roll Number and field to update[cite: 26]
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            student = students[roll]
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field_choice = input("Choose field to update (1 for Branch, 2 for Semester): ")
            
            if field_choice == '1':
                new_branch = input("Enter new branch: ")
                student['Branch'] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field_choice == '2':
                new_sem = int(input("Enter new semester: "))
                student['Semester'] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid field choice.")
        else:
            print(f"[ERROR] Roll No {roll} not found.")
            
    elif choice == '5':
        # Choice 5 (Academic Performance): Calculate total and average marks[cite: 26]
        roll = input("Enter Roll Number for Academic Performance: ")
        if roll in students:
            student = students[roll]
            total_marks = sum(student['Marks'])
            avg_marks = total_marks / len(student['Marks'])
            pass_status = "PASS" if avg_marks >= 40 else "FAIL"
            
            print("\n=================== ACADEMIC REPORT ===================")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total_marks} / 300")
            print(f"Average Marks: {avg_marks:.2f}%")
            print(f"Final Result : {pass_status}")
            print("=======================================================")
        else:
            print(f"[ERROR] Roll No {roll} not found.")
            
    elif choice == '6':
        # Choice 6 (Delete): Safely remove the record using .pop()[cite: 26]
        roll = input("Enter Roll Number to delete: ")
        removed_record = students.pop(roll, None)
        if removed_record:
            print(f"\n[SUCCESS] Record for '{removed_record['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"\n[ERROR] Roll No {roll} not found.")
            
    elif choice == '7':
        # Choice 7 (Exit): Print goodbye message and exit loop using break[cite: 26]
        print("\nThank you for using Student Information System. Goodbye!")
        break
        
    else:
        print("\n[ERROR] Invalid choice. Please enter a number between 1 and 7[cite: 25, 26].")