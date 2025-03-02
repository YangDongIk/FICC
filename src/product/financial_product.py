from abc import ABC, abstractmethod
from utils.cls_prop import generate_required_property


class FinancialProduct(ABC):
    def __init__(self, division_code, fund_code, type, product_code):
        self.division_code = division_code
        self.fund_code = fund_code
        self.product_type = type  # 상품구분
        self.product_code = product_code  # 상품코드
        self._position = None
        self._long_short = None

    long_short = generate_required_property("long_short")
    position = generate_required_property("position")
