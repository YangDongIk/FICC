from abc import ABC, abstractmethod


class FinancialProduct(ABC):
    def __init__(self, type, product_code, product_name):
        self.product_type = type  # 상품구분
        self.product_code = product_code  # 상품코드
        self.product_name = product_name  # 상품명
        self._position = None

    @property
    def position(self):
        if self._position is None:
            raise ValueError("position 속성이 설정되지 않았습니다.")
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
