db = {
    'peter':{'password':'00000000'},
    'backbender':{'password': '12345678'}

}

Max_attempts = 3
attempts = 0

while attempts < Max_attempts:
    username = input('enter your username')

    if username.lower() == 'quit':
        print('Goodbye hehe!')
        break

    if username in db.keys():
        password = input('create a new password')

        if  db[username]['password'] == password:
            print('you have logged in')
            break

        else:
            attempts += 1
            remaining = Max_attempts - attempts
            if remaining > 0:
                print('Remember your password please. You have ' + str(remaining) + ' attempt(s) left.')
    else:
        attempts += 1
        remaining = Max_attempts - attempts
        if remaining > 0:
            print('you better be joking. You have ' + str(remaining) + ' attempt(s) left.')

    if attempts == Max_attempts:
        print('You have been blocked after 3 failed attempts.')