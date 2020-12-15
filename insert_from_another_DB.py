from DB import *
from tablenames import tableNames
columnlist = []
for tableName in tableNames:
    #skipping auto increment
    not_a_i = ("SELECT column_Name,column_default FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+tableName+ "' AND column_default is null")
    DB1.execute(not_a_i)
    val = DB1.fetchall()
    for v in val:
        columnlist.append(v[0])

    #destination
    DB2.execute("select MAX(id) from "+tableName)
    #source
    #DB1.execute("select MAX(id) from "+tableName)

    #retrieving column name from tables of source database 
    ##########################
    # query = ("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= '%s'" %tableName )
    # DB1.execute(query)
    # columns = DB1.fetchall()
    # for column in columns:
    #     if column[3] == 'id':
    #         continue       #as id is autoincremental, not addiddig it to the list
    #     else:
    #         columnlist.append(column[3])   
    ##########################
    destination_table_max_id = DB2.fetchone()[0] 
    print(destination_table_max_id)
    tuple(columnlist)
    if destination_table_max_id is None :
        DB1.execute("SELECT * from "+ tableName)
        rows = DB1.fetchall()
        print(rows)
   
        for row in rows:
            new_row = list(row)
            new_row.pop(0)
            new_row_values = tuple(new_row)
            print(new_row_values)
            #DB2.execute("INSERT INTO "+ tableName +" ( " + columnlist[0] + "," + columnlist[1] +") values('%s','%s');" %new_row_values)
            DB2.execute("INSERT INTO "+ tableName +" ( " + ",".join(columnlist) +") values("+",".join("'"+str(i)+"'" for i in new_row_values)+");")
            postgres.commit()
    elif destination_table_max_id is not None:
        DB1.execute("SELECT * from "+ tableName + " where id > "+ str(destination_table_max_id))
        rows = DB1.fetchall()
        print(rows)
        
        for row in rows:
            new_row = list(row)
            new_row.pop(0)
            new_row_values = tuple(new_row)
            print(new_row_values)
#            DB2.execute("INSERT INTO "+ tableName +" ( " + columnlist[0] + "," + columnlist[1] +") values('%s','%s');" %new_row_values)
            #dynamically inserting into table by checking extra values
            DB2.execute("INSERT INTO "+ tableName +" ( " + ",".join(columnlist) +") values("+",".join("'"+str(i)+"'" for i in new_row_values)+");")

            postgres.commit()

        

    list(columnlist)
    columnlist.clear()   
    



