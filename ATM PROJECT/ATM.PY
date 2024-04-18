class User:
    def __init__(self, user_id, pin, balance, name):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.name = name

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin


class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            user = self.users[user_id]
            if user.verify_pin(pin):
                self.current_user = user
                return True
        return False
    
    def welcome_message(self):
        print("""
  __    __     _                                          
 / / /\ \ \___| | ___ ___  _ __ ___   ___     
 \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
  \  /\  /  __/ | (_| (_) | | | | | |  __/ 
   \/  \/ \___|_|\___\___/|_| |_| |_|\___| 
                                                                   
    """)
        print("Welcome to OCTANET ATM!\n")

    def main_menu(self):
        print(f"Hello, {self.current_user.name}! How can we assist you today?\n")
        while True:
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Deposit Funds")
            print("4. Transfer Money")
            print("5. View Transaction History")
            print("6. Update PIN")
            print("7. Exit")
            choice = input("Please select an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                self.view_transaction_history()
            elif choice == "6":
                self.update_pin()
            elif choice == "7":
                print(f"Thank you for banking with OCTANET! Have a great day, {self.current_user.name}! 💼💳")
                break
            else:
                print("Invalid option. Please try again. ❌")

    def check_balance(self):
        print(f"Your current balance is ${self.current_user.balance}.\n")

    def withdraw(self):
        amount = float(input("How much would you like to withdraw?\n$"))
        if amount <= 0 or amount > self.current_user.balance:
            print("Invalid amount or insufficient funds. ❌")
        else:
            self.current_user.balance -= amount
            print("Processing request... 💼💰")
            print(f"Transaction successful! ${amount} has been withdrawn from your account. 💳")
            self.check_balance()

    def deposit(self):
        amount = float(input("How much would you like to deposit?\n$"))
        if amount <= 0:
            print("Invalid amount. ❌")
        else:
            self.current_user.balance += amount
            print(f"Deposit successful! ${amount} has been added to your account. 💳")
            self.check_balance()

    def transfer(self):
        recipient_id = input("Enter the recipient's user ID: ")
        if recipient_id not in self.users:
            print("Recipient not found. ❌")
            return
        recipient = self.users[recipient_id]
        amount = float(input("Enter the amount to transfer:\n$"))
        if amount <= 0 or amount > self.current_user.balance:
            print("Invalid amount or insufficient funds. ❌")
            return
        self.current_user.balance -= amount
        recipient.balance += amount
        print("Processing transfer... 💼💸")
        print(f"Transfer successful! ${amount} has been transferred to user ID: {recipient_id}. 💳")
        self.check_balance()

    def view_transaction_history(self):
        print("Transaction history not available in this version. 📜")

    def update_pin(self):
        new_pin = input("Enter your new PIN: ")
        self.current_user.pin = new_pin
        print("PIN updated successfully. 🔒")


def main():
    atm = ATM()

    # Add dummy users
    user1 = User("1234", "4321", 2000.0, "John Doe")
    user2 = User("5678", "8765", 500.0, "Jane Smith")
    user3 = User("9101", "0019", 1000.0, "Mary jon")
    user4 = User("1121", "1211", 1000.0,"curie")
    user5 = User("3141", "1413", 3000.0,"Tony stark")

    atm.add_user(user1)
    atm.add_user(user2)
    atm.add_user(user3)
    atm.add_user(user4)
    atm.add_user(user5)

    # User authentication
    atm.welcome_message()
    while True:
        user_id = input("Please enter your user ID: ")
        pin = input("Please enter your PIN: ")
        if atm.authenticate_user(user_id, pin):
            print("Authentication successful! ✔️\n")
            break
        else:
            print("Invalid user ID or PIN. Please try again. ❌")

    # Display main menu
    atm.main_menu()


if __name__ == "__main__":
    main()
