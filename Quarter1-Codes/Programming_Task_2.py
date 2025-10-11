# Delivery Fee Calculator
# This program calculates the delivery fee based on distance and rate per kilometer.
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

# Calculate total fee
total_fee = distance * rate

# Display result
print(f"Total Delivery Fee: ₱{total_fee:.2f}")
