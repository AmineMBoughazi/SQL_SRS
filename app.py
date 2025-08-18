import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world")

data = {"a" : [1,2,3], "b" : [4,5,6]}
df = pd.DataFrame(data)

tab1,tab2 = st.tabs(["SQL interpreter","SQL exercice"])

with tab1 :
    input_text = st.text_area(label = "Input your SQL query")
    st.dataframe(df)
    if input_text :
        try :
            user_query_df = duckdb.sql(input_text).df()
            st.dataframe(user_query_df)
        except (ValueError,duckdb.duckdb.ParserException) as e :
            st.write("Votre query n'est pas valide")
            st.write(e)
