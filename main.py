import g
from datetime import datetime


def main():
    print('Wow another project jiro? Well you better finish this... ')
    print('Welcome to Point of Sales Prototype')
    print(g.receptionMainMenu)
    reception()


def reception():
    while True:
        receptionOutput = input('What action would you like to do: ')
        if receptionOutput in ['a', 'A']:
            receptionAActionCommand()
            break
        elif receptionOutput in ['b', 'B']:
            receptionBActionCommand()
            break
        elif receptionOutput in ['c', 'C']:
            receptionCActionCommand()
            break
        elif receptionOutput in ['d', 'D']:
            receptionDActionCommand()
            break
        elif receptionOutput in ['e', 'E']:
            receptionEActionCommand()
            break
        elif receptionOutput in ['menu', 'Menu', 'MENU']:
            print(g.receptionMainMenu)
        elif receptionOutput in ['admin', 'Admin', 'ADMIN']:
            adminCommand()
            break
        elif receptionOutput in ['exit', 'Exit', 'EXIT']:
            exitCommand('reception', None)
        else:
            print('Please select a valid character from the list. ')


def receptionAActionCommand():
    print('[A] View available items')
    loopThroughList(g.productID, g.productName, g.productPrice, g.productStock)
    if confirmationCommand(g.q6) in ['n', 'N']:
        reception()
    else:
        addItemToCartUserInput(g.productID, g.productName, g.productPrice, g.productStock)


def receptionBActionCommand():
    print('[B] Search for a product')
    print('Due to my inept intelect please enter the correct spelling and sequence of letters of the product name you wish to search.')
    receptionBActionOutput = input('What item are we looking for: ')
    if receptionBActionOutput == '**return'.casefold(): goToCommand('reception')
    split = receptionBActionOutput.split()
    for x in g.productName:
        if all(var in x for var in split):
            g.productNameSearchList.append(x)
            index = g.productName.index(x)
            g.productNameIndexList.append(index)
            g.productIDSearchList.append(g.productID[index])
            g.productPriceSearchList.append(g.productPrice[index])
            g.productStockSearchList.append(g.productStock[index])
    if g.productNameSearchList:
        print(f'Product(s) from the list containing {receptionBActionOutput}')
        print('   - ID -  - Name -  - Price -  - Stock - ')
        for index in range(len(g.productNameSearchList)):
            print(index + 1, ' : ', g.productIDSearchList[index], ' - ', g.productNameSearchList[index],
                  ' - ', g.productPriceSearchList[index], ' - ', g.productStockSearchList[index])
        if confirmationCommand(g.q6) in ['n', 'N']:
            reception()
        else:
            addItemToCartUserInput(g.productIDSearchList, g.productNameSearchList, g.productPriceSearchList, g.productStockSearchList)
    else:
        print(f'{receptionBActionOutput} is not in stock')
        if confirmationCommand(g.q5) in ['n', 'N']:
            reception()
        else:
            receptionBActionCommand()


def addItemToCartUserInput(tempID, tempName, tempPrice, tempStock):
    while True:
        try:
            productIndex = input('Enter product slot: ')
            if productIndex == '**return'.casefold(): 
                reception()
                break
            productIndex = int(productIndex)
        except ValueError:
            continue
        i = productIndex - 1
        if productIndex > len(tempID):
            continue
        # if its equals to zero then it ahs already been poppeed right? identical line at popitemtocart
        if tempStock[i] == 0:
            continue
        break
    while True:
        try:
            quantity = input('How many will you put in your cart: ')
            if quantity == '**return'.casefold(): 
                addItemToCartUserInput(tempID, tempName, tempPrice, tempStock)
                break
            quantity = int(quantity)
        except ValueError:
            continue
        if quantity > tempStock[i]:
            print(f'There are only {tempStock[i]} available {tempName[i]}')
            addItemToCartQuantityOverflow(tempID, tempName, tempPrice, tempStock, i)
            break
        tempStock[i] = tempStock[i] - quantity
        addItemToCart(tempID, tempName, tempPrice, quantity, i, tempStock)
        break
    

