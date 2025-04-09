import streamlit as st
import FinanceDataReader as fdr
import datetime

st.set_page_config(layout="wide")
st.title("📈 S&P500 & 이동평균선 차트")

start_date = st.date_input("조회 시작일", value=datetime.date(2010, 1, 1))
code = st.text_input("종목 코드 (예: 005930, 360750)", value="360750")

if code:
    df = fdr.DataReader(code, start_date)
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    st.line_chart(df[['Close', 'MA20', 'MA50']])
