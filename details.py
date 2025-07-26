def collect_user_info():
    print("=== User Information Form ===")
    
    # Personal Information
    first_name = input("Enter your First Name: ")
    middle_name = input("Enter your Middle Name (optional): ")
    last_name = input("Enter your Last Name: ")
    email = input("Enter your Email Address: ")
    
    # Address Details
    street = input("Enter your Street or Post Office Address: ")
    address_line2 = input("Enter Address Line 2 (optional): ")
    city = input("Enter your City: ")
    state = input("Enter your State/Province: ")
    postal_code = input("Enter your Postal Code: ")
    country = input("Enter your Country: ")

    # Contact Numbers
    phone_home = input("Enter your Home Phone Number: ")
    phone_additional = input("Enter Additional Phone Number (optional): ")
    phone_fax = input("Enter Fax Number (optional): ")

    # Preferences
    receive_printed = input("Would you like to receive printed issues? (yes/no): ")

    # Public Profile
    public_profile = input("Enter Public Member Profile Text (max 500 characters): ")
    
    print("\n=== Summary of Entered Information ===")
    print(f"Name: {first_name} {middle_name} {last_name}")
    print(f"Email: {email}")
    print(f"Address: {street}, {address_line2}, {city}, {state}, {postal_code}, {country}")
    print(f"Phone - Home: {phone_home}")
    print(f"Phone - Additional: {phone_additional}")
    print(f"Phone - Fax: {phone_fax}")
    print(f"Printed Issues: {receive_printed}")
    print(f"Public Profile: {public_profile[:500]}")  # Limit to 500 chars


# Run the function
collect_user_info()