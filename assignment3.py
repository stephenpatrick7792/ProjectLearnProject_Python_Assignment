# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is less than 20%, no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main Program ---
# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call function
    final_price = calculate_discount(price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
