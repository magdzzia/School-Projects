# defining a global variable of bank_balance as the accumulator
bank_balance = 0

# Define main function
def main():
    # setting an initalized value for a while loop
    leave = "n"
    # defining a loop in order to continue if user hasn't exited
    while leave == "n":
        # defining the layout and input option
        option = int(input("\n-----Your Banking Options-----" +
                           "\n\n1. Check Balance" +
                           "\n2. Deposit" +
                           "\n3. Withdraw" +
                           "\n4. Exit" +
                           "\n\n------------------------------" +
                           "\nPlease select an option: "))
        # defining the if statements for each option
        if option == 1:
            check_balance(bank_balance)
        elif option == 2:
            deposit(bank_balance)
        elif option == 3:
            withdraw(bank_balance)
        elif option == 4:
            exit_choice = input("Do you want to exit (y/n)? ")
            # if statement for when the user decides to pick either y or n to exit option
            if exit_choice == "y":
                print("Goodbye!")
                leave = "y"
            elif exit_choice == "n":
                leave == "n"
            else:
                print("Please put in a proper option!")

# Define check_balance function
def check_balance(balance):
    print(f'Current balance: ${balance:,.2f}')

# Define deposit function
def deposit(deposit_balance):
    global bank_balance
    # asking the user how much they want to deposit
    deposit = float(input("Enter the amount to deposit: $"))
    print(f'Deposited ${deposit:,.2f}.')
    # adding to the accumulator
    bank_balance = deposit_balance + deposit
    print(f'New balance: ${bank_balance:,.2f}.')

# Define withdraw function
def withdraw(withdraw_balance):
    global bank_balance
    # asking the user how much they want to withdraw
    withdraw = float(input("Enter the amount to withdraw: $"))
    # setting an if statement in case user wants to with draw more or and else statement that states they can't withdraw more than they have
    if withdraw <= bank_balance:
        print(f'Withdrew ${withdraw:,.2f}.')
        # subtractin from the accumulator
        bank_balance = withdraw_balance - withdraw
        print(f'New balance: ${bank_balance:,.2f}.')
    else:
        print('Insufficient funds!')
    
main() # calling the function
