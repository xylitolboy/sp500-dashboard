import streamlit as st
import FinanceDataReader as fdr
import datetime
import pyupbit

st.set_page_config(layout="wide")
st.title("📈 실시간 금융 대시보드: S&P500, Bitcoin, Magnificent 7")

start_date = datetime.date(2010, 1, 1)

# 📊 S&P500
st.subheader("📊 S&P500 (미국 지수)")
snp_df = fdr.DataReader("^GSPC", start_date)
snp_df['MA20'] = snp_df['Close'].rolling(window=20).mean()
snp_df['MA50'] = snp_df['Close'].rolling(window=50).mean()
st.line_chart(snp_df[['Close', 'MA20', 'MA50']])

# 💰 Bitcoin
st.subheader("💰 Bitcoin (KRW)")
btc_df = pyupbit.get_ohlcv("KRW-BTC")
btc_df['MA20'] = btc_df['close'].rolling(window=20).mean()
btc_df['MA50'] = btc_df['close'].rolling(window=50).mean()
btc_df.rename(columns={"close": "Close"}, inplace=True)
st.line_chart(btc_df[['Close', 'MA20', 'MA50']])

# 🌟 Magnificent 7
st.subheader("🌟 Magnificent 7 (전 종목)")
magnificent_7 = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "AMZN": "Amazon",
    "NVDA": "NVIDIA",
    "GOOGL": "Google",
    "META": "Meta",
    "TSLA": "Tesla"
}

for ticker, name in magnificent_7.items():
    st.markdown(f"#### {name} ({ticker})")
    try:
        df = fdr.DataReader(ticker, start_date)
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        st.line_chart(df[['Close', 'MA20', 'MA50']])
    except Exception as e:
        st.warning(f"{name} 데이터 로드 실패: {e}")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

