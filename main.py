import sys
import pandas as pd


def main():
    if len(sys.argv) < 2:
        print("사용법: python main.py data/user_data_cclibrary.csv")
        return

    csv_path = sys.argv[1]

    # GA4 CSV 파일은 위쪽 9줄이 설명 영역이고, 10번째 줄부터 실제 표가 시작됨
    df = pd.read_csv(csv_path, skiprows=9, encoding="utf-8")

    # 날짜 컬럼 변환: 20251201 -> 2025-12-01
    df["날짜"] = pd.to_datetime(df["날짜"].astype(str), format="%Y%m%d")

    average_users = df["총 사용자"].mean()
    max_row = df.loc[df["총 사용자"].idxmax()]
    min_row = df.loc[df["총 사용자"].idxmin()]

    total_users = df["총 사용자"].sum()
    total_new_users = df["새 사용자 수"].sum()
    total_sessions = df["세션수"].sum()
    total_views = df["조회수"].sum()

    average_views_per_session = df["세션당 조회수"].mean()
    average_session_time = df["평균 세션 시간"].mean()

    print("춘천시립도서관 GA4 트래픽 요약")
    print("--------------------------------")
    print(f"분석 기간: {df['날짜'].min().date()} ~ {df['날짜'].max().date()}")
    print(f"일 평균 총 사용자 수: {average_users:.0f}명")
    print(f"총 사용자 수 합계: {total_users:,}명")
    print(f"새 사용자 수 합계: {total_new_users:,}명")
    print(f"세션 수 합계: {total_sessions:,}회")
    print(f"조회수 합계: {total_views:,}회")
    print(f"평균 세션당 조회수: {average_views_per_session:.2f}회")
    print(f"평균 세션 시간: {average_session_time:.1f}초")
    print()
    print(f"가장 사용자가 많은 날: {max_row['날짜'].date()} / {max_row['총 사용자']:,}명")
    print(f"가장 사용자가 적은 날: {min_row['날짜'].date()} / {min_row['총 사용자']:,}명")


if __name__ == "__main__":
    main()