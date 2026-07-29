import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="글로벌 MBTI", page_icon="🌍")

st.title("🌍 주요 국가별 MBTI 비교")
st.write("한국, 미국, 일본 3개국의 주요 MBTI 유형별 분포 차이를 비교합니다.")

# 국가별 가상 비교 데이터 
data = {
    '국가': ['한국', '한국', '한국', '미국', '미국', '미국', '일본', '일본', '일본'],
    'MBTI': ['INFP', 'ESTJ', 'ISFJ', 'INFP', 'ESTJ', 'ISFJ', 'INFP', 'ESTJ', 'ISFJ'],
    '비율(%)': [13.4, 8.1, 8.4, 6.5, 13.8, 11.2, 16.4, 4.5, 8.9]
}

df = pd.DataFrame(data)

# 그룹 막대 그래프 생성
fig = px.bar(
    df, 
    x='MBTI', 
    y='비율(%)', 
    color='국가', 
    barmode='group',
    title="국가별 대표 MBTI 성향 비교 (INFP, ESTJ, ISFJ)",
    color_discrete_sequence=['#FF9999', '#66B2FF', '#99FF99']
)

fig.update_layout(xaxis_title="MBTI 유형", yaxis_title="비율 (%)")

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**📊 데이터 해석 포인트:**
* **한국 & 일본:** INFP 비율이 상대적으로 높게 나타납니다.
* **미국:** ESTJ, ISFJ 등 실용적이고 체계적인(SJ) 유형이 다수 분포하는 경향이 있습니다.
""")