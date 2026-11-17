# Lab 19 - Student Notes Management System
import os

FILENAME = "notes.txt"

def write_notes(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

def read_notes(filename):
    if not os.path.exists(filename):
        return "[INFO] No notes file exists yet. Please write notes first."
    with open(filename, 'r') as f:
        content = f.read()
    return content

def main():
    while True:
        print("\n=== STUDENT NOTES MANAGEMENT SYSTEM ===")
        print("1. Write / Save Notes")
        print("2. View Saved Notes")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            content = input("Enter notes to save: ")
            write_notes(FILENAME, content)
            
        elif choice == '2':
            print(f"\n--- Notes Content ({FILENAME}) ---")
            notes = read_notes(FILENAME)
            print(notes)
            
        elif choice == '3':
            print("Thank you for using the Notes Management System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()