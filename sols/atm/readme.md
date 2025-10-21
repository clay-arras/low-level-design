## stage 1: asking clarifying questions

- can users be in debt? as in, if someone withdraws cash when the account is at
zero, should we invalidate the withdrawal (if so, should we throw an error, or
something else?) OR should we let them widrawal and make the account negative?
- what does validate user accounts mean? should a user have a password, or can
they just authenticate using the ATM card security code? can different users use
the same card, or should each card be associated with only one user?
- should transactions be logged / stored?

- assuming that all PINs are unique, and can be represented as an integer.
- assuming an ATM card has the following characteristics: a number, a expiration
date (month / year), and a three-digit security code

- cash dispensing: assuming that the valid denominations are 100, 20, 10, and 5,
and that a greedy approach of always withdrawing the biggest denomination will
work
- concurrency and user interface: I think we should skip this for now.

---

- what happens if the user tries to withdraw a number that cannot be made using
20, 50, 100s? should it reject, OR should it give the user the closest number
less than their withdrawal count? 


## stage 2: design

need some sort of centralized system to keep track of number -> pin. (singleton)

class BankingSystem:
    _instance: BankingSystem | None = None
    accounts: list[Account]  
    number_to_card: dict[int, Card]
    card_to_acc: dict[Card, Account]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def auth_user(self, card_number: str, card_pin: str) -> Account | None:
        pass

    def withdraw(self, acc: Account, amount: int) -> bool:
        pass

    def deposit(self, acc: Account, amount: int) -> bool:
        pass

    def view_balance(self, acc: Account, amount: int) -> bool:
        pass


class ATM: 
    def __init__(self) -> None:
        self.curr_account: Account | None
        self.dispenser: CashDispenser

    def insert_card(self, card_number: str, card_pin: str) -> bool:
        pass
    
    def remove_card(self) -> None:
        pass

    def withraw(self, amount: int) -> bool:
        pass

    def deposit(self, amount: int) -> bool:
        pass

    def view_balance(self) -> int:
        pass

class CashDispenser:
    valid_denoms: set[int] = {20, 50, 100} 

    def __init__(self) -> None:
        self.left_cnt: dict[int, int] = {} # denom -> count

    def withdraw_cash(self, amount: int) -> bool:
        pass


class Account: 
    def __init__(self) -> None:
        self.__cards: list[Card]
        self.__balance: int
        self.__lock: Lock = threading.Lock()

    def withdraw(self, amount: int) -> bool:
        pass

    def deposit(self, amount: int) -> bool:
        pass
    
    def view_balance(self) -> int:
        pass


@dataclass
class Card:
    number: str
    pin: str
