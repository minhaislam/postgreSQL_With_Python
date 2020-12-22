from DB import DB4, dvdrental

try:
    DB4.execute('''CREATE INDEX rental_ids ON rental (rental_id);''')

    dvdrental.commit()

    print('btree index created')
except:
    print('failed')
