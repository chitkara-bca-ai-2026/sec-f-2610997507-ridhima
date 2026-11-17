# Lab 18 - Mathematics Learning Tool

def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    while True:
        print("\n=== MATHEMATICS LEARNING TOOL ===")
        print("1. Calculate Factorial")
        print("2. Generate Fibonacci Series")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            try:
                n = int(input("Enter a non-negative integer: "))
                if n < 0:
                    print("[ERROR] Factorial is not defined for negative numbers.")
                else:
                    result = factorial(n)
                    print(f"[RESULT] Factorial of {n} ({n}!) = {result}")
            except ValueError:
                print("[ERROR] Please enter a valid integer.")
                
        elif choice == '2':
            try:
                terms = int(input("Enter number of terms to generate: "))
                if terms <= 0:
                    print("[ERROR] Number of terms must be greater than 0.")
                else:
                    series = [fibonacci(i) for i in range(terms)]
                    print(f"[RESULT] Fibonacci series ({terms} terms): {series}")
            except ValueError:
                print("[ERROR] Please enter a valid integer.")
                
        elif choice == '3':
            print("Thank you for using the Mathematics Learning Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()