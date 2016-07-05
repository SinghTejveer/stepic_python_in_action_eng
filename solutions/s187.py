"""
You have login and password as integer numbers stored in the code as login and
password variables. The user inputs two integers (the login and the password).
If they match to one in the code - output "Login success", if the password
doesn't match, but logins match, output "Wrong password", if login is wrong,
output "No user with login XXXX found", where XXXX is the login, the user's
just input.

INPUT

Two integers, the first - login, the second - password.

OUTPUT

"Login success" if both match, "Wrong password" if passwords do not match, but
logins match and "No user with login XXXX found" if logins do not match (XXXX
is the login, the user has input).
"""

LOGIN = '100500'
PASSWORD = '424242'


def main():
    login, password = input().rstrip().split()
    if login != LOGIN:
        print('No user with login %s found' % login)
    elif password != PASSWORD:
        print('Wrong password')
    else:
        print('Login success')

if __name__ == '__main__':
    main()
