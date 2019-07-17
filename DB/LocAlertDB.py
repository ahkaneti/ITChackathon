import pymysql

def get_sql_from_file(filename):
    """
    Get the SQL instruction from a file

    :return: a list of each SQL query whithout the trailing ";"
    """
    with open(filename, "r") as sql_file:
        # Split file in list
        ret = sql_file.read().split(';')
        # drop last empty entry
        ret.pop()
        return ret

request_list = get_sql_from_file("sql/LocAlert.sql")
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root')
cur = conn.cursor()

try:
    cur.execute("CREATE database localert;")
except pymysql.err.ProgrammingError:
    cur.execute("DROP database localert;")
    cur.execute("CREATE database localert;")
finally:
    cur.execute("USE localert;")


for request in request_list:
    cur.execute(request)
cur.close()