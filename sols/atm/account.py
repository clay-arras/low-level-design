from threading import Lock

from sols.atm.card import Card


class Account:
    def __init__(self) -> None:
        self.cards: list[Card]
        self.__balance: int
        self.__lock: Lock = Lock()

    def withdraw(self, amount: int) -> bool:
        with self.__lock:
            if self.__balance - amount >= 0:
                self.__balance -= amount
                return True
            return False

    def deposit(self, amount: int) -> bool:
        with self.__lock:
            self.__balance += amount
            return True

    def view_balance(self) -> int:
        with self.__lock:
            return self.__balance
