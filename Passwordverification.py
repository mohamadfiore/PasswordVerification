test = 0
PASSWORD_LENGHT = 8

def passwordChcek (str):
    if len(str) >= PASSWORD_LENGHT:
        return True
    else:
        return False

while test == 0:

    # ask for the user input
    password = input('Enter your password:')

    if passwordChcek(password):
        re_password = input('Enter your password again:')
        if password == re_password:
            test +=1

        else:
            print ('passwords are not matching')

    else:
        print('password does not meet the requirement')

else:
    print('pair of passwords will work')
