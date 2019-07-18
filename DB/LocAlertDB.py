import pymysql
import csv
import os

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

request_list = get_sql_from_file("LocAlert.sql")
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='nacabiedargent')
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
#cur.close()

def filling_report(filename):


    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                values = [row["report_kind"], row["report_name"], row["report_description"], row["radius_dist"]]
                cur.execute(
                    "INSERT INTO Report_Kinds(report_kind, report_name, report_description, radius_dist) VALUES (%s, %s, %s, %s)",
                    values)
        conn.commit()


def filling_users(filename):
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                values = [row["user_id"], row["user_name"], row["email"], row["address"], row['phone_numbers']]
                cur.execute(
                    "INSERT INTO Users(user_id, user_name, email, address, phone_numbers) VALUES (%s, %s, %s, %s, %s)",
                    values)
        conn.commit()


filling_report('report_kinds.csv')
filling_users('users.csv')

cur.close()






