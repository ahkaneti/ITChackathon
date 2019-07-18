from bottle import request, run, route, post, get
import datetime
import pymysql

# Frontend

@route('/')
def homepage():
    print('hellllloooo nurse')
    return 'hellllloooo nurse'


## Creation

# Create User
@post('/create_user')
def create_user():
    print('hello create_user')
    try:
        user_first_name = request.forms.get('user_first_name')
        user_last_name = request.forms.get('user_last_name')
    except:
        print('got no data')
    else:
        if user_first_name is not None:
            print(user_first_name)
            print(user_last_name)
            # TODO: Connect to the DB - return userid
    return ('hello create_user - {} {}'.format(user_first_name, user_last_name))


# Create Group
@post('/create_user_group')
def create_user_group():
    print('hello create_user_group')
    try:
        user_group_name = request.forms.get('user_group_name')
        user_group_members = request.forms.get('user_group_members')
    except:
        print('got no data')
    else:
        if user_group_name is not None:
            print(user_group_name)
            print(user_group_members)
            # TODO: Connect to the DB - return group id
    return ('hello create_user_group - {}, members: {}'.format(user_group_name, user_group_members))


## Updates and reports from users

# Update user location
@post('/update_user_location')
def update_user_location():
    print('hello update_user_location')
    try:
        user_id = request.forms.get('user_id')
        location = request.forms.get('location')
    except:
        print('got no data')
    else:
        if user_id is not None:
            print(user_id)
            print(location)
            # TODO: Connect to the DB
    return ('hello update_user_location - {} {}'.format(user_id, str(location)))


# Report Issue by User
@post('/create_user_report')
def create_user_report():
    print('hello create_user_report')
    try:
        user_id = request.forms.get('user_id')
        location = request.forms.get('location')
        report = request.forms.get('report')
    except:
        print('got no data')
    else:
        if user_id is not None:
            print(user_id)
            print(location)
            print(report)
            # TODO: Connect to the DB
    return ('hello create_user_report - {}, {}, {}'.format(user_id, str(location), report))


# Alert sent by user
@post('/alert_sent_by_user')
def alert_sent_by_user():
    print('hello alert_sent_by_user')
    try:
        user_id = request.forms.get('user_id')
        location = request.forms.get('location')
    except:
        print('got no data')
    else:
        if user_id is not None:
            print(user_id)
            print(location)
            # TODO: Connect to the DB
    return ('hello alert_sent_by_user - {}, {}'.format(user_id, str(location)))


#
# # Update user location
# @post('/update_user_location')
# def update_user_location():
#     print('hello update_user_location')
#     try:
#         user_id = request.forms.get('user_id')
#         location = request.forms.get('location')
#     except:
#         print('got no data')
#     else:
#         if user_id is not None:
#             print(user_id)
#             print(location)
#             # TODO: Connect to the DB
#     return ('hello update_user_location - {}, {}'.format(user_id, str(location)))


#####
# Backend
## Updates and reports to users

# Todo: implement get routes and methods
# Get / Selects
# Get user location
@get('/get_user_location/<userid>')
def get_user_location(userid):
    print('in get_user_location - userid: {}'.format(userid))
    location = get_user_location_from_database(userid)
    return ('in get_user_location - userid: {}, location: {}'.format(userid,location))


# Get group alerts
""" 
    This endpoint is polled by the client.
    If there is an alert by a group member the mothod returns: userid, location
"""
@get('/get_group_location/<groupid>')
def get_user_location(groupid):
    print('in get_group_location - groupid: {}'.format(groupid))
    update = get_group_updates_from_database(groupid)
    return ('in get_group_location - groupid: {}, update: {}'.format(groupid, update))

# Get nearby reports

@get('/get_nearby_reports/<positionId>')
def get_nearby_reports(positionId):
    print("in get_nearby_reports positionId: {}".format(positionId))
    reports = get_nearby_reports_from_database(positionId)
    return reports


# Set / Update / Insert / Delete


#####
# DB
# Connection setup
# Setting connection parameters
host='127.0.0.1'
user='root'
password='i326849775'

# Creating a general connection
conn = None

# Methods

