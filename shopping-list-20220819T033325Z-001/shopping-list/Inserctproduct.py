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
    option = int(input('\n1 - New Product\n2 - Delet this item\n3 - Clear the List\n4 - Exite\n'))
    if option == 4:
        insertproducts = 'exit'
        print(f'List {mainlist}')
    elif option == 3:
        mainlist.clear()
        print(f'List {mainlist}')
    elif option == 2:
        mainlist.pop()
        print(f'List {mainlist}')
    else:
        print(f'List {mainlist}')
                