def addItemToCartQuantityOverflow(tempID, tempName, tempPrice, tempStock, i):
    while True:
        try:
            quantityOverflowConfirmation = input('Would you like to take them all or change quantity (1 or 2): ')
            if quantityOverflowConfirmation == '**return'.casefold(): 
                addItemToCartUserInput(tempID, tempName, tempPrice, tempStock)
                break
            quantityOverflowConfirmation = int(quantityOverflowConfirmation)
        except ValueError:
            continue
        if quantityOverflowConfirmation == 1:
            stock = tempStock[i]
            tempStock[i] = tempStock[i] - tempStock[i]
            addItemToCart(tempID, tempName, tempPrice, stock, i, tempStock)
            break
        elif not 2:
            continue
        break
    while True:
        try:
            newQuantity = input('How many will you put in your cart: ')
            if newQuantity == '**return'.casefold(): 
                addItemToCartUserInput(tempID, tempName, tempPrice, tempStock)
                break
            newQuantity = int(newQuantity)
        except ValueError:
            continue
        if newQuantity >= tempStock[i]:
            print(f'There are only {tempStock[i]} available {tempName[i]}')
            continue
        tempStock[i] = tempStock[i] - newQuantity
        addItemToCart(tempID, tempName, tempPrice, newQuantity, i, tempStock)
        break
    
        
def addItemToCart(tempID, tempName, tempPrice, quantity, i, idkwhattoname):
    appendList(g.cartProductID, g.cartProductName, g.cartProductPrice, g.cartProductStock, tempID[i], tempName[i], tempPrice[i], quantity)
    print(f'{quantity} {tempName[i]} added to cart. ')
    popList(tempID, tempName, tempPrice, idkwhattoname, i, False)
    loopThroughList(g.productID, g.productName, g.productPrice, g.productStock)
    if confirmationCommand(g.q7) in ['n', 'N']:
        reception()
    else:
        addItemToCartUserInput(tempID, tempName, tempPrice, idkwhattoname)


def receptionCActionCommand():
    print('[C] My cart')
    loopThroughList(g.cartProductID, g.cartProductName, g.cartProductPrice, g.cartProductStock)
    if confirmationCommand(g.q9) in ['n', 'N']:
        checkOutFromCart()
    else:
        editItemToCart()


def editItemToCart():
    while True:
        try:
            productIndex = input('Enter product slot: ')
            if productIndex == '**return'.casefold(): 
                reception()
                break
            productIndex = int(productIndex)
        except ValueError:
            continue
        i = productIndex - 1
        if productIndex > len(g.cartProductID):
            continue
        break
    while True:
        try:
            confirmation = input(f'Would you like to remove {g.cartProductName[i]} from your cart or change its quantity (1 or 2): ')
            if confirmation == '**return'.casefold(): 
                editItemToCart()
                break
            confirmation = int(confirmation)
        except ValueError:
            continue
        if confirmation == 1:
            removeItemToCart(i)
        elif confirmation == 2:
            changeItemToCart(i)
        break
    checkOutFromCart()


def checkOutFromCart():
    if confirmationCommand(g.q10) in ['n', 'N']:
        receptionCActionCommand()
    else:
        receptionDActionCommand()


def removeItemToCart(i):
    index = g.productName.index(g.cartProductName[i])
    if g.cartProductName[i] in g.productName:
        g.productStock[index] = g.productStock[index] + g.cartProductStock[i]
    else:
        appendList(g.productID, g.productName, g.productPrice, g.productStock, g.popProductID[i], g.popProductName[i], g.popProductPrice[i], g.cartProductStock[i])
    popList(g.cartProductID, g.cartProductName, g.cartProductPrice, g.cartProductStock, i, True)
    # maybe we dont need this
    loopThroughList(g.productID, g.productName, g.productPrice, g.productStock)


def changeItemToCart(i):
    # what if magbabawas sa from cart... hindi mo naisip yun no. recycle code from admin same lang nito
    index = g.productName.index(g.cartProductName[i])
    if g.cartProductName[i] not in g.productName:
        print(f'{g.cartProductName[i]} has no stocks left in shelf')
        reception()
    print(f'There are {g.productStock[index]} available {g.productName[index]}')
    while True:
        try:
            quantity = input('How many will you add: ')
            if quantity == '**return'.casefold(): 
                editItemToCart()
                break
            quantity = int(quantity)
        except ValueError:
            continue
        if quantity > g.productStock[index]:
            print(f'There are only {g.productStock[index]} available {g.productID[index]}')
            continue
        g.cartProductStock[i] = g.cartProductStock[i] + quantity
        g.productStock[i] = g.productStock[i] - quantity
        popList(g.productID, g.productName, g.productPrice, g.productStock, index, False)
        break
    if confirmationCommand(g.q7) in ['n', 'N']:
        pass
    else:
        receptionCActionCommand()


