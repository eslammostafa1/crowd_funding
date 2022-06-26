import auth
import login

while True:
    print("""--------------------------------------------------------------------------------"
                                     MAIN MENU   
                                     -----------                                    
        =>press (1) for registration                                                        
        =>press (2) for login  
        =>press (any) for exit                                                 """)
    inp = input("your choice is ")
    if inp == "1":
        auth.registrate()
    elif inp == "2":
        login.login_fun()
    else:
        break
