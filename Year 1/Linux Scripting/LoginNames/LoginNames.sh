#!/bin/bash

# Takes list of login names of your computer as command-line arguments
# Display login names + Full name + User ID (found in /etc/passwd), one per line
# If login is not valid (not in etc), display login name and error message

# Login name ; password ; user id ; group id; user info; home directory ; loginshell

IFS=":" # Creating a delimiter to separate the strings in the /etc/passwd 

if [ $# = 0 ]; then # Checking for minimum 1 argument 
  echo "Please provide at least 1 login name"
  exit 1
else 
  for login_name in "$@"; do # Creating a for loop to iterate of "$@" elements
    found=false # Creating a flag
    while read user password userid groupid userinfo homedir defshell; do # Seperating sections of /etc/passwd with IFS and read
      if [ "$login_name" == "$user" ]; then # Checking if the names match
        echo "Login name: $user, Full Name: $userinfo, User ID: $userid"
        found=true # Setting the flag to true in order to reiterate
      fi
    done < /etc/passwd # The loop will execute coming from the /etc/passwd
  if [ "$found" == false ]; then # Stating if flag is false, leading to name not being found because names didn't match
    echo "Error: $login_name not found in /etc/passwd."
  fi
done
fi


