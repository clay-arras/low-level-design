from sols.atm.account import Account
from sols.atm.card import Card


class BankingSystem:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, accounts: list[Account]) -> None:
        if self._initialized:
            return

        self.accounts: list[Account] = accounts
        self.number_to_card: dict[str, Card] = {}
        self.card_to_acc: dict[Card, Account] = {}

        for acc in self.accounts:
            for card in acc.cards:
                self.card_to_acc[card] = acc
                self.number_to_card[card.number] = card

        self._initialized = True

    def auth_user(self, card_number: str, card_pin: str) -> Account | None:
        if card_number not in self.number_to_card.items():
            return None
        actual_card = self.number_to_card[card_number]
        if actual_card.pin != card_pin:
            return None
        return self.card_to_acc[actual_card]

    def withdraw(self, acc: Account, amount: int) -> bool:
        return acc.withdraw(amount=amount)

    def deposit(self, acc: Account, amount: int) -> bool:
        return acc.deposit(amount=amount)

    def view_balance(self, acc: Account) -> int | None:
        return acc.view_balance()
