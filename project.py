import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pyodbc

# connection to database
db_path = r"C:\Users\GILBERT FG\Desktop\Readings\PSP_database.accdb"
query = r"SELECT * FROM TreeData WHERE AreaType = 'Teak' AND Plantations = 'Tain II' AND [Monitoring year] = 2022.0"

def db_connection(db_string):
    conn = pyodbc.connect(
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            rf"DBQ={db_string};"
        )

    return conn

def display_db_table_names(conn):
    cursor = conn.cursor()
    
    print("\n====== LIST OF TABLES ==========\n")

    for table in cursor.tables(tableType='TABLE'):
        print(table.table_name)

    print("\n====== END TO TABLE NAMES ========")


def query_table(pd, query, conn):
    df = pd.read_sql(query, conn)

    return df

def table_snapshot(df):

    # data information
    df.info()




conn = db_connection(db_path)

display_db_table_names(conn)

df = query_table(pd, query, conn)

table_snapshot(df)



