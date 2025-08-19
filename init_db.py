import io

import duckdb
import pandas as pd

con = duckdb .connect("data/exercises_sql_db.duckdb")

# --------------------------------------------------------

# EXERCISES LIST

# --------------------------------------------------------

data = {
    "theme" : ["cross joins","window functions"],
    "exercises_name" : ["beverages and food","simple window"],
    "tables" : [["beverages", "food"],"simple window"],
    "last_reviewed" : ["2023-01-01","2023-01-01"]
}
memory_state_df = pd.DataFrame(data)

con.execute("Create table if not exists memory_state as select * from memory_state_df")


# --------------------------------------------------------

# CROSS JOIN EXERCISES

# --------------------------------------------------------

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
