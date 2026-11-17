# Lab 20 - Office Daily Log Book
import os

FILENAME = "daily_log.txt"

def initialize_log(filename):
    if not os.path.exists(filename):
        initial_entries = [
            "09:00 AM - System server startup verified.",
            "10:30 AM - Morning attendance synchronized.",
            "02:15 PM - Network security patch applied."
        ]
        with open(filename, 'w') as f:
            for entry in initial_entries:
                f.write(entry + "\n")

def append_entry(filename, entry):
    with open(filename, 'a') as f:
        f.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")

def display_log(filename):
    if not os.path.exists(filename):
        print("[INFO] Log file is currently empty.")
        return
        
    print("\nDAILY LOG BOOK")
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines, 1):
        print(f"[{idx:02d}] {line.strip()}")
    print(f"\nTotal Logged Entries: {len(lines)}")

def main():
    initialize_log(FILENAME)
    
    while True:
        print("\n=== OFFICE DAILY LOG BOOK ===")
        print("1. Add Log Entry")
        print("2. Display Complete Log")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            entry = input("Enter log entry: ").strip()
            if entry:
                append_entry(FILENAME, entry)
            else:
                print("[ERROR] Entry cannot be empty.")
                
        elif choice == '2':
            display_log(FILENAME)
            
        elif choice == '3':
            print("Thank you for using the Daily Log Book. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()