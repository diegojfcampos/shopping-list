def consultproduct(mainlist):
    nonlocal mainlist
    if mainlist == []:
        consult = False
        while consult != True:
            redirection = 0
            redirection = int(input(('This list is empty\n1 - Insert Products\n2 - Exit '))
            if redirection != 1:
                insertproducts()
            else:
                consult = True
            else:       
                consultlist = mainlist     
                copylist = tuple(consultlist[])
                copylist1 = {}
                for j in range consultlist:            
                    copylist1[j] = consultlist
                    print('copylist1\n')