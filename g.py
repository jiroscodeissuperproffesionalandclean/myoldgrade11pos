

# Product information
# try list for product info
# only 4 digits alphabetic number(if double digit get the second one), Flavour, Ounce(if ounce only a digit add 0)
productID = [4214, 2113, 6190, 3480, 3515, 8113, 2180, 2370, 4614, 2713]
productName = ['Doritos Nacho Cheese 14.5 oz', 'Lay\'s Classic 13 oz', 'Fritos Original 9.25 oz', 'Cheetos Puff 8 oz',
               'Cheetos Crunchy 15 oz', 'Ruffles Original 13 oz', 'Lay\'s Classic 8 oz', 'Lay\'s Barbecue 7.75 oz',
               'Doritos Cool Ranch 14.5 oz', 'Lay\'s Wavy Original 13 oz']
productPrice = [4.98, 4.78, 3.98, 3.98, 4.98, 4.98, 3.48, 3.48, 4.98, 4.78]
productStock = [30, 30, 25, 30, 30, 30, 30, 30, 20, 25]

cartProductID = []
cartProductName = []
cartProductPrice = []
cartProductStock = []

popProductID = []
popProductName = []
popProductPrice = []
popProductStock = []

timesIDEntered = 0
timesNameEntered = 0
timesPriceEntered = 0
timesQuantityEntered = 0

editProductID = None
editProductName = None
editProductPrice = None
editProductStock = None

productIDSlotNumber = len(productID)
productNameSlotNumber = len(productName)
productPriceSlotNumber = len(productPrice)
productStockSlotNumber = len(productStock)

productIDSearchList = []
productNameSearchList = []
productPriceSearchList = []
productStockSearchList = []
productNameIndexList = []

productIDSearchList = []
productNameSearchList = []
productPriceSearchList = []
productStockSearchList = []
productNameIndexList = []

receptionMainMenu = '''
 - Main Menu - 
[A] View available items
[B] Search for a product
[C] My cart
[D] Check out
[E] Cancel
[Menu]
[Exit]'''

adminPortalMainMenu = '''
 - Admin Menu - 
[A] Add stock
[B] Edit store stock
[C] Clear store stock
[D] Sales receipt
[E] Close of business
[Menu]
[Return]'''

adminAActionMenu = '''
[Add]
'''

adminBActionMainMenu = '''[A] Edit
[B] Remove'''

q1 = 'Are you sure (Y or N): '
q2 = '1/3 Are you sure (Y or N): '
q3 = '2/3 Are you sure (Y or N): '
q4 = '3/3 Are you sure (Y or N): '
q5 = 'Would you like to search for anything else (Y or N): '
q6 = 'Add item(s) to cart? (Y or N): '
q7 = 'Would you like to add anything else (Y or N): '
q8 = 'Would you like to edit anything else (Y or N): '
q9 = 'Would you like to edit an item to cart (Y or N): '
q10 = 'Would you like to proceed to check out (Y or N): '


# if we have problems with calculation maybe check here because the variable isnt already set to a set type
# productID = 124
# print(productID)
# print(type(productID))
# admin password
password = 'clichepassword'
# alternative
# def password():
#     global password
#     password = 'clichepassword'

# 'Plain Apa', 'Sprinkled Plain Apa', 'Choco Dipped Apa', 'Strawberry Dipped Apa', 'Plain Sugar Cone', 'Sprinkled Plain Sugar Cone', 'Choco Dipped Sugar Cone', 'Strawberry Dipped Sugar Cone', 'Mini Sundae'
# for ice creaman prototype


#all of this is a test
    #user can click choose slot twice
    #print('Put a space between numbers if choosing multiple index')
    #productIndex = input('Enter product(s) slot: ')
    #splitIndex = productIndex.split()
    #multipleIndex = []
    #for x in splitIndex:
    #    multipleIndex.append(int(x))
    #for x in multipleIndex:
    #    i = x - 1
    #    g.cartProductID.append(productIDSearchList[i])
    #    g.cartProductName.append(productNameSearchList[i])
    #    g.cartProductPrice.append(productPriceSearchList[i])
    #    g.cartProductStock.append(productStockSearchList[i])
    #for index in range(len(g.cartProductID)):
    #    print(g.cartProductID[index], ' - ', g.cartProductName[index],
    #          ' - ', g.cartProductPrice[index], ' - ', g.cartProductStock[index])
    # if we do implement this add duplicate remover using set()
