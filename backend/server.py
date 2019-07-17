from bottle import run, post

# Frontend

# Update location
@post('/update_user_location')
def update_user_location():
    print('hello update_user_location')

# Report
@post('/create_user_report')
def create_user_report():
    print('hello create_user_report')

# Alert
@post('/create_user_report')
def update_user_location():
    print('hello update_user_location')

# Backend



run(host='localhost',port=4261,reloader=True,debug=True)







