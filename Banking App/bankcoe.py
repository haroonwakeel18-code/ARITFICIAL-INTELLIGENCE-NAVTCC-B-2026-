# Bank Core Module - Handles user authentication and account creation

# Branch ID constant
branch_id = 2057

# List to store user information [customer_id, name, password]
users_info = []

def generate_customer_id():
    """
    Generates customer ID in format: branch_id-user_number
    Example: 2057-1, 2057-2, etc.
    """
    user_number = len(users_info) + 1
    return f"{branch_id}-{user_number}"

def create_account(name, password):
    """
    Creates a new bank account
    Args:
        name: Account holder's name
        password: Account password
    Returns:
        customer_id: Newly generated customer ID
    """
    customer_id = generate_customer_id()
    users_info.append([customer_id, name, password])
    print(f"\n✅ Account created successfully!")
    print(f"Your Customer ID is: {customer_id}")
    print(f"Account Holder: {name}")
    return customer_id

def login(customer_id, password):
    """
    Authenticates user login
    Args:
        customer_id: Customer ID to verify
        password: Password to verify
    Returns:
        bool: True if login successful, False otherwise
    """
    for user in users_info:
        if user[0] == customer_id and user[2] == password:
            print(f"\n✅ Login successful! Welcome back, {user[1]}!")
            return True
    
    print("\n❌ Invalid login! Customer ID or password is incorrect.")
    return False

def find_user_by_id(customer_id):
    """
    Helper function to find a user by their customer ID
    Args:
        customer_id: Customer ID to find
    Returns:
        user: User list if found, None otherwise
    """
    for user in users_info:
        if user[0] == customer_id:
            return user
    return None