from dataclasses import dataclass, field
from datetime import datetime

from utils.cls_prop import generate_property
from product.traditional_assets import Traditional_Assets
from credit_rating.credit_rating import CreditRating


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
    bond_type_code: str


class Bond(Traditional_Assets):
    def __init__(
        self,
        division_code,
        fund_code,
        type,
        code,
        bond_info: Bond_Info,
        rating: CreditRating,
    ):
        super().__init__(division_code, fund_code, type, code)
        self.bond_info = bond_info
        self._rating = rating

    @property
    def external_rating(self):
        if self.bond_info.bond_type_code in [
            "C21",
            "111200",
            "111100",
        ]:
            return "국채_무등급"
        return self._rating.external_rating

    @property
    def internal_rating(self):
        if self.bond_info.bond_type_code in [
            "C21",
            "111200",
            "111100",
        ]:
            return "1"
        return self._rating.internal_rating
