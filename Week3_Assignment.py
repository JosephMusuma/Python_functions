# Creating a function named calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = int(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount, or if no discount was applied, print the original price.
if final_price != original_price:
    print("Final price after applying a discount = Kenya Shillings", final_price)
else:
    print("No discount applied. Price = Kenya Shillings", original_price)
