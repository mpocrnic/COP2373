import re

# Function to validate US phone numbers
# The function returns True if the input matches one of the patterns.
def validate_phone(phone):
    pattern = re.compile(r'^(\(\d{3}\)\s?|\d{3}-?)\d{3}-?\d{4}$')
    return bool(pattern.match(phone))

# Function to validate US Social Security Numbers (SSNs).
def validate_ssn(ssn):
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Function to validate ZIP codes.
def validate_zip(zip_code):
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

# Main function to interact with the user.
def main():
    print("Enter your personal information for validation.\n")

    # Prompting the user for each piece of information
    phone = input("Enter your phone number: ")
    ssn = input("Enter your Social Security Number: ")
    zip_code = input("Enter your ZIP code: ")

    # Displaying the validation results
    print("\nValidation Results:")
    print(f"Phone Number Valid: {validate_phone(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"ZIP Code Valid: {validate_zip(zip_code)}")

# Executes the main function when run directly.
if __name__ == "__main__":
    main()
