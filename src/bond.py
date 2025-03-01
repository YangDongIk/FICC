from sys import settrace
from traditional_assets import Traditional_Assets


class Bond(Traditional_Assets):
    def __init__(
        self,
        type,
        code,
        name,
        issure,
        quantity,
        crncy,
        issue_date,
        maturity_date,
        cpn_rate,
    ):
        super().__init__(type, code, name, issure, quantity, crncy)
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.cpn_rate = cpn_rate
        self._ytm = None
        self._price = None

    @property
    def price(self):
        if self._price is None:
            raise ValueError("price 속성이 설정되지 않았습니다.")
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
