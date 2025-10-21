from sols.atm.account import Account
from sols.atm.banking_system import BankingSystem
from sols.atm.cash_dispenser import CashDispenser


class ATM:
    def __init__(self) -> None:
        self.curr_account: Account | None
        self.dispenser: CashDispenser

    def insert_card(self, card_number: str, card_pin: str) -> bool:
        auth_acc = BankingSystem().auth_user(card_number=card_number, card_pin=card_pin)
        if auth_acc is None:
            return False
        self.curr_account = auth_acc

    def remove_card(self) -> None:
        self.curr_account = None

    def withraw(self, amount: int) -> dict[int, int] | None:
        if self.curr_account is None:
            return None
        if not BankingSystem().withdraw(acc=self.curr_account, amount=amount):
            return None
        withdraw_success = self.dispenser.withdraw_cash(amount=amount)
        return withdraw_success

    def deposit(self, amount: int) -> True | None:
        if self.curr_account is None:
            return
        if not BankingSystem().deposit(acc=self.curr_account, amount=amount):
            return
        return True

    def view_balance(self) -> int | None:
        if self.curr_account is None:
            return None
        return BankingSystem().view_balance(self.curr_account)
