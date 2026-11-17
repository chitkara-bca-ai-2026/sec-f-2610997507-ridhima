# Lab 17 - Student Records Management System

def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    name = student["Name"]
    marks = student["Marks"]
    total, average = calculate_results(marks)
    print(f"Roll No: {roll} | Name: {name} | Marks: {marks} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    if roll in records:
        print(f"[ERROR] Student with Roll Number '{roll}' already exists.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")

def main():
    students = {
        "101": {"Name": "Aman", "Marks": [85, 90, 78]},
        "102": {"Name": "Riya", "Marks": [92, 88, 95]},
        "103": {"Name": "Karan", "Marks": [74, 80, 82]}
    }
    
    while True:
        print("\n=== STUDENT RECORDS MANAGEMENT SYSTEM ===")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- All Student Records ---")
            if not students:
                print("No student records available.")
            else:
                for roll, student in students.items():
                    display_student(roll, student)
                print(f"Total Students: {len(students)}")
                
        elif choice == '2':
            print("\n--- Add New Student ---")
            roll = input("Enter Roll Number: ").strip()
            name = input("Enter Student Name: ").strip()
            try:
                print("Enter marks for 3 subjects (0-100):")
                m1 = int(input("Subject 1: "))
                m2 = int(input("Subject 2: "))
                m3 = int(input("Subject 3: "))
                if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
                    print("[ERROR] Marks must be between 0 and 100.")
                    continue
                add_student(students, roll, name, [m1, m2, m3])
            except ValueError:
                print("[ERROR] Please enter valid integer marks.")
                
        elif choice == '3':
            roll = input("Enter Roll Number to search: ").strip()
            student = students.get(roll)
            if student:
                print("[RECORD FOUND]")
                display_student(roll, student)
            else:
                print(f"[ERROR] No student found with Roll Number '{roll}'.")
                
        elif choice == '4':
            print("Thank you for using the Student Records System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()