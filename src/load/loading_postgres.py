from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://basel:baselnabil@localhost:5432/python_etl')

df = pd.read_csv('/home/basel/basel/python_Etl/src/load/data1.csv')


# Write DataFrame to PostgreSQL table
df.to_sql('vaccine_stats', engine, if_exists='replace', index=False)
