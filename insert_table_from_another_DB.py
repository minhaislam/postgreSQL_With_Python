from DB import *
from commands import Source_table_DDL
from tablenames import tableNames,destination_tableNames

for table in tableNames:
    if table not in destination_tableNames:
        for key in Source_table_DDL:
            if(table == key):
                DB2.execute(Source_table_DDL[key])
                postgres.commit()
                print("Imported succesfully")
                   

        


