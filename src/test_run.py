import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import xlwings as xw
import pandas as pd

from product.bond import Bond, Bond_Info
from credit_rating.credit_rating import CreditRating


def main():
    # 현재 실행하는 스크립트의 위치 확인
    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.parent / "data/2024-09-12/W6644_채권.csv"
    wb = xw.Book(file_path)

    rd = (
        wb.sheets[0]
        .range("A1")
        .options(pd.DataFrame, index=False, header=True, expand="table")
        .value
    )

    for index, row in rd.iterrows():

        bond_info = Bond_Info(
            bond_type="원화채권",
            name=row["종목명"],
            crncy="KRW",
            issue_date=row["발행일자"],
            maturity_date=row["만기일자"],
            coupon_method=row["이자지급방법"],
            coupon_rate=(row["표면이율"] / 100),
            coupon_cycle=None,
            issure=None,
            issure_type=None,
            issure_country=None,
        )

        cr = CreditRating(
            kis=row["신용등급KIS"],
            kap=row["신용등급KBP"],
            nice=row["신용등급NIC"],
            fnp=row["신용등급FNP"],
        )

        div_code = str(int(row["부서코드"])).zfill(5)
        fund_code = str(int(row["펀드코드"]))
        this_bond = Bond(div_code, fund_code, "채권", row["종목번호"], bond_info, cr)

    return None


if __name__ == "__main__":
    main()
