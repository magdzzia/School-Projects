#!/bin/tcsh

if ( $# == 1 ) then # Checks for only one argument
  if ( -d "$1" ) then
    cd "$1" # Enters the directory
    find . -type f -size 0 -delete # Recursively deletes file size 0
    rm -r *.tmp # Recursively deletes .tmp files
    rm -r *.swp  # Recursively deletes .swp files
    tar -cf cleaned_directory.tar . 
    gzip cleaned_directory.tar 
    scp ./cleaned_directory.tar.gz magdziaa@atlas.sheridanc.on.ca:~ # SCPs tar'd file to my remote server
  else
    echo "Please make sure you input a directory"
  endif 
else
  echo "Please only put 1 directory"
endif
