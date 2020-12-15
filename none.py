from DB import *
from commands import Source_table_DDL
from tablenames import tableNames, destination_tableNames
columnlist = []

for table in tableNames:
    if table not in destination_tableNames:
        for key in Source_table_DDL:
            if(table == key):
                print(Source_table_DDL[key])

for tableName in tableNames:
    #auto_increment = ("SELECT column_Name,column_default FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+tableName+ "' AND column_default ='nextval(''%s_id_seq''::regclass)'" %tableName)
    #auto_increment = ("SELECT column_Name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" %tableName)
    not_a_i = ("SELECT column_Name,column_default FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+tableName+ "' AND column_default is null")
    DB1.execute(not_a_i)
    val = DB1.fetchall()
    for v in val:
        print(v[0])
    #print(val)

