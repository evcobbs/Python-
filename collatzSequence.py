#The Collatz Sequence
#from automate the boring stuff with python
#completed april 2022

print( """ 
Welcom to The Collatz Sequence.
Enter any whole number greater than one.
I will crush it. 
        """)


def collatz():
  try: 
    #this MF has to be IN the try loop or the IDE will throw an exception befoe you can handle
    num= int(input("Enter a number:"))
    while num > 1:
      if num % 2== 0:
        print(num//2)
        num = num//2
      else:
        print(3*num+1)
        num = 3*num+1
    print("Done!")
  except ValueError:
    print("Please enter an integer")
    #added this so user can keep trying until they enter a valid int
    collatz()



collatz()
    
  