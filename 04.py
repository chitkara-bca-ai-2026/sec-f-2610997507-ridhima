
product_name = input("Enter Product Name : ")


price = float(input("Enter Price : "))


quantity = int(input("Enter Quantity : "))


total_price = price * quantity


amount_str = str(total_price)


print("\n" + "=" * 55)
print("                     DATA CONVERSION UTILITY")
print("=" * 55)
print(f"\nEnter Product Name : {product_name}")
print(f"Enter Price        : {price}")
print(f"Enter Quantity     : {quantity}")

print("\n" + "-" * 55)
print("                   TYPE CASTING SUMMARY")
print("-" * 55)
print(f"{'Variable':<15} {'Value':<12} {'Python Type'}")
print("-" * 55)
print(f"{'product_name':<15} {product_name:<12} {str(type(product_name))}")
print(f"{'price':<15} {price:<12} {str(type(price))}")
print(f"{'quantity':<15} {quantity:<12} {str(type(quantity))}")
print(f"{'total_price':<15} {total_price:<12} {str(type(total_price))}")
print(f"{'amount_str':<15} {amount_str:<12} {str(type(amount_str))}")
print("-" * 55)


print("\n                        TAX INVOICE")
print("-" * 55)
print(f"Product Name       : {product_name}")
print(f"Price per Unit     : Rs. {price}")
print(f"Quantity           : {quantity}")
print("-" * 55)
print(f"Invoice Total      : Rs. {amount_str}")
print("=" * 55)