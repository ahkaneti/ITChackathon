from bottle import run, route, post


# Frontend

@route('/')
def homepage():
    print('hellllloooo nurse')
    return 'hellllloooo nurse'



# Update location
@post('/update_user_location')
def update_user_location():
    print('hello update_user_location')
    return('hello update_user_location')


# Report
@post('/create_user_report')
def create_user_report():
    print('hello create_user_report')
    return('hello create_user_report')


# Alert
@post('/create_user_report')
def update_user_location():
    print('hello update_user_location')
    return('hello update_user_location')


# Backend


run(host='localhost', port=4261, reloader=True, debug=True)
