from credit_rating.rating_value import RatingValue


class ExternalRating:
    def __init__(self, **kwargs):
        domestic_keys = {"kis", "kap", "nice", "fnp"}
        foreign_keys = {"moodys", "snp", "fitch"}

        domestic_ratings = {k: v for k, v in kwargs.items() if k in domestic_keys}
        foreign_ratings = {k: v for k, v in kwargs.items() if k in foreign_keys}

        self.domestic = RatingValue(**domestic_ratings) if domestic_ratings else None
        self.foreign = RatingValue(**foreign_ratings) if foreign_ratings else None

    @property
    def value(self):
        if self.domestic and (domestic_rating := self.domestic.get_overall_rating()):
            return domestic_rating
        if self.foreign and (foreign_rating := self.foreign.get_overall_rating()):
            return foreign_rating
        return "무등급"

    def __repr__(self):
        return f"ExternalRating(domestic={self.domestic}, foreign={self.foreign})"
