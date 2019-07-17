from bottle import request, run, route, post


# Frontend

@route('/')
def homepage():
    print('hellllloooo nurse')
    return 'hellllloooo nurse'


# Update location
@post('/update_user_location')
def update_user_location():
    print('hello update_user_location')
    return ('hello update_user_location')


# Report Issue
@post('/create_user_report')
def create_user_report():
    print('hello create_user_report')
    return ('hello create_user_report')


# Alert
@post('/create_user_report')
def update_user_location():
    print('hello update_user_location')
    return ('hello update_user_location')

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
    return ('hello create_user_group - {}, members: {}'.format(user_group_name,user_group_members))


#####
# Backend


######
#
run(host='localhost', port=4261, reloader=True, debug=True)
