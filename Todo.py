# This program creates a todo list and follows your command

def todo_prep():
  print("--------------------")
  print("    MY TODO APP     ")
  print("--------------------")
  print("P. PRINT MY TODO LIST")
  print("A. ADD A NEW TODO TO MY LIST")
  print("D. DELETE A TODO FROM MY LIST")
  print("--------------------")
  user_option = input("Pick an option (P, A, D):")
  print("--------------------")

todo_prep()

user_input = input("Enter a new item to your todo list:\n")

todo_list = ["1. Do your python homework", user_input]

todo_values = ["P", "A", "D"]

def todo_validation():
  user_option = input("Pick an option (P, A, D):")
  while user_option != todo_values:
    print("Invalid Option")
    print(user_option)
  if  todo_list == todo_values[0]:
    print(todo_list)
  if user_option == todo_values[1]:
    todo_list.append()
    print(user_input + "is added to your todo list")
  if user_option == todo_values[2]:
    todo_list.remove
    print(user_input + "is removed from your todo list")

todo_validation()
