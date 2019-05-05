#  ®All rights reserved.
#   This material can only be modified for educational reasons and it can only be used if credit is given to the creator.

#-------Startup Variables-------
import time
import os

name = []
number = []
address = []
email = []

x = 0
i = 0
user_input = " "
#-------------------------------

#-------Main Code-------
time.sleep(1)
print "Hello there,"
time.sleep(1)
print "This is a basic contacts log and that means it can only hold 20 deferent contacts."
time.sleep(3)
print "If at any time you wish to exit type (exit)."
time.sleep(3)
print "If you exit all of your data will be lost."
time.sleep(5)

while user_input != "exit":

    print

    os.system('cls')

    print

    user_input = raw_input("Would you like to (make) or (read) a contact: ")

    if user_input == "make":
        user_input = raw_input("Give the contacts full name: ")
        name.append(user_input)
    
        user_input = raw_input("Give the contacts number: ")
        number.append(user_input)

        user_input = raw_input("Would you like to add an address on the contact? (yes/no): ")

        if user_input == "yes":
            user_input = raw_input("Give the contacts address: ")
            address.append(user_input)

        elif user_input == "no":
            print "No address will be placed on this contact"
            address.append("None")

        user_input = raw_input("Would you like to add an email on the contact? (yes/no): ")

        if user_input == "yes":
            user_input = raw_input("Give the contacts email: ")
            email.append(user_input)

        elif user_input == "no":
            print "No email address will be placed on this contact"
            email.append("None")
        
        time.sleep(2)

    elif user_input == "read":
        if name != []:
            print

            for elem in name:
                print x,".",elem
                x=x+1

                print

                user_input = input("Give the corresponding number of the contact you would like to see: ")
                i = user_input

                print

                print "Name: ",name[i]
                print "Number: ",number[i]
                print "Address: ",address[i]
                print "Email: ",email[i]
        
                time.sleep(5)

                print
                
                user_input = raw_input("When ready please press enter to continue")

        else:
            print
            print "There are no contacts. You could create one and it will appear here."
            time.sleep(3)

os.system('cls')

print

print "You are about to exit!"
time.sleep(1)
print "Good bye!"
time.sleep(3)
exit()
#-----------------------
