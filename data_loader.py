import pandas as pd


def load_ga4_csv(csv_path: str) -> pd.DataFrame:
    """GA4 CSV 파일을 읽고 날짜 컬럼을 datetime으로 변환합니다."""
    # GA4 CSV 파일은 위쪽 9줄이 설명 영역이고, 10번째 줄부터 실제 표가 시작됨
    df = pd.read_csv(csv_path, skiprows=9, encoding="utf-8")

    # 날짜 컬럼 변환: 20251201 -> 2025-12-01
    df["날짜"] = pd.to_datetime(df["날짜"].astype(str), format="%Y%m%d")
    return df
