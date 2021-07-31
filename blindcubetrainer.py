import sys
import time

def option1():
  print("test 1")
def option2():
  pass
def option3():
  pass
def quit():
  print("Closing Cube Trainer")
  time.sleep(2)
  sys.exit()  

# Start of Menu
def menu():
  print("########## Rubik Cube Trainer ##########")
  time.sleep(1)

choice = input(""")
  [1] Option 1
  [2] Option 2
  [3] Option 3
  [0] Exit Cube Trainer

Select Training Program to Run: """)

if choice == "1" or choice == "Option 1":
      #do option 1 stuff
      print("Option 1 selected")
elif choice == "2" or choice == "Option 2":
      #do option 2 stuff
      print("Option 2 selected")
elif choice == "3" or choice == "Option 3":
      #do option 3 stuff
      option3()
else:
      print("Invalid option")
      print() 
      menu()


print("A Cube Code Project by AccidentalsHappen ©2021")
