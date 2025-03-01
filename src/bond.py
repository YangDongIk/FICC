from dataclasses import dataclass
from datetime import datetime

from .traditional_assets import Traditional_Assets
from .util import generate_property


@dataclass
class Bond_Info:
    type: str
    code: str
    name: str
    crncy: str
    issue_date: datetime
    maturity_date: datetime
    coupon_rate: float  # 할인채는 할인발행률
    coupon_cycle: int  # 연당 이표,0는 할인채
    issure: str
    issure_type: str
    credit_rating: str


class Bond(Traditional_Assets):
    def __init__(
        self,
        type,
        code,
        name,
        quantity,
        crncy,
        issue_date,
        maturity_date,
        cpn_rate,
    ):
        super().__init__(type, code, name, quantity, crncy)
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.cpn_rate = cpn_rate
        self._issure = None
        self._ytm = None
        self._price = None

    issure = generate_property("issure")
    ytm = generate_property("ytm")
    price = generate_property("price")
    issure_type = generate_property("issure_type")
    bond_type = generate_property("bond_type")
