import time

username = 'Jweb'
password = 'wonderland'

username_input = input('username: ')
password_input = input('password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('please wait')
    time.sleep(5)
    print('ok ...loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')

    print('Alright, you logged-in successfully')

elif username_input == username and password_input != password:
    print('Incorrect password, try again')
elif username_input != username and password_input == password:
    print('Incorrect username, try again')

else:
    print('You may want to check both fields')
