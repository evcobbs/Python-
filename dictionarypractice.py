#dictionary practice

myGirls = {
  'Ali':{'Movie':5, 'Beer':10},
  'Yuko':{'Art':3, 'Movie':7, 'Beer':10, 'history':4},
  'Emiko':{'Art':6, 'Beer':3, 'History':7}
}

def totalPower(girls, hobby):
  power =  0
  for k, v in girls.items():
    power = power + v.get(hobby, 0)
  return power


print("Your group has...")

print('beer power of ' + str(totalPower(myGirls, 'Beer')))


#dictionary practice? 
myItems = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
      print (v, k)
      item_total = item_total + v
    print("Total number of items: " + str(item_total))

displayInventory(myItems)

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
     