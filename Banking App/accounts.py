# Accounts Module - Handles banking operations like balance check, deposit, withdrawal

# List to store balance records [customer_id, balance]
balance_record = []

def find_balance_record(customer_id):
    """
    Helper function to find balance record for a customer
    Args:
        customer_id: Customer ID to find
    Returns:
        record: Balance record if found, None otherwise
    """
    for record in balance_record:
        if record[0] == customer_id:
            return record
    return None

def check_balance(customer_id):
    """
    Returns the user's current balance
    Args:
        customer_id: Customer ID to check balance for
    Returns:
        float: Current balance or 0 if no account exists
    """
    record = find_balance_record(customer_id)
    if record:
        return record[1]
    else:
        # Create balance record if it doesn't exist
        balance_record.append([customer_id, 0.0])
        return 0.0

def deposit(customer_id, amount):
    """
    Adds amount to the user's balance
    Args:
        customer_id: Customer ID
        amount: Amount to deposit
    Returns:
        bool: True if deposit successful, False otherwise
    """
    if amount <= 0:
        print("\n❌ Invalid amount! Please enter a positive amount.")
        return False
    
    record = find_balance_record(customer_id)
    if record:
        record[1] += amount
    else:
        balance_record.append([customer_id, amount])
    
    print(f"\n✅ Successfully deposited: ${amount:.2f}")
    print(f"Current balance: ${check_balance(customer_id):.2f}")
    return True

def withdraw(customer_id, amount):
    """
    Deducts amount from balance if sufficient funds available
    Args:
        customer_id: Customer ID
        amount: Amount to withdraw
    Returns:
        bool: True if withdrawal successful, False otherwise
    """
    if amount <= 0:
        print("\n❌ Invalid amount! Please enter a positive amount.")
        return False
    
    current_balance = check_balance(customer_id)
    
    if current_balance >= amount:
        record = find_balance_record(customer_id)
        record[1] -= amount
        print(f"\n✅ Successfully withdrew: ${amount:.2f}")
        print(f"Current balance: ${record[1]:.2f}")
        return True
    else:
        print(f"\n❌ Insufficient balance!")
        print(f"Current balance: ${current_balance:.2f}")
        print(f"Requested withdrawal: ${amount:.2f}")
        return False