# pylint: disable=missing-module-docstring
import ast
import io

import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect("data/exercises_sql_db.duckdb",read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to do?",
        {"cross joins", "Group by", "Window Function"},
        index=None,
        placeholder="Select a theme",
    )
    if theme:
        st.write("you selected : ",theme)
    exercise = con.execute(f"select * from memory_state where theme = '{theme}'").df()
    st.write(exercise)
    exercise_name = exercise.loc[0,"answer"]
    with open(f"answers/{exercise_name}","r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

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
#
st.header("Enter your code:")
query = st.text_input("Votre code SQL ici", key="user_input")
result = None  # pylint: disable=invalid-name

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
    except KeyError as e:
        st.write("some columns are missing")

    try:
        st.dataframe(result.compare(solution_df))
    except ValueError as e:
        st.write("some columns are missing")

tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    exercises_table = ast.literal_eval(exercise.loc[0,"tables"])
    for tables in exercises_table:
        st.write(f"table name : {tables}")
        tmp_tab = con.execute(f"select * from {tables}").df()
        st.dataframe(tmp_tab)

with tab2:
    st.write(answer)

