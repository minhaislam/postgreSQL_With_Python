from DB import *

DB1.execute('''SELECT table_name
  FROM information_schema.tables
 WHERE table_schema='public'
   AND table_type='BASE TABLE';''')

#source
tableNames = []

db_tables1 = DB1.fetchall()
#table_name
for tablesName in db_tables1:
    tableNames.append(tablesName[0])
print(tableNames)
#count =0
#print(db_tables1)
#print(result)

#destination
DB2.execute('''SELECT table_name
  FROM information_schema.tables
 WHERE table_schema='public'
   AND table_type='BASE TABLE';''')


destination_tableNames = []

db_tables1 = DB2.fetchall()
#table_name
for des_tablesName in db_tables1:
    destination_tableNames.append(des_tablesName[0])
print(destination_tableNames)
