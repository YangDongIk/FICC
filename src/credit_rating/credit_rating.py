from credit_rating.external_rating import ExternalRating
from credit_rating.rating_value import RatingValue


class CreditRating:
    def __init__(self, internal=None, **kwargs):
        self.external_rating = ExternalRating(**kwargs)
        if internal:
            self.internal_rating = internal
        else:
            # 자동 매핑 적용
            overall_exteranl = self.external_rating.value
            self.internal_rating = RatingValue.internal_rating_map.get(
                overall_exteranl, "무등급"
            )

    def __repr__(self):
        return f"CreditRating(external_rating={self.external_rating}, internal_rating={self.internal_rating})"
