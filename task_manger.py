# Task Number : 1
# File Name : task_manger.py
# Written by : Shaakir Caroto
# Date Written : 21/02/2020
# The function of this program : This program is used for a small business that has a login and allows the user to do multiple tasks 
# like registering user and tasks and stores them in text files


# This opening the user.txt 
# These lines of code (lines 13 - 19 ) are getting the admin's username and password to check if the user enters the admin information
# line 20 is the file being closes for later use 
f_user = open("user.txt","r")
line = f_user.readline()
line = line.replace("\n","")
line = line.split(",")
line[1] = line[1].replace(" ","")
line[1] = line[1].replace("\n","")
admin = line[0]
admin_pass = line[1]
f_user.close()

# line 23 and line 24 are the user inputs for the login in process 
ent_user = input("Enter your username : ")
ent_pass = input("Enter your password : ")

# The following if statement checks if the information input is the admin or another users that does not have the same menu
# else is used for the other user information 
if  (admin_pass == ent_pass) and (admin == ent_user):
   # This while true allows the program to continue running after the user done a function and will end only if the user asks to exit the program
   while True:
      # lines 32 - 42 is the admins menu that will be displayed when they login 
      print(f"Welcome {ent_user}")

      print("Please select one of the following options : ")
      print("=" * 50)
      print("r - register user")
      print("a - add task")
      print("va - view all tasks")
      print("vm - view my tasks")
      print("st - statistics")
      print("e - exit")
      print("=" * 50)
      
      # This is asking for the user to enter what option they would like to input
      option_int = input("Enter which option you would like to use : ").lower()

      # This checks if the user have entered the correct input 
      # if the user has not the program will ask the user for the input again until they answer correctly
      while option_int == "r" or option_int == "a" or option_int == "vm" or option_int == "va" or option_int == "st" or option_int == "e":

       # This is the register option that allows the user to register new users which will be saved in the user text file where all of the usernames and passwords are stored
       # lines 63 -65 tells the user what option they selected 
       # lines 67 - 68 requests the user input for the new users information 
       # lines 70 - 80 are used for the vaildation of the new users password and uses a while true in line 63 if the user input the password incorrectly the second time
       # there will be a message displayed and the the input prompt will be asked again
       # if the user inputs it in correctly then the loop will break and the useer can continue
       # lines 82 - 86 the new username and password will be stored in the user text file and is ready for the new user
       # lines 88 - 96 is an input prompt asking if the user would like to enter another user 
       # if the user inputs yes the process will repeat
       # if the user inputs no the program will go back to the menu and can exit from there or continue in the program
       if option_int == "r":

          print("=" * 50)
          print("You have chosen to register a new user")
          print("Please enter the username and the password of the new user")

          new_user = input("Enter the username of the new user : ")
          new_pass = input("Enter the password of the new password : ")

          print("Please enter the password again for vaildation")
          vail_pass = input("Please enter the password of the new user again : ")

          while True:
             if new_pass == vail_pass:
                 print("Thank you")
                 print("You have added a new user")
                 break
             else:
                 print("The passwords are not the same please try again")
                 vail_pass = input("Please enter the password of the new user again : ")

          f_user = open("user.txt","a")
          f_user.writelines("")
          f_user.writelines(f"{new_user}, {new_pass}\n")
          f_user.writelines("")
          f_user.close()

          option_menu = input("Would you like to enter a new user : ").lower()

          if option_menu == "yes":
               print("You have asked to enter a new user")
          elif option_menu == "no":
               print("Have chosen not to enter a new user")
               break
          else:
               print("You have enter the incorrect input")
 
       # This is the add task option that allows the user to add a new task to the task text file 
       # This allows the users to assign another user a task 
       # lines 108 - 110  tells the user what option they have picked and tells the user what is needed from them 
       # lines 112 - 122  requests inputs from the user and also tells the what they need to enter for specific tasks so the correct information is entered
       # task_complete has default of "no" as if it is a new task then it will automaticly will not be complete
       # lines 124 - 162  is an while loop that checks if the user entered something in the variables needed
       # lines 137 - 162  is the else for the while loop if all the questions are answered then the task is written to the task file
       # lines 145 - 159  is an input request asking if the user they would like to enter another task
       # if the user enters "yes" the process will restart
       # if the user enters "no" the process will be broken (lines 153 - 155) and the user will go back to the main menu   
       elif option_int == "a" :
              print("The option you have chosen is to add a new task to the task text file.")
              print("=" * 50)  
              print("This option needs you to add the users name and other details to construct the complete task file.") 

              task_user = input('Enter the name of the user who is going to do the task : ')
              title_task = input("Enter the title of the task : ")
              description_task = input("Enter the description of the task : ")
              print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
              issue_task = input("Enter the current date of the task bing issued  :")
              print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
              due_date_task = input("Enter the date the task is due : ")
              print("Please enter yes or no ")
              task_complete = input("Enter if the task is complete or not : ").lower()
              task_complete = "No"

              while task_user == " " or task_user == "" or title_task == " " or title_task == "" or description_task == " " or description_task == "" or issue_task == " " or issue_task == "" or due_date_task == "" or due_date_task == " " or  task_complete == "" or task_complete == " ":
                 
                  print("Please re-input your answers")
                  task_user = input('Enter the name of the user who is going to do the task : ')
                  title_task = input("Enter the title of the task : ")
                  description_task = input("Enter the description of the task : ")
                  print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
                  issue_task = input("Enter the current date of the task bing issued  :")
                  print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
                  due_date_task = input("Enter the date the task is due : ")
                  print("Please enter yes or no ")
                 
                  task_complete = input("Enter if the task is complete or not : ").lower()
              else:
                 
                  print("You have answered all the questions")
                  f_task = open("tasks.txt","a")
                  f_task.writelines(f"{task_user}, {title_task}, {description_task}, {issue_task}, {due_date_task}, {task_complete.capitalize()}\n")
                  f_task.close()
                  print("The task has been added to the task file")
                 
                  while True:
                 
                     add_task = input("Would you like to add another task : ").lower()
                 
                     if add_task == "yes":
                        print("You have chosen to enter new task")
                        break
                 
                     elif add_task == "no":
                        print("You have chosen not to add another task")
                        break
                 
                     else:
                 
                        print("Please input the correct input")
               
                  break 

       # This is the view all option that allows the user to view will the tasks that are available
       # lines 175 - 178 tells the user what option they have selected in a user friendly manner
       # lines 180 - 201 is the opened and the readed of the task text file
       # in the for loop (lines 181 - 201 ) the lines of the text file are readed and split in seperate variables to be stored for easy reading
       # the if statement (line 185 ) has a break function. This is the program does not crush as it runs out of things to read 
       # when they are assigned they are set to be displayed in print statement (lines 195 - 201 )
       # when that is all done the file is closed (line 203 )
       # the user is when asked if they would like to continue go to the menu or continue reading (lines 205 - 213 )
       # if the user inputs "yes" then the program will go back to the main menu
       # if the user input anything else then the program will continue showing the information above until the user inputs "yes"
       elif option_int == "va" : 

           print("You have chosen to view of the available tasks ")
           print("=" * 50)
           print("Task information")
           print("=" * 50)

           f_task = open("tasks.txt","r")
           for line in f_task:
              line = line.replace("\n","")
              line = line.split(",")

              if line[0] == "":
                 break

              user_assigned = line[0] 
              title = line[1]
              description = line[2]
              date_issued = line[3]
              date_due = line[4]
              task_comp = line[5]

              print(f"The user that this task is assigned : {user_assigned}")
              print(f"The title of the task : {title}")
              print(f"The description of the task : {description}")
              print(f"The date the task is issued : {date_issued}")
              print(f"The due date of the task  : {date_due}")
              print(f"Is the task completed : {task_comp}")
              print("=" * 50)

           f_task.close()

           wait_view = input("Would you like to go to the menu  :  ").lower()

           if wait_view == "yes" :

              print("You have chosen to go to the menu")
              break
           else:

              print("Please input the answer again")

       # This is the view mine option that allows the user to view all of their tasks
       # lines 229 - 230 tells the user whose tasks they are going to view 
       # lines 232 - 259 opens the text file 
       # lines 236 - 237 in the for loop the lines are split into a list 
       # lines 239 -254  uses an if statement to find the user tasks
       # when the user tasks are found the program will assign the correct items to the correct variable 
       # lines 248 - 254 is the display of the user task using print statement
       # if the user can not be found the for loop will break 
       # line 259 the file will close
       # the user is when asked if they would like to continue go to the menu or continue reading (lines 261 - 269 )
       # if the user inputs "yes" then the program will go back to the main menu
       # if the user input anything else then the program will continue showing the information above until the user inputs "yes"
       elif option_int == "vm" : 

          print(f"You have chosen to view your personal tasks of {ent_user}")
          print("=" * 50)

          f_task = open("tasks.txt","r")

          for line in f_task:

             line = line.replace("\n","")
             line = line.split(",")

             if line[0] == ent_user:

                 user_assigned = line[0]
                 title = line[1]
                 description = line[2]
                 date_issued = line[3]
                 date_due = line[4]
                 task_comp = line[5]

                 print(f"The user that this task is assigned : {user_assigned}")
                 print(f"The title of the task : {title}")
                 print(f"The description of the task : {description}")
                 print(f"The date the task is issued : {date_issued}")
                 print(f"The due date of the task  : {date_due}")
                 print(f"Is the task completed : {task_comp}")
                 print("=" * 50) 

             else:
                 break

          f_task.close()

          wait_view = input("Would you like to go to the menu  :  ").lower()

          if wait_view == "yes" :

              print("You have chosen to go to the menu")
              break

          else:
              print("Please input the answer again")

       # This the option statistics that is only available for the admin 
       # This option  allows the user to view the number of task active and the number of users that have been registered to use the program
       # lines 288 - 292 tells the user what option they have entered and what files statistics they are going to see
       # lines 294 - 295 is the openning of the text file and the declaring of a count "i"
       # lines 297 - 298 is a for loop that counts the number of lines there are in the text file 
       # line 300 is the closing of the file
       # line 302 is the display of the files information that has been counted
       # lines 304 - 307 is the introduction to the next text files information
       # lines 309 - 310 is the openning of the next text file and the declaring of a count "y"
       # lines 312 - 313 is a for loop that counts the number of lines that are in the text file 
       # line 315 is the closing of the file
       # line 317 is the display of the files information that has been counted
       # the user is when asked if they would like to continue go to the menu or continue reading (lines 320 - 329 )
       # if the user inputs "yes" then the program will go back to the main menu
       # if the user input anything else then the program will continue showing the information above until the user inputs "yes"
       elif option_int == "st":

           print("You have chosen to see the statistics of the files ")
           print("=" * 50)
           print("\n")
           print("User file statistics:")
           print("="* 50)

           f_user = open("user.txt", "r")
           i = 0

           for line in f_user:
             i += 1

           f_user.close()

           print(f"The total number of users registered to use the program : {i}")

           print("="* 50)
           print("\n")
           print("Task file stactistics:")
           print("=" * 50)

           f_task = open("tasks.txt","r")
           y = 0

           for line in f_task:
              y += 1

           f_task.close()

           print(f"The total number of task active : {y}")
           print("=" * 50)

           wait_view = input("Would you like to go to the menu  : ").lower()

           if wait_view == "yes" :

              print("You have chosen to go to the menu")
              break

           else:

              print("Please input the answer again")
       else:
          # if the user does not enter any of the options and this is the end of the if statement
          break
     
      else:
       # if the user does not enter the correct input  
       print("Please enter the correct option ")
  
      # This is exit option that if the user if done with the program and wish to exit the program
      # the program will display a message and then break the whole while true loop
      if option_int == "e":
         print("You have chosen to exit the program")
         break
