myItems = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(items):
  for i in items:
    print(items.value(), items.key())


displayInventory(myItems)
     