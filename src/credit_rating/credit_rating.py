from pandas import isna

from ..utils.cls_prop import generate_required_property, generate_property


class CreditRating:
    def __init__(self, **kwargs):
        def clean_value(value):
            """빈 값, NaN, pd.NA 등을 None으로 변환"""
            return None if isna(value) or value == "" else value

        self.kis = clean_value(kwargs.get("kis", None))
        self.kap = clean_value(kwargs.get("kap", None))
        self.nice = clean_value(kwargs.get("nice", None))
        self.fnp = clean_value(kwargs.get("fnp", None))
        self.moodys = clean_value(kwargs.get("moodys", None))
        self.snp = clean_value(kwargs.get("snp", None))
        self.fitch = clean_value(kwargs.get("fitch", None))
        self._overall_rating_dmst = None
        self._overall_rating_frgn = None
        self._internal_rating = None

    overall_rating = generate_required_property("overall_rating")
    internal_rating = generate_property("internal_rating")

    rank_map = {
        "AAA": 1,
        "Aaa": 1,
        "AA+": 2,
        "Aa1": 2,
        "AA": 3,
        "AA0": 3,
        "Aa2": 3,
        "AA-": 4,
        "Aa3": 4,
        "A+": 5,
        "A1": 5,
        "A": 6,
        "A0": 6,
        "A2": 6,
        "A-": 7,
        "A3": 7,
        "BBB+": 8,
        "Baa1": 8,
        "BBB": 9,
        "BBB0": 9,
        "Baa2": 9,
        "BBB-": 10,
        "Baa3": 10,
        "BB+": 11,
        "Ba1": 11,
        "BB": 12,
        "BB0": 12,
        "Ba2": 12,
        "BB-": 13,
        "Ba3": 13,
        "B+": 14,
        "B1": 14,
        "B": 15,
        "B0": 15,
        "B2": 15,
        "B-": 16,
        "B3": 16,
        "CCC+": 17,
        "Caa1": 17,
        "CCC": 18,
        "CCC0": 18,
        "Caa2": 18,
        "CCC-": 19,
        "Caa3": 19,
        "D": 20,
        "D0": 20,
        "무등급": 99,
    }

    def to_score(self, ):

    def evaluate_or_domestic(self):
        