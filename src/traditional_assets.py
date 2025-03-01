from .financial_product import FinancialProduct


class Traditional_Assets(FinancialProduct):
    def __init__(self, type, code, name, issure, quantity, crncy):
        super().__init__(type, code, name)
        self.issure = issure
        self.quantity = quantity
        self.crncy = crncy
