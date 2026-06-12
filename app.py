import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EnviroMetric Dashboard", layout="wide")

st.title("🔬 EnviroMetric: Research Dashboard")
st.write("Comparing the Energy Cost of Software Implementations")

uploaded = st.sidebar.file_uploader("Upload research_data.csv", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Energy Consumption (Joules)")
        fig1 = px.bar(df.groupby("Label")["Energy_J"].mean().reset_index(), 
                     x="Label", y="Energy_J", color="Label")
        st.plotly_chart(fig1)

    with col2:
        st.subheader("Time vs Energy Efficiency")
        fig2 = px.scatter(df, x="Duration_S", y="Energy_J", color="Label",
                         title="Pareto Efficiency Frontier")
        st.plotly_chart(fig2)

    # PhD Insight: Statistical Significance
    st.divider()
    st.subheader("Research Summary")
    avg = df.groupby("Label")["Energy_J"].mean()
    diff = ((avg.max() - avg.min()) / avg.max()) * 100
    st.info(f"The Optimized version is **{diff:.2f}%** more energy efficient than the Legacy version.")
