#! /usr/bin/python3.4

#* Nicholas DiBari & Chris George                                                     *#
#* ScaleFinder                                                                        *#
#* Program to display scale for given note                                            *#
#* ----------------------------------------------------------------------------------- #
#* Implemented Features:                                                              *#
#* Ability to search for a scale based on a given chord and its position in the scale *#
#* Ability to search for a scale based on a list of chords provided                   *#
#* Calls scales from created database                                                 *#
#* Show relative minor scale                                                          *#
#* ----------------------------------------------------------------------------------- #
#* TODO                                                                               *#
#* Show fingering positions of chords within a key                                    *#
#* Show 7th Notes                                                                     *#
#*      7s on all chords except the 5th, which is a dominant 7th                      *#


import shelve


# 1. Creates list of scales from database
scalefile=shelve.open("Scales")
scales=list(scalefile.values())
scales.sort()
    
# 2. Prompts User for input
def GetNote():


    chord = ' '
    chords_entered = []
    for a in range(20):
        print (" ")
    print ('Please pick your input choices: ')
    print ('1. Display specific scale')
    print ('2. Enter multiple chords to find scale')
    choice = int(input())
    while True:
        #Position/Chord Initialized
        if choice == 1:
            chord = input("Please input what scale you would like to view " )
            CheckScalePOS(chord)
            break
        
        
        #List of chords Initialized
        if choice == 2:
            print ("Please input the chords in your scale (enter done to exit)")
            for b in range(6):
                entry = input()
                if entry == 'done':
                    break
                chords_entered.append(entry)
            CheckScaleCHORDS(chords_entered)
            break
        
        else:
            choice=input("That's not a valid input. Please try again")
        

# 3A. Checks Input against scales List (POS/CHORD)
def CheckScalePOS(chord):
    for a in range (len(scales)):
        if (chord == scales[a][0]):
            DisplayScale(scales[a])


# 3B. Checks Input against scales List (CHORDS)
def CheckScaleCHORDS(chords_entered):
    for a in range (len(scales)):
        hold = scales[a]
        if set(chords_entered) < set(hold):
            DisplayScale(hold)

    

# 4. Displays required scale
def DisplayScale(found):
    print (' ')
    print ("You're in the " + found[0] + " scale:")
    for i in range(len(found)):
        print(found[i])
    print(" ")
    
    #If user chooses, also displays the relative Minor scale
    choice = input("Would you like to see the relative minor scale for " + found[0] + "? (y/n): ")
    print(" ")
    if choice == 'y' or choice == 'Y':
        print("The " + found[-2] + " scale:")
        for i in range(len(found)):
            print(found[i-2])

GetNote()
