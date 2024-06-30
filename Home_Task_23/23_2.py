import psycopg2
import pandas as pd
con = psycopg2.connect(
    database = 'postgres',
    user='postgres',
    password =                                                                                                                       '2001',
    host = '127.0.0.1',
    port = '5432'
)
cur = con.cursor()
cur.execute('''SELECT * from book11''')
lst = []
for i in cur:
    lst.append(list(i))

df = pd.DataFrame(lst)

cur.execute('''SELECT column_name
FROM information_schema.columns 
WHERE table_name = 'book11'
order by ordinal_position''')
lst_ind = [i[0] for i in cur]

df.columns = lst_ind
print(df)

con.close()