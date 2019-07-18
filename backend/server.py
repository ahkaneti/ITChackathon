from bottle import request, run, route, post, get

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
    return ('in get_user_location - userid: {}'.format(userid))


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
    return ("in get_nearby_reports positionId -positionId: {}, reports: {}".format(positionId,reports))


# Set / Update / Insert / Delete


#####
# DB

# Auxiliary methods
# Get User from database
# Get Group from database
# Get Group Members from database
# 


# Methods
def get_user_location_from_database(userid):
    print('in get_user_location_from_database(userid): {}'.format(userid))
    # TODO: DB connection code
    location = {'234', '6476'}
    return location

def get_nearby_reports_from_database(positionId):
    print("in get_nearby_reports_from_database positionId: {}".format(positionId))
    # TODO: DB connection code
    reports_data  ="reports"
    return reports_data

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
# add pymysql, get_group_updates endpoint and methods

# Todo: implement database connectivity - select, insert, update, delete
# Create User (insert)
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

run(host='localhost', port=4261, reloader=True, debug=True)
