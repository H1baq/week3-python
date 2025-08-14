"""
QUESTION:
Create a function named calculate_discount(price, discount_percent) that calculates 
the final price after applying a discount. The function should take the original 
price (price) and the discount percentage (discount_percent) as parameters.

If the discount is 20% or higher, apply the discount; otherwise, return the original price.

Using the calculate_discount function, prompt the user to enter the original price 
of an item and the discount percentage. Print the final price after applying the discount, 
or if no discount was applied, print the original price.
"""

# Step 1: Define the function to calculate the final price
def calculate_discount(price, discount_percent):
    """
    This function checks if the discount is 20% or more.
    - If YES: applies the discount and returns the new price.
    - If NO: returns the original price.
    """
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = (discount_percent / 100) * price
        # Subtract discount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

# Step 2: Ask the user for the original price
price = float(input("Enter the original price: "))

# Step 3: Ask the user for the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Step 4: Call the function to get the final price
final_price = calculate_discount(price, discount_percent)

# Step 5: Show the result
# Using round() to display only 2 decimal places for currency formatting
print(f"The final price is: {round(final_price, 2)}")
