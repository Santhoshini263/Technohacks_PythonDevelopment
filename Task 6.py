class ATM_Simulator:

    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Your account balance is: Rs. {self.balance}")

    def deposit_amt(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Invalid amount2.")

    def withdraw_amt(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient amount")

def main():
    atm = ATM_Simulator()
    print("\n*********** Welcome to the ATM! ***********")
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Cash Withdrawal")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: Rs. "))
                atm.deposit_amt(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: Rs. "))
                atm.withdraw_amt(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == 4:
            print("Thank you for using the ATM!!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


    