#coin flip streaks 
#Automate the boring stuff with python Ch4 
#added a wrapper practice
#added a version using generator, instead of a list to see if the generator is faster as well as more space efficient. 

import random
from time import time 

#wrapper to see if list or generators are faster 
def timePerformance(func):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'this took {t2-t1} ms.')
    return result
  return wrapper

#coinFlipExperiment using list. 
@timePerformance 
def coinFlipExperimentLIST(numOfExperiments):
  numberOfStreaks = 0
  coinFlips = []
  streak = 1
  
  for experimentNumber in range(numOfExperiments):
  #create list of 100 heads or tails (1 or 0)
    for i in range (99):
      flip = random.randint(0, 1)
      coinFlips.append(flip)
  #print(coinFlips) # my check 
  
  #check if there is 6+ streak of heads or tails (1 or 0)
    for i in range(len(coinFlips)):
      if coinFlips[i] == coinFlips[i-1]:
        streak +=1
      else: 
        streak == 1

      if streak == 6:
        numberOfStreaks += 1

  print('Chance of streak: %s%%' % (numberOfStreaks / 100))

#coinFlipExperiment using generators 
#range is a generator, we don't save the values in the list to save time and storage. 
@timePerformance 
def coinFlipExperimentGEN(numOfExperiments):
  numberOfStreaks = 0
  streak = 1
  flip = random.randint(0, 1)
  
  for experimentNumber in range(numOfExperiments):
  
#check if there is 6+ streak of heads or tails (1 or 0)
    for i in range(99):
      nextFlip = random.randint(0, 1)
      if nextFlip == flip:
        streak +=1
      else: 
        streak == 1
        
      if streak == 6:
        numberOfStreaks += 1

      flip == nextFlip 

  print('Chance of streak: %s%%' % (numberOfStreaks / 100))

print("---list---")
print("1 list")
coinFlipExperimentLIST(1)
print("10 list")
coinFlipExperimentLIST(10)
print("100 list")
coinFlipExperimentLIST(100)
print("1000 list")
coinFlipExperimentLIST(1000)

print("---no list---")
print("1 gen")
coinFlipExperimentGEN(1)
print("10 gen")
coinFlipExperimentGEN(10)
print("100 gen")
coinFlipExperimentGEN(100)
print("1000 gen")
coinFlipExperimentGEN(1000)
  