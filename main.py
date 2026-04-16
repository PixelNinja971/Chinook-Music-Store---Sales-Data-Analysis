import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt
from utils import REQUETE_TOP_VENTES, REQUETE_PAYS, REQUETE_EMPLOYEE



con = sqlite3.connect("Chinook.sqlite")
cur = con.cursor()

# Je veux les ventes ? J'appelle juste ça :
df = pd.read_sql_query(REQUETE_TOP_VENTES, con)


# Je veux les pays ? Je change juste la variable :
# df = pd.read_sql_query(REQUETE_PAYS, con)

# Je veux les employer ? Je change juste la variable :
# df = pd.read_sql_query(REQUETE_EMPLOYEE, con)

df.plot.bar(x='Name', y='total_ventes' title="Top 10 des ventes par chanson");
plt.show()



print(DataFrame)