def receptionDActionCommand():
    # check out from cart
    # do payment
    print('[D] Check out')
    # total all price and show recipt 
    # add payment method?
    print('\n *RECEIPT* ')
    dt = datetime.now()
    date, time = dt.strftime('%d/%m/%Y'), dt.strftime('%H:%M:%S')
    print(f'Date: {date}')
    print(f'Time: {time}\n')
    totalPriceList =  []
    for index in range(len(g.cartProductID)):
        if g.cartProductStock[index] is 1:
            print(f'{g.cartProductName[index]} - {g.cartProductPrice[index]}')
            x = g.cartProductPrice[index]
        else:
            raw = g.cartProductPrice[index]*float(g.cartProductStock[index])
            twoDecimals = '{:.2f}'.format(raw)
            print(f'{g.cartProductName[index]} - {float(twoDecimals)}\n    {g.cartProductStock[index]} x {g.cartProductPrice[index]}')
            x = twoDecimals
        totalPriceList.append(float(x))
    raw = sum(totalPriceList)
    total = '{:.2f}'.format(raw)
    print(f'''\n                    -----
Total               {total}
                    -----
Cash: {userCash}                    
Change: {userChange}''')
    



def receptionEActionCommand():
    print('[E] Cancel')
    removeAndClearList(g.cartProductID, g.cartProductName, g.cartProductPrice, g.cartProductStock, 'Cart')
    reception()


def adminCommand():
    for x in range(5):
        adminOutput = input('Enter the password: ')
        if adminOutput == '**return'.casefold(): 
            reception()
            break
        if adminOutput == g.password:
            adminPortal()
            break
    else:
        print('Too many attempts... Try again later')
        reception()


def adminPortal():
    print(g.adminPortalMainMenu)
    while True:
        adminPortalOutput = input('What action would you like to do next: ')
        if adminPortalOutput in ['a', 'A']:
            adminAActionCommand()
            break
        elif adminPortalOutput in ['b', 'B']:
            adminBActionCommand()
            break
        elif adminPortalOutput in ['c', 'C']:
            adminCActionCommand()
            break
        elif adminPortalOutput in ['d', 'D']:
            adminDActionCommand()
            break
        elif adminPortalOutput in ['e', 'E']:
            adminEActionCommand()
            break
        elif adminPortalOutput in ['menu', 'Menu', 'MENU']:
            print(g.adminPortalMainMenu)
        elif adminPortalOutput in ['return', 'Return', 'RETURN']:
            goToCommand('reception')
            break
        else:
            print('Please select a valid character from the list. ')


def adminAActionCommand():
    print('[A] Add stock')
    while True:
        try:
            addProductID = int(input('Product ID: '))
        except ValueError:
            continue
        else:
            if addProductID > 9999 or addProductID < 1000:
                print('The required product ID is 4 digits')
                continue
            g.productID.append(addProductID)
            break
    while True:
        try:
            addProductName = str(input('Product Name: '))
            if addProductName == '':
                continue
        except ValueError:
            continue
        else:
            g.productName.append(addProductName)
            break
    while True:
        try:
            addProductPrice = float(input('Product Price: '))
        except ValueError:
            continue
        else:
            g.productPrice.append(addProductPrice)
            break
    while True:
        try:
            addProductStock = int(input('Product Stock: '))
        except ValueError:
            continue
        else:
            if addProductStock < 1:
                print('Stock should be at least one')
                continue
            g.productStock.append(addProductStock)
            break
    print(g.productIDSlotNumber + 1, ' : ', g.productID[-1], ' - ', g.productName[-1], ' - ',
          g.productPrice[-1], ' - ', g.productStock[-1])


def adminBActionCommand():
    print('[B] Edit store stock')
    loopThroughList(g.productID, g.productName, g.productPrice, g.productStock)
    while True:
        try:
            editNumber = input('Edit item number: ')
            if editNumber == '**return'.casefold(): 
                adminPortal()
                break
            editNumber = int(editNumber)
        except ValueError:
            continue
        break
    editNumberSlot = editNumber - 1
    print(editNumber, ' : ', g.productID[editNumberSlot], ' - ', g.productName[editNumberSlot],
          ' - ', g.productPrice[editNumberSlot], ' - ', g.productStock[editNumberSlot])
    print(g.adminBActionMainMenu)
    while True:
        adminBActionOutput = input('What action would you like to do next: ')
        if adminBActionOutput in ['a', 'A']:
            adminBAActionCommand(editNumber, editNumberSlot)
            break
        elif adminBActionOutput in ['b', 'B']:
            adminBBActionCommand(editNumberSlot)
            break
        elif adminBActionOutput in ['menu', 'Menu', 'MENU']:
            print(g.adminBActionMainMenu)
        elif adminBActionOutput in ['return', 'Return', 'RETURN']:
            goToCommand('adminPortal')
            break
        else:
            print('Please select a valid character from the list. ')


