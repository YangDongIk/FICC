import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import xlwings as xw
import pandas as pd

from src.bond import Bond


def main():
    wb = xw.Book("data/2024-09-12/W6644_채권.csv")

    rd = (
        wb.sheets[0]
        .range("A1")
        .options(pd.DataFrame, index=False, header=True, expand="table")
        .value
    )

    for index, row in rd.iterrows():
        x = Bond(
            "원화채권",
            row["종목번호"],
            row["종목명"],
            row["수량"],
            "KRW",
            row["발행일자"],
            row["만기일자"],
        )

    return None


if __name__ == "__main__":
    main()
