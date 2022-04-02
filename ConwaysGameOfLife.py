#Conway's game of life
#from Ch4 Automate the Boring stuff with Python
#my attempt

import random, time, copy

WIDTH = 60
HEIGHT = 20

#creat a nested list for the cells
nextCells = []
for x in range(WIDTH):
  column = [] #new column
  for y in range(HEIGHT):
    if random.randint(0, 1) == 0:
      column.append('#') # living cell
    else: 
      column.append(' ') #Dead cell
  nextCells.append(column) 


while True: #main program loop
  print('\n\n\n\n\n') #seperate each step with newlines. 
  currentCells = copy.deepcopy(nextCells)

  #print currentCells on screen
  for y in range (HEIGHT):
    for x in range (WIDTH):
      print(currentCells[x][y], end = '')
    print()

  #calculate next steps cells based on current steps cells
  for x in range(WIDTH):
    for y in range(HEIGHT):
      #get neighbor coordintaes 
      # makes sure leftCoord is alwasy between 0 and width -1
      leftCoord = (x-1)% WIDTH
      rightCoord = (x+1)% WIDTH
      aboveCoord = (y-1)% HEIGHT
      belowCoord = (y+1)% HEIGHT

      #count living neighbors 
      numNeighbors = 0
      if currentCells[leftCoord][aboveCoord] == '#':
        numNeighbors += 1 #top left
      if currentCells[x][aboveCoord] == '#':
        numNeighbors += 1 #top
      if currentCells[rightCoord][aboveCoord] == '#':
        numNeighbors += 1 #top right
      if currentCells[leftCoord][y] == '#':
        numNeighbors += 1 #left
      if currentCells[rightCoord][y] == '#':
        numNeighbors += 1 #right
      if currentCells[leftCoord][belowCoord] == '#':
        numNeighbors += 1 #bottom left
      if currentCells[x][belowCoord] == '#':
        numNeighbors += 1 #bottom
      if currentCells[rightCoord][belowCoord] == '#':
        numNeighbors += 1 #bottom right

      #set cell based on rules
      if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
        nextCells [x][y] = '#' #cells staying alive
      elif currentCells[x][y] == ' 'and numNeighbors ==3:
        nextCells [x][y] = '#' #cells coming alive
      else:
        nextCells [x][y] = ' ' #everything else, stay dead or die
  time.sleep(1)
      