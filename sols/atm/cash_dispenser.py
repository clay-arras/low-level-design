class CashDispenser:
    valid_denoms: set[int] = {20, 50, 100}

    def __init__(self) -> None:
        self.left_cnt: dict[int, int] = {}  # denom -> count

    def withdraw_cash(self, amount: int) -> dict[int, int] | None:
        if not self._can_withdraw(amount):
            return None

    def _can_withdraw(self, amount: int) -> bool:
        pass
