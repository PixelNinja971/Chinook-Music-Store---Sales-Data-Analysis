import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt



con = sqlite3.connect("Chinook.sqlite")
cur = con.cursor()
ma_requete_top_sale = """

    SELECT track.Name , sum (invoiceline.Quantity) AS total_ventes
    FROM track
    INNER JOIN invoiceline ON track.trackId = invoiceline.trackId
    Group by track.Name
    order by total_ventes desc
    Limit 10
"""
df = pd.read_sql_query(ma_requete_top_sale, con)

df.plot.bar(x='Name', y='total_ventes' title="Top 10 des ventes par chanson");
plt.show()



print(DataFrame)