class DepositError(Exception):
    """Raised when a deposit amount is zero or negative."""


class WithDrawError(Exception):
    """Raised when a withdrawal amount is zero or negative."""


class InSuffFundError(Exception):
    """Raised when the account balance cannot cover a withdrawal."""
