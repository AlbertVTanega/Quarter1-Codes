full_name = input("Enter your full name (First, Middle, Last): ")

# Split into parts
first, middle, last = full_name.split(",")

# Remove extra spaces and capitalize properly
first = first.strip().capitalize()
middle = middle.strip().capitalize()
last = last.strip().title()   # title() handles names like "dela cruz"

# Convert middle name to initial with a period
middle_initial = middle[0] + "."

# Format output
formatted_name = f"{last}, {first} {middle_initial}"

# Display result
print("Formatted Name:", formatted_name)