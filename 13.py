# Lab 13 - Inventory Control System

# Initialize an inventory list with at least 4 products
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

# Use a while True loop so the program continues running until the user chooses to exit
while True:
    print("\n" + "=" * 50)
    print("                INVENTORY CONTROL SYSTEM")
    print("=" * 50)
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    
    # Prompt the user to choose an operation using numbers 1 to 5[cite: 22]
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        # 1: Loop through the list and display items with numbers[cite: 22]
        print("\n--- Current Inventory ---")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")
            
    elif choice == '2':
        # 2: Accept an item name from user input and add it using .append()[cite: 22]
        item_to_add = input("Enter item name to add: ")
        inventory.append(item_to_add)
        print(f"[SUCCESS] \"{item_to_add}\" added to inventory.")
        
    elif choice == '3':
        # 3: Check if the item exists using in. If found, remove it using .remove(); otherwise, display an error message[cite: 22]
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
            
    elif choice == '4':
        # 4: Sort the inventory alphabetically using .sort() and display the sorted list[cite: 22]
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i in range(len(inventory)):
            print(f"{i + 1}. {inventory[i]}")
            
    elif choice == '5':
        # 5: Print a goodbye message and exit the loop using break[cite: 22]
        print("\nThank you for using Inventory Control System. Goodbye!")
        break
        
    else:
        # If the user enters an invalid number, display an error message and display the menu again[cite: 22]
        print("\n[ERROR] Invalid choice. Please enter a number between 1 and 5.")