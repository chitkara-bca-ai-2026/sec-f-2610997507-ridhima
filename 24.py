import csv


def read_all_students(filename="studentdata.txt"):
    print("\n" + "-" * 14 + " ALL ENROLLED STUDENTS " + "-" * 14)
    print(f"{'Roll No':<10} {'Name':<12} {'Subject':<12} {'Marks':<8}")
    print("-" * 51)

    count = 0
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(
                f"{row['RollNo']:<10} {row['Name']:<12} {row['Subject']:<12} {row['Marks']:<8}"
            )
            count += 1

    print("-" * 51)
    print(f"Total Records: {count}\n")


def filter_students_above_threshold(filename="studentdata.txt", threshold=50):
    print(f"\n" + "-" * 11 + f" STUDENTS WITH MARKS > {threshold} " + "-" * 11)
    print(f"{'Roll No':<10} {'Name':<12} {'Subject':<12} {'Marks':<8}")
    print("-" * 51)

    qualified_count = 0
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Marks"]) > threshold:
                print(
                    f"{row['RollNo']:<10} {row['Name']:<12} {row['Subject']:<12} {row['Marks']:<8}"
                )
                qualified_count += 1

    print("-" * 51)
    print(f"Qualified Students Count: {qualified_count}\n")


def main():
    filename = "studentdata.txt"

    print("=" * 45)
    print("       STUDENT RESULT ANALYSIS SYSTEM")
    print("=" * 45)

    while True:
        print("Select an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            read_all_students(filename)
        elif choice == "2":
            filter_students_above_threshold(filename, threshold=50)
        elif choice == "3":
            print("Thank you for using Student Result Analysis System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()