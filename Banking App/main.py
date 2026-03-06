# Main Module - Application entry point and menu handling

import bankcoe
import accounts

def banking_menu(customer_id):
    """
    Displays banking operations menu after successful login
    Args:
        customer_id: Logged in customer's ID
    """
    while True:
        print("\n" + "="*40)
        print("           BANKING MENU")
        print("="*40)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")
        print("="*40)
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                # Check Balance
                balance = accounts.check_balance(customer_id)
                print(f"\n💰 Current Balance: ${balance:.2f}")
            
            elif choice == 2:
                # Deposit Money
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    accounts.deposit(customer_id, amount)
                except ValueError:
                    print("\n❌ Invalid amount! Please enter a number.")
            
            elif choice == 3:
                # Withdraw Money
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    accounts.withdraw(customer_id, amount)
                except ValueError:
                    print("\n❌ Invalid amount! Please enter a number.")
            
            elif choice == 4:
                # Logout
                print("\n✅ Logged out successfully!")
                break
            
            else:
                print("\n❌ Invalid choice! Please enter 1-4.")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")

def main():
    """
    Main function - Displays welcome message and main menu
    """
    while True:
        print("\n" + "="*40)
        print("      WELCOME TO ABC BANK")
        print("="*40)
        print("1. Create an account")
        print("2. Login to account")
        print("3. Exit")
        print("="*40)
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                # Create Account
                print("\n--- Create New Account ---")
                name = input("Enter your full name: ").strip()
                if not name:
                    print("❌ Name cannot be empty!")
                    continue
                
                password = input("Create a password: ").strip()
                if not password:
                    print("❌ Password cannot be empty!")
                    continue
                
                # Confirm password
                confirm_password = input("Confirm password: ").strip()
                if password != confirm_password:
                    print("❌ Passwords do not match!")
                    continue
                
                customer_id = bankcoe.create_account(name, password)
                
                # Initialize balance for new account
                accounts.check_balance(customer_id)
            
            elif choice == 2:
                # Login
                print("\n--- Login to Your Account ---")
                customer_id = input("Enter your Customer ID: ").strip()
                password = input("Enter your password: ").strip()
                
                if bankcoe.login(customer_id, password):
                    # Show banking menu after successful login
                    banking_menu(customer_id)
            
            elif choice == 3:
                # Exit
                print("\nThank you for banking with ABC Bank!")
                print("Have a great day!")
                break
            
            else:
                print("\n❌ Invalid choice! Please enter 1-3.")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()