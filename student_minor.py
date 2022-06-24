#print the menu
print ("Select option form Menu\n---------------------------")
print("1. Login")
print("2. Create User")

#get the option the user selected
while True:
    user_option = input("Would you like to 1. Login or 2. Create an account? ")
    #ensure the user entered a valid option (1 or 2)
    if user_option != "1" and user_option != "2":
        #-if not, promp user again
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("you done good buddyboi")
        break

#if user chose 1, ask for user name and password and 
if user_option == "1":
    while True:
        user_name = input("Please enter your user name ")
        user_pass = input("Please enter your password ")
        #open the user's file
        user_file = open("users.txt", "r")
        for line in user_file:
            print(line)
#- validate username and password combination in the user.txt file
#-if not valid combination reprompt the user
#- if valid then move on to prompt for student data
#If user chose 2, ask for user name and password and
#- validate username and password length. If va;id, writ to users.xt file
#- and move on
#If not valid re prompt user

#ask user how many students to enter data
# prompt user to enter student name and number score
#store data somewhere
#convert the number score to a letter grade

#print sutdent data(name,score,grade)
#calculate and print class average
