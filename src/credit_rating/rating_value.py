from pandas import isna


class RatingValue:
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
        "CC": 20,
        "C": 21,
        "D": 22,
        "무등급": 99,
    }

    moodys_to_sp_map = {
        "Aaa": "AAA",
        "Aa1": "AA+",
        "Aa2": "AA",
        "Aa3": "AA-",
        "A1": "A+",
        "A2": "A",
        "A3": "A-",
        "Baa1": "BBB+",
        "Baa2": "BBB",
        "Baa3": "BBB-",
        "Ba1": "BB+",
        "Ba2": "BB",
        "Ba3": "BB-",
        "B1": "B+",
        "B2": "B",
        "B3": "B-",
        "Caa1": "CCC+",
        "Caa2": "CCC",
        "Caa3": "CCC-",
        "Ca": "CC",
        "C": "C",
        "D": "D",
    }

    standardize_map = {
        "AA0": "AA",
        "BBB0": "BBB",
        "BB0": "BB",
        "B0": "B",
        "CCC0": "CCC",
        "CC0": "CC",
        "C0": "C",
        "D0": "D",
    }

    internal_rating_map = {
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
        "BB+": 10,
        "BB": 10,
        "BB-": 10,
        "B+": 10,
        "B": 10,
        "B-": 10,
        "CCC+": 10,
        "CCC": 10,
        "CCC-": 10,
        "CC": 10,
        "C": 10,
        "D": 10,
        "무등급": 99,
    }

    def __init__(self, **kwargs):
        def clean_value(value):
            if isna(value) or value == "":
                return None
            value = self.moodys_to_sp_map.get(value, value)  # Moody's 변환 적용
            return self.standardize_map.get(value, value)  # 표준화 변환 적용

        for key, value in kwargs.items():
            setattr(self, key, clean_value(value))

    def get_overall_rating(self):
        valid_ratings = []
        for attr, rating in self.__dict__.items():
            if rating in self.rank_map:
                valid_ratings.append(self.moodys_to_sp_map.get(rating, rating))
        return (
            max(valid_ratings, key=lambda x: self.rank_map[x])
            if valid_ratings
            else "무등급"
        )

    def __repr__(self) -> str:
        ratings = {k: v for k, v in self.__dict__.items() if v is not None}
        return f"RatingValue({ratings})"
