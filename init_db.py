import io

import duckdb
import pandas as pd

con = duckdb .connect("data/exercises_sql_db.duckdb")

# --------------------------------------------------------

# EXERCISES LIST

# --------------------------------------------------------

data = {
    "theme" : ["cross joins","cross joins"],
    "exercises_name" : ["beverages and food","trademarks and sizes"],
    "tables" : [["beverages", "food_items"],["sizes", "trademarks"]],
    "last_reviewed" : ["2023-01-02","2023-01-01"],
    "answer" : ["beverages_and_food.sql",'trademarks_and_sizes.sql']
}
memory_state_df = pd.DataFrame(data)

con.execute("Create table if not exists memory_state as select * from memory_state_df")


# --------------------------------------------------------

# CROSS JOIN EXERCISES

# --------------------------------------------------------


#Exercice 1 Food and beverages
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

con.execute("Create table if not exists beverages as select * from beverages ")

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

con.execute("Create table if not exists food_items as select * from food_items ")

#Exercise 2 sizes and trademarks
sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("Create table if not exists sizes as select * from sizes ")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Levis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("Create table if not exists trademarks as select * from trademarks ")