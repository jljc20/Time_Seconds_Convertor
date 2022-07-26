#!/usr/bin/env python3

print('\nHello, Welcome to the Converting Time to Seconds program \n')

################################
#     Validating User Input    #
################################

while True:
    try:
        hours = int(input('\nEnter the Hours (0-12): '))

    except ValueError:
        print('\nPlease enter within the range 0-12\n')
    
    if(hours < 0 or hours > 12):
        continue

    else:
        break

while True:
    try:
        mins = int(input('\nEnter the Minutes (0-60): '))

    except ValueError:
        print('\nPlease enter within the range 0-60\n')
    
    if(mins < 0 or mins > 60):
        continue

    else:
        break

while True:
    try:
        secs = int(input('\nEnter the Seconds (0-60): '))

    except ValueError:
        print('\nPlease enter within the range 0-60\n')
    
    if(secs < 0 or secs > 60):
        continue

    else:
        break

while True:
    try:
        day = input('\nEnter AM / PM: ')

    except ValueError:
        print('\nPlease enter only AM / PM\n')
    
    if(day == 'AM' or day == 'PM'):
        break

    else:
        continue

#############################################################################
#  Error checking to ensure no eccess 12 hours is added to the final timing #    #
#############################################################################

hr_check = hours % 12

################################
#     Calculating AM Seconds   #
################################

if (day == 'AM'):
    total_sec = (hr_check * 60 * 60) + (mins * 60) + secs 

################################
#     Calculating PM Seconds   #
################################

else:
    total_sec = (hr_check * 60 * 60) + (mins * 60) + secs + (12 * 60 * 60)
    
################################
#     Printing the Results     #
################################

print('\nThe time is converted to : ' + str(total_sec) +' seconds\n')