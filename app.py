import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))


with st.sidebar :
    option = st.selectbox(
        "What would you like to do?",
        {"Joins","Group by","Window Function"},
        index=None,
        placeholder="Select an option",
    )
    if option :
        st.write(option)

st.header(
"""
#SQL SRS
## SQL TRAINING APP
""")


answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.sql(answer).df()

st.header("Enter your code:")
query = st.text_input("Votre code SQL ici", key ="user_input")
if query:
    result = duckdb.query(query).df()
    st.dataframe(result)


tab1,tab2 = st.tabs(["tables","solution"])

with tab1 :
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab2 :
    st.write("query : answer")
    st.write(answer)
