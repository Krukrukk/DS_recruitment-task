import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('data/descriptive.csv', sep=';', decimal=',', index_col='id')
df_signal = pd.read_csv('data/signal.csv', sep=';', index_col='id')
df['y'] = df_signal['y']


profile = ProfileReport(df,
                        title="Descriptive Data",
                        correlations={
                                        "pearson": {"calculate": True},
                                        "spearman": {"calculate": False},
                                        "kendall": {"calculate": False},
                                        "phi_k": {"calculate": False}},
                        minimal=True
                        )

st.title("Pandas Profiling")
st.header("Data: data/descriptive.csv")
st.write(df)

st_profile_report(profile)