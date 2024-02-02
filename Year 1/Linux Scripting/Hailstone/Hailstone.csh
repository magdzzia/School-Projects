#!/bin/tcsh

if ($# == 1) then # Only one argument
  if ( "$1" !~ *[0-9]*[A-Za-z]* ) then # Checking for improper input in the syntax [number][letter]
    if ( "$1" !~ *[A-Za-z]*[0-9]*[A-Za-z]* ) then # Checking for improper input in the syntax [letter][number][letter]
      if ( "$1" !~ *[A-Za-z]*[0-9]* ) then # Checking for improper input in the syntax [letter][number]
        if ( "$1" !~ *[A-Za-z]* ) then # Checking for improper input in the syntax [letter]
          if ( "$1" != 0 ) then # Can't use 0 for hailstone
            if ($1 % 2 == 0) then # Odds or even ( This is the even section)
              @ integer= "$1"
              echo "$integer"
              while ($integer != 1)
                if ($integer % 2 == 0) then
                  @ integer= $integer / 2
                  echo "$integer"
                else if ($integer % 2 != 0) then
                  @ integer= (3 * $integer + 1)
                  echo "$integer"
                endif
              end
            else if ($1 % 2 != 0) then # Odds or even ( This is the odd section)
              @ integer= "$1"
              echo "$integer"
              while ($integer != 1)
                if ($integer % 2 == 0) then
                  @ integer= $integer / 2
                  echo "$integer"
                else if ($integer % 2 != 0) then
                  @ integer= (3 * $integer + 1)
                  echo "$integer"
                endif
              end
            endif
          else
            echo "Please do not put any 0's in"
          endif
        else 
          echo "Please put only numbers in"
        endif
      else
        echo "Please put only numbers in"
      endif
    else 
      echo "Please put only numbers in"
    endif
  else
    echo "Please put only numbers in"
  endif
else
  echo "Please put only 1 integer in"
endif  