def adminBAActionCommand(editNumber, editNumberSlot):
    print('[A] Edit')
    print(editNumber, ' : ', g.productID[editNumberSlot], ' - ', g.productName[editNumberSlot], ' - ',
          g.productPrice[editNumberSlot])
    print('Toggle Enter key to skip')
    print(f'Product ID: {g.productID[editNumberSlot]}')
    while True:
        try:
            g.editProductID = int(input('New product ID: '))
        except ValueError:
            # if editProductID is not true it means that the variable is empty
            # in result of the user toggling the enter key this snippet is a redundant fail safe
            if not g.editProductID:
                break
        else:
            if g.editProductID > 4 or g.editProductID < 4:
                print('The required product ID is 4 digits')
                continue
            g.productID[editNumberSlot] = g.editProductID
            break
    print(f'Product Name: {g.productName[editNumberSlot]}')
    while True:
        try:
            g.editProductName = str(input('New product Name: '))
        except ValueError:
            if not g.editProductName:
                break
        else:
            g.productName[editNumberSlot] = g.editProductName
            break
    print(f'Product Price: {g.productPrice[editNumberSlot]}')
    while True:
        try:
            g.editProductPrice = float(input('New product Price: '))
        except ValueError:
            if not g.editProductPrice:
                break
        else:
            g.productPrice[editNumberSlot] = g.editProductPrice
            break
    print(editNumber, ' : ', g.productID[editNumberSlot], ' - ', g.productName[editNumberSlot], ' - ',
          g.productPrice[editNumberSlot])
    # use return portal here???
    adminPortal()


def adminBBActionCommand(removeSlot):
    print('[B] Remove')
    if confirmationCommand(g.q1) in ['n', 'N']:
        reception()
    else:
        popList(g.productID, g.productName, g.productPrice, g.productStock, removeSlot, True)
        adminBActionCommand()


def adminCActionCommand():
    print('[C] Clear store stock')
    removeAndClearList(g.productID, g.productName, g.productPrice, g.productStock, 'Stock')
    adminPortal()


def adminDActionCommand():
    print('[C] Sales receipt')
    # total gross, operation time, stocks left


def adminEActionCommand():
    print('[D] Close of business')
    exitCommand('adminPortal', 'adminDActionCommand')


def goToCommand(returnKeyword):
    eval(returnKeyword + '()')


def exitCommand(exitKeyword, preExitAction):
    # i cannot use the current confirmation here because i will need to make new functions
    if confirmationCommand(g.q1) in ['n', 'N']:
        eval(exitKeyword + '()')
    if preExitAction:
        # undestand this pls
        eval(preExitAction + '()')
    else:
        exit()


def popList(IDList, nameList, priceList, stockList, pop, trulse):
    print('called')
    if stockList[pop] == 0 or trulse == True:
        g.popProductID.append(IDList.pop(pop))
        g.popProductName.append(nameList.pop(pop))
        g.popProductPrice.append(priceList.pop(pop))
        g.popProductStock.append(stockList.pop(pop)) # this is 0 because we cleaned the stock list
        print('exec')
    print('bye')


def appendList(IDList, nameList, priceList, stockList, IDAppend, nameAppend, priceAppend, stockAppend):
    IDList.append(IDAppend)
    nameList.append(nameAppend)
    priceList.append(priceAppend)
    stockList.append(stockAppend)


def clearList(IDList, nameList, priceList, stockList):
    IDList.clear()
    nameList.clear()
    priceList.clear()
    stockList.clear()


# additional func


def confirmationCommand(promt):
    while True:
        userConfirmation = input(promt)
        if userConfirmation in ['y', 'Y']:
            return
        elif userConfirmation in ['n', 'N']:
            ugh = userConfirmation
            return ugh
        else:
            continue
            #print('Please select a valid character from the list. ')


def removeAndClearList(clearID, clearName, clearPrice, clearStock, message):
    if confirmationCommand(g.q2) in ['n', 'N']:
        reception()
    if confirmationCommand(g.q3) in ['n', 'N']:
        reception()
    if confirmationCommand(g.q4) in ['n', 'N']:
        reception()
    clearList(clearID, clearName, clearPrice, clearStock)
    print(f'{message} cleared')


def loopThroughList(tempID, tempName, tempPrice, tempStock):
    print('     - ID -  - Name -  - Price -  - Stock - ')
    for index in range(len(tempID)):
        print(index + 1, ' : ', tempID[index], ' - ', tempName[index],
              ' - ', tempPrice[index], ' - ', tempStock[index])


main()

# look for professional app messages to user
# add server side like a file or smth
# add exit to options
# mass add items to cart
# multiple chosen index to remove and add option
# add option to show menu in functions with menu if menu true: menu
# add option to show instruction messages
# change one value function
# better question variables
# strip whitespace from input
# use dict to put removed and added product in the original slot
