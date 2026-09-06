from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit, withdraw, balenq

while True:
    try:
        menu()
        ch = int(input("Enter your choice: "))

        match ch:
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("DON'T ENTER NEGATIVE / ZERO AMOUNT FOR DEPOSIT")
                except ValueError:
                    print("DON'T ENTER LETTERS OR SYMBOLS FOR DEPOSIT")

            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("DON'T ENTER NEGATIVE / ZERO AMOUNT FOR WITHDRAW")
                except InSuffFundError:
                    print("YOUR ACCOUNT DOES NOT HAVE SUFFICIENT FUNDS")
                except ValueError:
                    print("DON'T ENTER LETTERS OR SYMBOLS FOR WITHDRAW")

            case 3:
                balenq()

            case 4:
                print("THANKS FOR USING THIS PROGRAM")
                break

            case _:
                print("Wrong operation selection — try again.")

    except ValueError:
        print("DON'T ENTER LETTERS OR SYMBOLS FOR CHOICE — TRY AGAIN")
