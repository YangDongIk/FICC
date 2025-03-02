from abc import ABC, abstractmethod
import pandas as pd
from src.risk_amount.risk import RiskAmount


class Portfolio(ABC):
    def __init__(self, name):
        self.name = name
        self.products = {}  # 딕셔너리 형태로 변경 {상품코드: 금융상품 객체}
        self.sub_portfolios = []
        self.risk_amount = RiskAmount()

    def add_product(self, product, product_code):
        """포트폴리오에 금융상품 추가 (상품 코드를 키로 사용)"""
        self.products[product_code] = product

    def add_portfolio(self, portfolio):
        """포트폴리오에 하위 포트폴리오 추가"""
        self.sub_portfolios.append(portfolio)

    def get_product_by_code(self, product_code):
        """상품 코드를 통해 금융상품 조회"""
        return self.products.get(product_code, None)  # 존재하지 않으면 None 반환

    def get_all_products(self):
        """현재 포트폴리오 및 하위 포트폴리오의 모든 금융상품을 리스트로 반환"""
        all_products = list(
            self.products.values()
        )  # 딕셔너리에서 값만 가져와 리스트로 변환
        for sub_portfolio in self.sub_portfolios:
            all_products.extend(
                sub_portfolio.get_all_products()
            )  # 하위 포트폴리오의 상품 추가
        return all_products

    def to_dataframe(self):
        """포트폴리오 내 모든 금융상품을 데이터프레임 형태로 변환"""
        data = [
            {
                "Portfolio": self.name,
                "Product Name": p.name,
                "Market Value": p.market_value,
            }
            for p in self.get_all_products()
        ]
        return pd.DataFrame(data)

    def calculate_risk_amount(self):
        """포트폴리오 내 모든 금융상품을 기반으로 위험액 계산"""
        return self.risk_amount.calculate_total_risk(self.get_all_products())
