import streamlit as st
import pandas as pd

st.title("English Vocabulary Tracker")

df = pd.read_csv('data/student_vocab_records.csv')
st.line_chart(df.pivot(index='date', columns='student_name', values='total_words_mastered'))
