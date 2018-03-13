import sqlite3

conn = sqlite3.connect('somedatabase.db')
curs = conn.cursor()
# curs.execute('''
# create table food(
# id text PRIMARY KEY ,
# water float,
# fat   float
# )
# ''')
# query = '''insert into food values(?,?,?)'''
# curs.execute(query,['a',1,4])
# curs.execute(query,['b',2,5])
# curs.execute(query,['c',3,6])
query1 = '''select * from food'''
print(query1)
curs.execute(query1)
for row in curs.fetchall():
    print(row)
    for i in zip(row):
        print('%s' % i)
conn.commit()
conn.close()