from bottle import request, run, route, post


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
            # TODO: Connect to the DB
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
            # TODO: Connect to the DB
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
    return ('hello update_user_location - {}, {}'.format(user_id, str(location)))

## Updates and reports to users




#####
# Backend


######
#
run(host='localhost', port=4261, reloader=True, debug=True)
