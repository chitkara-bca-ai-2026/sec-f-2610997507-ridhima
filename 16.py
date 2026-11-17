# Lab 16 - Enterprise Modular Utility Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

def main():
    history = []
    
    while True:
        print("\n=== ENTERPRISE MODULAR UTILITY CALCULATOR ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus Remainder (%)")
        print("6. Power / Exponentiation (Default: Square)")
        print("7. View Calculation History")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("[ERROR] Please enter valid numeric values.")
                continue
                
            num1_fmt = format_number(num1)
            num2_fmt = format_number(num2)
            
            if choice == '1':
                res = add(num1, num2)
                op_str = f"{num1_fmt} + {num2_fmt} = {format_number(res)}"
                print(f"[RESULT] {op_str}")
                history.append(op_str)
            elif choice == '2':
                res = subtract(num1, num2)
                op_str = f"{num1_fmt} - {num2_fmt} = {format_number(res)}"
                print(f"[RESULT] {op_str}")
                history.append(op_str)
            elif choice == '3':
                res = multiply(num1, num2)
                op_str = f"{num1_fmt} * {num2_fmt} = {format_number(res)}"
                print(f"[RESULT] {op_str}")
                history.append(op_str)
            elif choice == '4':
                res = divide(num1, num2)
                if res is None:
                    print("[ERROR] Division by zero is not allowed.")
                else:
                    op_str = f"{num1_fmt} / {num2_fmt} = {format_number(res)}"
                    print(f"[RESULT] {op_str}")
                    history.append(op_str)
            elif choice == '5':
                res = modulus(num1, num2)
                if res is None:
                    print("[ERROR] Modulus by zero is not allowed.")
                else:
                    op_str = f"{num1_fmt} % {num2_fmt} = {format_number(res)}"
                    print(f"[RESULT] {op_str}")
                    history.append(op_str)
                    
        elif choice == '6':
            try:
                base_input = input("Enter base number: ")
                base = float(base_input)
                exp_input = input("Enter exponent (Press Enter for default square): ").strip()
                if exp_input == "":
                    res = power(base)
                    op_str = f"{format_number(base)}^2 = {format_number(res)}"
                else:
                    exp = float(exp_input)
                    res = power(base, exp)
                    op_str = f"{format_number(base)}^{format_number(exp)} = {format_number(res)}"
                print(f"[RESULT] {op_str}")
                history.append(op_str)
            except ValueError:
                print("[ERROR] Please enter valid numeric values.")
                
        elif choice == '7':
            print("\n--- Calculation History Ledger ---")
            if not history:
                print("No calculations performed yet.")
            else:
                for idx, record in enumerate(history, 1):
                    print(f"{idx}. {record}")
                    
        elif choice == '8':
            print("Thank you for using Enterprise Modular Utility Calculator. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select an option between 1 and 8.")

if __name__ == "__main__":
    main()