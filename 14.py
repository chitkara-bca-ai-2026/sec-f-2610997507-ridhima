# Lab 14 - Library Book Collection

# 1. Initial Data Setup:
# Store at least 4 default books as tuples in a list 'books'. Each tuple must contain (title, author, year, category), with year stored as a string.
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff with Python", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Extract the initial unique categories into a set named 'library_categories'[cite: 23, 24].
library_categories = {book[3] for book in books}

# Initialize a second set named 'student_wishlist' with at least 4 requested genres[cite: 23, 24].
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

# 2. Control Flow: Use a while true loop with choices 1 to 6[cite: 23, 24].
while True:
    print("\n" + "=" * 65)
    print("                 LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 65)
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        # Choice 1 (View Books): Loop through books, unpack each tuple, and print formatted details with total book count[cite: 23, 24].
        print("\n--- Current Library Catalog (Fixed Records) ---")
        for i, (title, author, year, category) in enumerate(books, 1):
            print(f"{i}. \"{title}\" by {author} ({year}) | Genre: {category}")
        print(f"Total Books: {len(books)}")
        
    elif choice == '2':
        # Choice 2 (Add Book): Prompt for title, author, year, and category. Append to books and library_categories[cite: 23, 24].
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        
        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)
        
        print(f"[SUCCESS] \"{title}\" added as an immutable catalog record.")
        print(f"[INFO] Category set updated with: \"{category}\"")
        
    elif choice == '3':
        # Choice 3 (View Categories): Display all unique categories from library_categories in sorted order, along with total count[cite: 24].
        print("\n--- Unique Categories Available in Library (Set) ---")
        sorted_categories = sorted(list(library_categories))
        for cat in sorted_categories:
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")
        
    elif choice == '4':
        # Choice 4 (Add to Wishlist): Prompt for a requested genre and add it to student_wishlist[cite: 24].
        print("\n--- Add to Student Wishlist ---")
        requested_genre = input("Enter requested genre: ")
        student_wishlist.add(requested_genre)
        print(f"[SUCCESS] \"{requested_genre}\" added to student wishlist.")
        
    elif choice == '5':
        # Choice 5 (Gap Analysis): Display current sets and calculate Intersection, Difference, and Union[cite: 24].
        print("\n=================== CATEGORY GAP ANALYSIS ===================")
        print(f"Library Holdings (Set): {sorted(list(library_categories))}")
        print(f"Student Wishlist (Set): {sorted(list(student_wishlist))}")
        print("-" * 61)
        
        # Intersection (&): Books requested that are already available in the library[cite: 24].
        intersection_res = library_categories.intersection(student_wishlist)
        print(f"1. Already in Stock (Intersection &):\n   {sorted(list(intersection_res))}")
        
        # Difference (-): Requested genres that the library does not own yet (procurement/purchase order)[cite: 24].
        difference_res = student_wishlist.difference(library_categories)
        print(f"\n2. Purchase Order Needed (Difference -):\n   {sorted(list(difference_res))}")
        
        # Union (|): Complete combined genre coverage[cite: 24].
        union_res = library_categories.union(student_wishlist)
        print(f"\n3. Full Combined Genre Coverage (Union |):\n   {sorted(list(union_res))}")
        print("=============================================================")
        
    elif choice == '6':
        # Choice 6 (Exit): Print a polite goodbye message and exit the loop using break[cite: 24].
        print("\nThank you for using the Library Manager. Goodbye!")
        break
        
    else:
        print("\n[ERROR] Invalid choice. Please enter a number between 1 and 6.")