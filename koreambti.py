import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="한국 MBTI 비율", page_icon="🇰🇷")

st.title("🇰🇷 우리나라 MBTI 분포도")
st.write("한국인에게 가장 많이 나타나는 MBTI 비율을 그래프로 확인해 보세요.")

# 한국 MBTI 대략적 통계 데이터 (예시 데이터)
data = {
    'MBTI': ['INFP', 'ENFP', 'ESFJ', 'ISFJ', 'ISFP', 'ESTJ', 'INFJ', 'ENFJ', 'ISTJ', 'ESTP', 'INTP', 'ENTP', 'ISTP', 'ESFP', 'ENTJ', 'INTJ'],
    '비율(%)': [13.4, 12.6, 9.0, 8.4, 8.2, 8.1, 6.8, 6.1, 5.7, 5.0, 4.3, 3.8, 3.2, 2.9, 1.8, 0.7]
}

df = pd.DataFrame(data)

# 막대 그래프 생성
fig = px.bar(
    df, 
    x='MBTI', 
    y='비율(%)', 
    text='비율(%)',
    color='MBTI',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="한국인의 MBTI 비율 순위"
)

fig.update_traces(textposition='outside')
fig.update_layout(xaxis_title="MBTI 유형", yaxis_title="비율 (%)", showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.info("💡 **참고:** INFP와 ENFP 등 직관적이고 감정적인(NF) 성향이 상위권을 차지하는 특징이 있습니다.")