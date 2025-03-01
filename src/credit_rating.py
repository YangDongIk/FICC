class CreditRating:
    """
    신용등급을 관리하는 유틸 클래스
    여러 개의 등급을 받아 종합 평가하며, 외부 및 내부 등급을 제공한다.
    """

    # 등급별 순위 (숫자가 클수록 신용도 낮음, 위험도 높음)
    rank_map = {
        "AAA": 1,
        "AA+": 2,
        "AA": 3,
        "AA-": 4,
        "A+": 5,
        "A": 6,
        "A-": 7,
        "BBB+": 8,
        "BBB": 9,
        "BBB-": 10,
        "BB+": 11,
        "BB": 12,
        "BB-": 13,
        "B+": 14,
        "B": 15,
        "B-": 16,
        "CCC+": 17,
        "CCC": 18,
        "CCC-": 19,
        "D": 20,
    }

    # 등급별 위험값 (낮을수록 안전, 높을수록 위험)
    risk_value_map = {
        "AAA": 0.01,
        "AA+": 0.02,
        "AA": 0.03,
        "AA-": 0.04,
        "A+": 0.06,
        "A": 0.08,
        "A-": 0.10,
        "BBB+": 0.15,
        "BBB": 0.20,
        "BBB-": 0.25,
        "BB+": 0.35,
        "BB": 0.50,
        "BB-": 0.75,
        "B+": 1.00,
        "B": 1.50,
        "B-": 2.00,
        "CCC+": 3.00,
        "CCC": 4.00,
        "CCC-": 5.00,
        "D": 10.00,
    }

    def __init__(self, external_ratings=None, internal_ratings=None):
        """
        external_ratings: 외부 신용등급 리스트
        internal_ratings: 내부 신용등급 리스트
        """
        self.external_ratings = external_ratings or []
        self.internal_ratings = internal_ratings or []

    def get_lowest_rating(self, ratings):
        """주어진 등급 리스트에서 가장 낮은 등급을 찾음 (즉, 위험도가 가장 높은 등급)"""
        if not ratings:
            return None
        return min(ratings, key=lambda r: self.rank_map.get(r, float("inf")))

    @property
    def external_rate(self):
        """외부 등급 중 가장 낮은 등급을 반환"""
        return self.get_lowest_rating(self.external_ratings)

    @property
    def internal_rate(self):
        """내부 등급 중 가장 낮은 등급을 반환"""
        return self.get_lowest_rating(self.internal_ratings)

    def get_risk_value(self, rating):
        """해당 등급의 위험값 반환"""
        return self.risk_value_map.get(rating, None)

    def add_external_rating(self, rating):
        """외부 신용등급 추가"""
        if rating in self.rank_map:
            self.external_ratings.append(rating)

    def add_internal_rating(self, rating):
        """내부 신용등급 추가"""
        if rating in self.rank_map:
            self.internal_ratings.append(rating)
