from bottle import request, run, route, post, get

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
    get_user_location_from_database(userid)
    return('in get_user_location - userid: {}'.format(userid))
# Get group alerts
# Get nearby reports

@get('/get_nearby_reports<positionId>')
def get_nearby_reports(positionId):
    print("in get_nearby_reports positionId: {}".format(positionId))
    get_nearby_reports_from_database(positionId)
    return print("in get_nearby_reports positionId: {}".format(positionId))


# Set / Update / Insert / Delete


#####
# DB
def get_user_location_from_database(userid):
    print('in get_user_location_from_database(userid): {}'.format(userid))
    # TODO: DB connection code
    location = {'234','6476'}
    return location
def get_nearby_reports_from_database(positionId):
    print("in get_nearby_reports_from_database positionId: {}".format(positionId))
    # TODO: DB connection code
    reports_data  = "reports"
    return reports_data

# Todo: implement database connectivity - select, insert, update, delete
# Create User (insert)
# Create Group (insert)
#
# Report Issue by User (insert)
# Alert sent by user (insert)
# Update user location

######
# Server run

run(host='localhost', port=4261, reloader=True, debug=True)
