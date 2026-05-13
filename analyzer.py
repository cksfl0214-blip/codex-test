import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> dict:
    """주요 GA4 지표를 계산해 딕셔너리로 반환합니다."""
    average_users = df["총 사용자"].mean()
    max_row = df.loc[df["총 사용자"].idxmax()]
    min_row = df.loc[df["총 사용자"].idxmin()]

    metrics = {
        "period_start": df["날짜"].min().date(),
        "period_end": df["날짜"].max().date(),
        "average_users": average_users,
        "total_users": df["총 사용자"].sum(),
        "total_new_users": df["새 사용자 수"].sum(),
        "total_sessions": df["세션수"].sum(),
        "total_views": df["조회수"].sum(),
        "average_views_per_session": df["세션당 조회수"].mean(),
        "average_session_time": df["평균 세션 시간"].mean(),
        "max_date": max_row["날짜"].date(),
        "max_users": max_row["총 사용자"],
        "min_date": min_row["날짜"].date(),
        "min_users": min_row["총 사용자"],
    }

    return metrics
