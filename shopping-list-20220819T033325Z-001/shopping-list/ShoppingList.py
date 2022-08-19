"""SHOPPING LIST"""
def logon():
    logon = True
    while logon == True:
        log = input("1 - NEW USER\n2 - LOGIN\nOPTION:  ")
        if log == '1':
            logon = False
            masteruser()            
        elif log == '2':
            logon = False 
            login()                      
        else:
            logon = True

def masteruser():
    masteruser = True
    while masteruser == True:
        print('=================\n¦ VIRTUAL STORE ¦')
        print('=================\n¦ REGISTER USER ¦\n=================')
        user = input("User: ")  
        password = input("Password: ") 
        email = input("E-mail: ")     
        access = user + password
        return access
        menu()
     
    
def login():
    login = False
    while login == False:
        print('=================\n¦ VIRTUAL STORE ¦')
        print("=================\n¦     LOGIN     ¦\n=================")
        user = input("User: ")  
        password = input("Password: ") 
        check = user + password
        if access != check:      
            login = False
        else:             
            login = True    
            menu()        

def menu():
        menu = True
        while menu == True:
            print('====================\nDigite a opção desejada\n====================')
            option = int(input('1 - Insert Products\n2 - Consult Products\n3 - Shopping Cart\n4 - Para Sair'))
            if option == 1:
                menu = False 
                insertproducts()                
            elif option == 2:
                menu = False 
                consultproduct()                                           
            elif option == 3:
                menu = False 
                shoppincart()                            
            elif option == 4:
                menu = False
            else:
                menu = True


def insertproducts():
    insertproducts = 'on'
    mainlist = []
    while insertproducts != 'exit':   
            product = str(input('Product Name: '))
            product.title().strip()
            price = float(input('Price of Product: '))
            about = str(input('Description Name: '))
            about.title().split()
            mainlist.append([product,price,about])
            print(mainlist)
            option = int(input('1 - New Producto\n2 - Delet this item\n3 - Clear the List\n4 - Exite\n'))
            if option == 4:
                insertproducts = 'exit'
            elif option == 3:
                mainlist.clear()
            elif option == 2:
                mainlist.pop()
            else:
                print(mainlist)

logon()