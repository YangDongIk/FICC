from dataclasses import dataclass, field
from datetime import datetime

from .util import generate_property
from .traditional_assets import Traditional_Assets
from .credit_rating import CreditRating


@dataclass
class Bond_Info:
    bond_type: str
    name: str
    crncy: str
    issue_date: datetime
    maturity_date: datetime
    coupon_method: str
    coupon_rate: float  # 할인채는 할인발행률
    coupon_cycle: int  # 연당 이표,0는 할인채
    issure: str
    issure_type: str
    issure_country: str
    credit_rating: CreditRating = field(default_factory=CreditRating)


class Bond(Traditional_Assets):
    def __init__(
        self,
        division_code,
        fund_code,
        type,
        code,
        bond_info: Bond_Info,
    ):
        super().__init__(division_code, fund_code, type, code)
        self.bond_info = bond_info
