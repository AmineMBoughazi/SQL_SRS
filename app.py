# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

con = duckdb .connect("data/exercises_sql_db.duckdb",read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to do?",
        {"cross joins", "Group by", "Window Function"},
        index=None,
        placeholder="Select a theme",
    )
    if theme:
        st.write("you selected : ",theme)
    exercice = con.execute(f"select * from memory_state where theme = '{theme}'")
    st.write(exercice)

st.header(
    """
#SQL SRS
## SQL TRAINING APP
"""
)


#ANSWER_STRING = """
#SELECT * FROM beverages
#CROSS JOIN food_items
#"""
#solution_df = duckdb.sql(ANSWER_STRING).df()

st.header("Enter your code:")
query = st.text_input("Votre code SQL ici", key="user_input")
result = None  # pylint: disable=invalid-name
#
#if query:
#    result = duckdb.query(query).df()
#    st.dataframe(result)
#
#    try:
#        result = result[solution_df.columns]
#    except KeyError as e:
#        st.write("some columns are missing")
#
#if result.shape[0]:
#    n_lignes_different = result.shape[0] - solution_df.shape[0]
#
#    if n_lignes_different != 0:
#        st.write(f"there are {n_lignes_different} lines differences with the solution")
#    try:
#        st.dataframe(result.compare(solution_df))
#    except ValueError as e:
#        st.write("some columns are missing")
#
#tab1, tab2 = st.tabs(["tables", "solution"])
#
#with tab1:
#    st.write("table : beverages")
#    st.dataframe(beverages)
#    st.write("table : food_items")
#    st.dataframe(food_items)
#    st.write("expected")
#    st.dataframe(solution_df)
#
#with tab2:
#    st.write("query : answer")
#    st.write(ANSWER_STRING)