else:
   # This is for the other users 
   # Reopen the users text file
   f_user = open("user.txt","r")
  
   # For line in the range of the text file f_user
   # line is getting the spaces and the \n replaced with nothing (lines 354 - 355)
   # line is also being split into a list (line 356)
   # Then a search function is being used to find the correct username and password for the login process (line 358)
   for line in f_user :

      line = line.replace(" ","")
      line = line.replace("\n","")
      line = line.split(",")

      if line[0] == ent_user and line[1] == ent_pass:

         # This while true allows the program to continue running after the user done a function and will end only if the user asks to exit the program
         while True:
           
           # lines 364 - 373 is the other user's menu that will be displayed when they login 
           print(f"Welcome {ent_user}")
           
           print("Please select one of the following options : ")
           print("=" * 50)
           print("r - register user")
           print("a - add task")
           print("va - view all tasks")
           print("vm - view my tasks")
           print("e - exit")
           print("=" * 50)
           
           # This is asking for the user to enter what option they would like to input
           option_int = input("Enter which option you would like to use : ").lower()
           
           # This checks if the user have entered the correct input 
           # if the user has not the program will ask the user for the input again until they answer correctly
           while option_int == "r" or option_int == "a" or option_int == "vm" or option_int == "va" or option_int == "e":

            # This is the register option but this user is unable to use is function 
            # this will get the user an error message and ask the user to go back to the menu
             if option_int == "r":
                print("You are unable to use this function are you are not an admin")
                print("Please go back to the menu")

                wait_view = input("Would you like to going to the menu: ").lower()

                if wait_view == "yes" :

                     print("If you want to register a new user please contact the admin of the program")
                else:

                     print("If you want to register a new user please contact the admin of the program")

                break

            # This is the add task option that allows the user to add a new task to the task text file 
            # This allows the users to assign another user a task 
            # lines 412 - 414 tells the user what option they have picked and tells the user what is needed from them 
            # lines 416 - 424 requests inputs from the user and also tells the what they need to enter for specific tasks so the correct information is entered
            # task_complete has default of "no" as if it is a new task then it will automaticly will not be complete
            # lines 426 - 464 is an while loop that checks if the user entered something in the variables needed
            # lines 439 - 464 is the else for the while loop if all the questions are answered then the task is written to the task file
            # lines 447 - 462 is an input request asking if the user they would like to enter another task
            # if the user enters "yes" the process will restart
            # if the user enters "no" the process will be broken (lines 456 - 462) and the user will go back to the main menu   
             elif option_int == "a":

                 print("The option you have chosen is to add a new task to the task text file.")
                 print("=" * 50)  
                 print("This option uses you to add the users name and other details to construct the complete task file.")  

                 task_user = input('Enter the name of the user who is going to do the task : ')
                 title_task = input("Enter the title of the task : ")
                 description_task = input("Enter the description of the task : ")
                 print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
                 issue_task = input("Enter the current date of the task bing issued  :")
                 print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
                 due_date_task = input("Enter the date the task is due : ")
                 print("Please enter yes or no ")
                 task_complete = input("Enter if the task is complete or not : ").lower()

                 while task_user == " " or task_user == "" or title_task == " " or title_task == "" or description_task == " " or description_task == "" or issue_task == " " or issue_task == "" or due_date_task == "" or due_date_task == " " or  task_complete == "" or task_complete == " ":

                    print("Please re-input your answers")
                    task_user = input('Enter the name of the user who is going to do the task : ')
                    title_task = input("Enter the title of the task : ")
                    description_task = input("Enter the description of the task : ")
                    print("Please the date in the format dd month yyyy: for example 10 Oct 2020")  
                    issue_task = input("Enter the current date of the task bing issued  :")
                    print("Please the date in the format dd month yyyy: for example 10 Oct 2020")
                    due_date_task = input("Enter the date the task is due : ")
                    print("Please enter yes or no ")
                    task_complete = input("Enter if the task is complete or not : ").lower()

                 else:

                    print("You have answered all the questions")
                    f_task = open("tasks.txt","a")
                    f_task.writelines(f"\n{task_user}, {title_task}, {description_task}, {issue_task}, {due_date_task}, {task_complete.capitalize()}\n")
                    f_task.close()
                    print("The task has been added to the task file")

                    while True:

                      add_task = input("Would you like to add another task : ").lower()

                      if add_task == "yes":

                         print("You have chosen to enter new task")
                         break

                      elif add_task == "no":

                         print("You have chosen not to add another task")
                         break

                      else:
                         print("Please input the correct input")
               
                    break

            # This is the view all option that allows the user to view will the tasks that are available
            # lines 479 - 482 tells the user what option they have selected in a user friendly manner
            # lines 484 - 508 is the opened and the readed of the task text file
            # in the for loop (lines 486 - 508 ) the lines of the text file are readed and split in seperate variables to be stored for easy reading
            # the if statement (line 492 ) has a break function. This is the program does not crush as it runs out of things to read 
            # when they are assigned they are set to be displayed in print statement (lines 501 - 507 )
            # when that is all done the file is closed (line 509 )
            # the user is when asked if they would like to continue go to the menu or continue reading (lines 511 - 517)
            # if the user inputs "yes" then the program will go back to the main menu
            # if the user input anything else then the program will continue showing the information above until the user inputs "yes"
             elif option_int == "va":

                  print("You have chosen to view of the available tasks ")
                  print("=" * 50)
                  print("Task information")
                  print("=" * 50)

                  f_task = open("tasks.txt","r")

                  for line in f_task:

                     line = line.replace("\n","")
                     line = line.split(",")
                     user_assigned = line[0]

                     if line[0] == "":
                        break

                     title = line[1]
                     description = line[2]
                     date_issued = line[3]
                     date_due = line[4]
                     task_comp = line[5]

                     print(f"The user that this task is assigned : {user_assigned}")
                     print(f"The title of the task : {title}")
                     print(f"The description of the task : {description}")
                     print(f"The date the task is issued : {date_issued}")
                     print(f"The due date of the task  : {date_due}")
                     print(f"Is the task completed : {task_comp}")
                     print("=" * 50)

                  f_task.close()

                  wait_view = input("Would you like to go to the menu  :  ").lower()

                  if wait_view == "yes" :
                     print("You have chosen to go to the menu")
                     break
                  else:
                     print("Please input the answer again")

            # This is the view mine option that allows the user to view all of their tasks
            # lines 531 - 532 tells the user whose tasks they are going to view 
            # lines 534 - 558 opens the text file 
            # lines 538 - 539 in the for loop the lines are split into a list 
            # lines 541 - 558 uses an if statement to find the user tasks
            # when the user tasks are found the program will assign the correct items to the correct variable 
            # lines 550 - 556 is the display of the user task using print statement
            # if the user can not be found the for loop will break 
            # line 558 the file will close
            # the user is when asked if they would like to continue go to the menu or continue reading (lines 560 - 566 )
            # if the user inputs "yes" then the program will go back to the main menu
            # if the user input anything else then the program will continue showing the information above until the user inputs "yes"
             elif option_int == "vm" :

                 print(f"You have chosen to view your personal tasks of {ent_user}")
                 print("=" * 50)

                 f_task = open("tasks.txt","r")

                 for line in f_task:

                   line = line.replace("\n","")
                   line = line.split(",")

                   if ent_user in line:

                      user_assigned = line[0]
                      title = line[1]
                      description = line[2]
                      date_issued = line[3]
                      date_due = line[4]
                      task_comp = line[5]

                      print(f"The user that this task is assigned : {user_assigned}")
                      print(f"The title of the task : {title}")
                      print(f"The description of the task : {description}")
                      print(f"The date the task is issued : {date_issued}")
                      print(f"The due date of the task  : {date_due}")
                      print(f"Is the task completed : {task_comp}")
                      print("=" * 50)

                 f_task.close()

                 wait_view = input("Would you like to go to the menu  :  ").lower()

                 if wait_view == "yes" :
                     print("You have chosen to go to the menu")
                     break
                 else:
                     print("Please input the answer again")
                     
             else:
                # This is the break for the if statement
                break
           else:
              # if the user does not enter the correct option
               print("Please enter the correct option")

           # This is exit option that if the user if done with the program and wish to exit the program
           # the program will display a message and then break the whole while true loop
           if option_int == "e":
               print("You have chosen to exit the program")
               break
   else:
      # This is the else for the for loop if the program is unable to find the user
      # It will display an error message to the user
      if line[0] != ent_user and line[1] != ent_pass:
        print('Username not found')
      
