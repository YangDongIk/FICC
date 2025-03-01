from .financial_product import FinancialProduct


class Traditional_Assets(FinancialProduct):
    def __init__(self, division_code, fund_code, product_type, product_code):
        super().__init__(division_code, fund_code, product_type, product_code)
        self._quantity = None
        self._price = None