# Create global connection
# Updates the global conn variable
# Returns a cursor ?
def create_global_db_connection():
    global conn
    try:
        conn = pymysql.connect(host=host, user=user, password=password)
        if(conn):
            print('DB connection successful')
    except:
        print('DB CONNECTION FAIL')
#
def check_db_connection():
    try:
        if(conn):
            print('DB is connected')
    except:
        print('DB is not connected')

#
def get_user_location_from_database(userid):
    print('in get_user_location_from_database(userid): {}'.format(userid))
    # TODO: DB connection code
    location = {'234', '6476'}
    return location

def get_nearby_reports_from_database(positionId):
    print("in get_nearby_reports_from_database positionId: {}".format(positionId))
    try:
        with conn.cursor() as curr:
            sql_query = 'SELECT report_date FROM localert.reports WHERE position_id={}'.format(positionId)
            print('sql_query: {}'.format(sql_query))
            curr.execute(sql_query)
            report_data = curr.fetchall()
            print('position_data: {}'.format(report_data))
        conn.commit()
        return report_data
    except:
        print('error getting the user from the database')

""" 
    This DB method is used by the get_group_location method.
    It receives a groupid.
    If there is an alert by a group member the mothod returns: userid, location
    In order to check if there is an alert it needs to join the tables: user_groups, alerts, on userid 
    where the groupid is equal to the received groupid. 
"""
def get_group_updates_from_database(groupid):
    print('in get_group_updates_from_database(groupid): {}'.format(groupid))
    # TODO: DB connection code
    # TODO: Create get group members method, use that to join on the alerts table
    # conn = pymysql.connect(host='127.0.0.1', user='root', password='zaq1zaq')
    # cur = conn.cursor()
    # join
    # cur.execute('SELECT * FROM user_groups LEFT JOIN alerts ON ')
    # temporary mock return value:
    group_updates = [{'update_id': 'some id', 'update_content': 'some updates'}]
    return group_updates
# add , get_group_updates endpoint and methods

# Auxiliary methods
# Get User from database
def get_user_from_database(userid):
    print('in get_user_from_database, userid: {}'.format(userid))
    try:
        with conn.cursor() as curr:
            sql_query = 'SELECT * FROM localert.users WHERE user_id={}'.format(userid)
            # sql_query = 'select * from localert.users;'
            print('sql_query: {}'.format(sql_query))
            curr.execute(sql_query)
            print('post curr exed')
            user = curr.fetchall()
            print('user: {}'.format(str(user)))
        conn.commit()
    except:
        print('error getting the user from the database')
    finally:
        print('in get_user_from_database - finally')
#
#     pass
# Get Group from database
# Get Group Members from database
#
# Todo: implement database connectivity - select, insert, update, delete
# Create User (insert)
def create_user(user_details):
    print(user_details)
    with conn.cursor() as curr:
        sql_query = 'INSERT INTO users (user_name,email,address,phone_numbers) VALUES({},{},{},{})'\
            .format(user_details.user_name,user_details.user_email,user_details.user_address,user_details.user_phone_numbers)
        curr.execute(sql_query)
        print('executed query: ' + sql_query)

        get_id_statement = 'LAST_INSERT_ID()'
        userid = curr.execute(get_id_statement)
        print(userid)


    #         user = curr.fetchone()
    #         print('user: {}'.format(user))
    # Get inserted id
    # with conn.curser() as curr:
        # userid = LAST_INSERT_ID()
# Create Group (insert)
#
# Report Issue by User (insert)
# Alert sent by user (insert)
# Update user location



###########
# Logic

# TODO:
# Monitor user movement in relation to the designated route
# Notify group members on route completion
# Alert the police
#







######
# Server run
if __name__ == '__main__':
    print('when running the server with reloader=True the server will be started twice: http://bottlepy.org/docs/dev/tutorial.html#auto-reloading')
    print('therefore these startap messages will show twice')
    print('server starting in main on {}'.format(datetime.datetime.now()))
    create_global_db_connection()
    check_db_connection()
    # test stuff
    get_user_from_database(2)
    # create_user('fasdf')
    run(host='localhost', port=4261, reloader=True, debug=True)
