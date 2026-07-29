import streamlit as st

st.set_page_config(page_title="MBTI 데이터 대시보드", page_icon="📊")

st.title("📊 MBTI 데이터 대시보드 메인")
st.write("""
왼쪽 사이드바의 메뉴를 클릭하여 페이지를 이동해 보세요!
- **1번 페이지**: 우리나라 MBTI 비율
- **2번 페이지**: 나라별 MBTI 분포도
- **3번 페이지**: MBTI별 과학자 유형 및 탐구 스타일 (추천)
""")