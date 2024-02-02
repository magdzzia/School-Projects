#!/bin/bash

# Input a trial password to the script as a command-line interpreter
# Must Meet: min. 8 length, min 1 numeric digit, must contain a non-alphabetic character (@,#,$,%,&,*,+,-,=)

if [ "$#" = 0 ] ; then # Checking for if there are 0 arguments in command-line interpreter
 echo "Enter a password" # Echo and read password because '$' and '&' don't work in arguments
 read password

# Echo and read password were done because $, &, ! , ^, *, werent able to be processed without error as a command-line argument.
# The user would have to input single quotes '' around the password in order for it to work without having to do echo read.
# However, there is no way to validate the user inputting '' around the command-line argument.
# If the user were to put single quotes around the command-line argument, the proper code would be as follows:

# if [ "$#" = 1 ] ; then # Checking for if there is 1 argument in command-line interpreter
# ...
# ... Same code as down below
# ...
# else
  # echo 'Please provide only 1 password as a command-line argument.' # Telling the user to input # only 1 argument into the command line
  # exit 1
# fi
       if [ "${#password}" -ge 8 ] ; then  # Checking for min. 8 characters
         if [[ "$password" =~ [0-9] ]] ; then # Checking for any digits between 0-9
           if [[ "$password" =~ ['@#$%&*+-='] ]] ; then # Checking for any special characters
             echo "This password is a good password!"
             exit 0
           else
             echo "Password must contain a non-alphabetic (@,#,$,%,&,*,+,-,=) character!" # User must have non-alphabetic characters
             exit 4
           fi
         else
           echo "Password must contain a numeric digit!" # User must have a digit
           exit 3
         fi 
       else 
         echo "Password must have min. 8 characters!" # User must have min. 8 length
         exit 2
       fi 
  
else 
  echo "Please execute the script without any arguments." # Telling user execute the script without argument
  exit 1
fi 


