#comma code
import copy

spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['Chris', 'Emily', 'Matt', 'Joseph', 'Kyle', 'Ian', 'Ross']

def commaCode(list):
  newlist = copy.copy(list)
  newlist[-2] = 'and '
  for i in (newlist):
    if i == newlist[-2]:
      print (i, end = "")
    elif i == newlist[-1]:
      print (i)
    else:
      print (i + ', ', end = "")

commaCode(spam)
commaCode(spam2)