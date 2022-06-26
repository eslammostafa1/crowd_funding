import re
import datetime


def view_project():
    print("welcome from view project function")
    project_data = open("project_data.txt", "r")
    project_data_line = project_data.readlines()
    project_data.close()
    print(project_data_line)
    print(project_data)
    it = 1
    for eachline in project_data_line:
        proj = eachline.split(",")
        print(" --------------------------project {} ---------------------".format(it))
        print(proj)
        it += 1


def edit_project(userlogin):
    global proj
    print(f"welcome {userlogin} from edit project function")
    project_data = open("project_data.txt", "r")
    project_data_line = project_data.readlines()
    project_data.close()
    it = 0
    proj = ''
    for eachline in project_data_line:
        proj = eachline.split(",")
        it += 1
        if userlogin == proj[5]:
            print(f" user is created this project <<<<{proj[5]}>>>>> ")
            print("enter number of what you want to change "
                  "\n1)name "
                  "\n2)details "
                  "\n3)target price "
                  "\n4)start date "
                  "\n5)end date ")
            editindicator = input("the number is : ")
            if editindicator == '1':
                proj[0] = input("enter the new name:")
                print(proj)
                print(it)
                break
            elif editindicator == '2':
                proj[1] = input("enter the new details:")
                print(proj)
                print(it)
                break
            elif editindicator == '3':
                proj[2] = input("enter the new target:")
                print(proj)
                print(it)
                break
            elif editindicator == '4':
                proj[3] = input("enter the new start date:")
                print(proj)
                print(it)
                break
            elif editindicator == '5':
                proj[4] = input("enter the new end date:")
                print(proj)
                print(it)
                break
            else:
                print("enter a number from the range !!")
    print(proj)
    print(it)
    print(project_data_line[it-1])
    strproj = ','.join(proj)
    print(strproj)
    project_data_line[it-1] = strproj
    print(project_data_line)
    print(proj)
    project_data = open("project_data.txt", "w")
    project_data.writelines(project_data_line)
    project_data.close()


def delete_project(userlogin):
    global proj
    print(f"welcome {userlogin} from delete project function")
    project_data = open("project_data.txt", "r")
    project_data_line = project_data.readlines()
    project_data.close()
    it = 0
    proj = ''
    for eachline in project_data_line:
        proj = eachline.split(",")
        it += 1
        if userlogin == proj[5]:
            print(f" user is created this project <<<<{proj[5]}>>>>> ")
            print("Are your sure you want delete project? y|n")
            ans = input(" => ")
            if ans == 'y' or ans == 'Y':
                proj = ''
                print(it)
                break
            else:
                print("try again ...")
    print(proj)
    print(it)
    print(project_data_line[it-1])
    project_data_line[it-1] = proj
    print(project_data_line)
    print(proj)
    project_data = open("project_data.txt", "w")
    project_data.writelines(project_data_line)
    project_data.close()


def create_project(userlogin):
    print("welcome from create project function")
    global project
    project = {'title': '', 'details': '', 'total_target': '', 'start_date': '', 'end_date': '', 'user_created': ''}
    print("Create project \n")
    # get user logging successfully from the login file to create a user

    # the title of the must be max 3 words
    project['title'] = input("Enter a project title: ")
    while not re.match('^(\w{2,20})\s(\w{1,20})?\s(\w{1,20})?\s?$', project['title']):
        project['title'] = input('Enter a project title (must be three words): ')
        if not re.match('^(\w{2,20})\s(\w{1,20})?\s(\w{1,20})?\s?$', project['title']):
            break

    # description of a project. example : this is a project for a poor poeple in india ana homeless poeple
    project['details'] = input("Enter a project details: ")

    # this is a mini and max budget of the project ^[0-9]{3,7}$
    project['total_target'] = input("Enter a project total target: ")
    while not re.match('^[0-9]{3,7}$', project['total_target']):
        project['total_target'] = input('Enter a project total target(must be from 1000 to 9999999): ')
        if not re.match('^[0-9]{3,7}$', project['title']):
            break

    # start date of project
    while True:
        start_date = input('Enter a project start date: day month year ')
        project['start_date'] = datetime.datetime.strptime(start_date, "%d %m %Y").date()
        print(project['start_date'].strftime("%d %b %Y"))
        check = input("are your start date is right? y|n ")
        if check == 'y' or check == 'Y':
            break
        else:
            print("Enter your start date again. ")

    # end date of project
    while True:
        end_date = input('Enter a project end date: day month year ')
        project['end_date'] = datetime.datetime.strptime(end_date, "%d %m %Y").date()
        print(project['end_date'].strftime("%d %b %Y"))
        check = input("are your end date is right? y|n ")
        if check == 'y' or check == 'Y':
            break
        else:
            print("Enter your end date again. ")

    print("\nstart date is  {} \nend date is   {} ".format(datetime.datetime.strptime(start_date, "%d %m %Y"),
                                                           datetime.datetime.strptime(end_date, "%d %m %Y")))
    project['user_created'] = userlogin

    print(project)

    project_data = open("project_data.txt", "a")
    project_data.write(project['title'])
    project_data.write(",")
    project_data.write(project['details'])
    project_data.write(",")
    project_data.write(project['total_target'])
    project_data.write(",")
    project_data.write(project['start_date'].strftime("%d %b %Y"))
    project_data.write(",")
    project_data.write(project['end_date'].strftime("%d %b %Y"))
    project_data.write(",")
    project_data.write(project['user_created'])
    project_data.write(",")
    project_data.write("\n")
    project_data.close()


print("welcome from project files")
