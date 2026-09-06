from decimal import Decimal, InvalidOperation

from ATMExcept import DepositError, InSuffFundError, WithDrawError


balance = Decimal("1000.00")


def _get_amount(prompt):
    """Return a valid money amount or raise ValueError."""
    try:
        amount = Decimal(input(prompt).strip())
    except InvalidOperation as error:
        raise ValueError("Amount must be numeric.") from error

    if not amount.is_finite():
        raise ValueError("Amount must be numeric.")

    return amount.quantize(Decimal("0.01"))


def deposit():
    global balance
    amount = _get_amount("Enter deposit amount: $")

    if amount <= 0:
        raise DepositError

    balance += amount
    print(f"Deposit successful. Current balance: ${balance:.2f}")


def withdraw():
    global balance
    amount = _get_amount("Enter withdrawal amount: $")

    if amount <= 0:
        raise WithDrawError
    if amount > balance:
        raise InSuffFundError

    balance -= amount
    print(f"Withdrawal successful. Current balance: ${balance:.2f}")


def balenq():
    print(f"Current balance: ${balance:.2f}")
