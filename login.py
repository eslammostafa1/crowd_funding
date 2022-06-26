import newproject

print("welcome from login.py file")

username = ''


def login_fun():
    userDataEntry = open('user_data.txt', 'r')
    listLines = userDataEntry.readlines()
    userDataEntry.close()
    print(listLines)
    userDict = {}
    for eachLine in listLines:
        entry = eachLine.split(',')
        email = entry[2]
        password = entry[3]
        user_name = entry[0]
        userDict[email] = [password, user_name]
    print(userDict)

    checker = 0
    while checker == 0:
        print("\nYou've registered first? let's login then!\n")
        emailInput = input("Please enter your email:")
        passwordInput = input("Please enter your password:")

        if emailInput in userDict:
            if userDict[emailInput][0] == passwordInput:
                print("\nLogin successful!\nWelcome back,", userDict[emailInput][1])
                global username
                username = userDict[emailInput][1]
                checker = 1

            else:
                print("Password is incorrect. Try again.")
                checker = 0

        else:
            print("Username does not exist. Try again.")
            checker = 0
    nextStep = int(input("\nWould you like to:\n1.) logout \n2.)Create projects\n3.) View projects\n4.) edit your projects\n5.) delete your projects\n"))
    if nextStep == 1:
        print("\nGoodbye!")

    if nextStep == 2:
        print("\ngo to Projects\n")
        newproject.create_project(username)

    if nextStep == 3:
        print("\nview all Projects\n")
        newproject.view_project()

    if nextStep == 4:
        print("\nedit your Projects\n")
        newproject.edit_project(username)

    if nextStep == 5:
        print("\ndelete your Projects\n")
        newproject.delete_project(username)
