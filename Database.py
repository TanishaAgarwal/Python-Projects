import psycopg2

def createTable():
    conn = psycopg2.connect('dbname=Data user=postgres password=SK@1973m port=5432 host=127.0.0.1')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    cur.close()
    conn.close()

def insertData(roll, nam, mark):
    conn = psycopg2.connect('dbname=Data user=postgres password=SK@1973m port=5432 host=127.0.0.1')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)",(roll, nam, mark))
    conn.commit()
    cur.close()
    conn.close()


def viewData():
    conn = psycopg2.connect('dbname=Data user=postgres password=SK@1973m port=5432 host=127.0.0.1')
    cur = conn.cursor()
    cur.execute("SELECT * from data")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows

def deleteData(roll):
    conn = psycopg2.connect('dbname=Data user=postgres password=SK@1973m port=5432 host=127.0.0.1')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=%s",(roll,))
    conn.commit()
    cur.close()
    conn.close()

def updateData(roll, nam, mark):
    conn = psycopg2.connect('dbname=Data user=postgres password=SK@1973m port=5432 host=127.0.0.1')
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=%s, marks=%s WHERE rollno=%s",(nam, mark ,roll))
    conn.commit()
    cur.close()
    conn.close()

# deleteData(1)
# updateData(2,"Gungun",100)
print(viewData())