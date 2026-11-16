# Lab 09 - Festival Decoration Designer

# 1. Take input from the user for the number of rows (n)
n = int(input("Enter the number of rows: "))

# Pattern 1 - Star Triangle (Right-Angled)
print("\nPattern 1: Star Triangle")
print("-" * 50)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 2 - Number Triangle
print("\nPattern 2: Number Triangle")
print("-" * 50)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 3 - Inverted Star Triangle
print("\nPattern 3: Inverted Star Triangle")
print("-" * 50)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 4 - Pyramid (Centered Triangle)
print("\nPattern 4: Pyramid")
print("-" * 50)
for i in range(1, n + 1):
    # Print spaces for centering
    print(" " * (n - i), end="")
    # Print stars with spaces
    for j in range(i):
        print("*", end=" ")
    print()