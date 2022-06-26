import re


def registrate():
    print("     registrate      \n"
          "     ----------        ")
    # enter the first name of the user must be all characters.
    first_name = input("Enter the first name: ")
    while not re.match('[A-Za-z]{3,25}$', first_name):
        first_name = input('Enter the first name again: ')
        if re.match('[A-Za-z]{3,25}$', first_name):
            break

    # enter the first name of the user must be all characters.
    last_name = input("Enter the last name: ")
    while not re.match('[A-Za-z]{3,25}$', last_name):
        last_name = input('Enter the last name again: ')
        if re.match('[A-Za-z]{3,25}$', last_name):
            break

    # validate the email of your by the default form email  [a-z0-9]+[\._]?[A-Za-z0-9]+[\@]\w+[\.][a-z]{2,4}
    email = input("Enter the your mail: ")
    while not re.match('[a-z0-9]+[\._]?[A-Za-z0-9]+[\@]\w+[.][a-z]{2,4}', email):
        email = input('Enter the email again: ')
        if re.match('[a-z0-9]+[\._]?[A-Za-z0-9]+[\@]\w+[.][a-z]{2,4}', email):
            break

    password = input("Enter your password: ")
    while len(password) < 8:
        password = input('Enter the password again: ')

    pass_confirm = input("please confirm the password: ")
    while password != pass_confirm:
        pass_confirm = input("password do not match, Enter the password again: ")

    # 01[0125][0-9]{8}
    phone = input("Enter the phone number: ")
    while not re.match('01[0125][0-9]{8}', phone):
        phone = input('Enter the phone again: ')
        if re.match('01[0125][0-9]{8}', phone):
            break


    userdata = open("user_data.txt", "a+")
    data = userdata.read()
    if len(data) > 0:
        userdata.write("\n")
    userdata.write(first_name)
    userdata.write(",")
    userdata.write(last_name)
    userdata.write(",")
    userdata.write(email)
    userdata.write(",")
    userdata.write(password)
    userdata.write(",")
    userdata.write(phone)
    userdata.write(",")
    userdata.write("\n")
    userdata.close()


