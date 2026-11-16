# Lab 08 - School Result Processing

print("=" * 60)
print("                    SCHOOL RESULT PROCESSING")
print("=" * 60)

# 1. Accept student details
student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

total_marks = 0.0
has_failed = False

# 2. Input marks for 5 subjects using a loop
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    
    # Validate each mark: must be between 0 and 100
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100. Exiting program.")
        exit()
        
    # Check passing status: below 40 means failed
    if mark < 40:
        has_failed = True
        
    total_marks += mark

# 3. Calculate total and percentage
percentage = (total_marks / 500.0) * 100

# 4. Assign Grade & Remark using if-elif-else
if has_failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

# 5. Display a formatted Report Card showing student details, total marks, percentage, result, grade, and remarks
print("\n" + "=" * 60)
print("                     STUDENT REPORT CARD")
print("=" * 60)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 60)
print(f"Total Marks  : {total_marks} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remarks}")
print("=" * 60)