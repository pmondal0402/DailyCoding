#!/bin/bash

# Read file.txt and output all phone number to stdout
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# Note :
# -P --> Pass
# \d --> digit 
# ^d--> This is used to count the amount of lines (in file or from a pipe)
# that start with a d.
# | --> add another command 
