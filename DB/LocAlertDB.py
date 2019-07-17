import pymysql

try:
    cur.execute("CREATE database localert;")
except pymysql.err.ProgrammingError:
    cur.execute("DROP database localert;")
    cur.execute("CREATE database localert;")
finally:
    cur.execute("USE localert;")