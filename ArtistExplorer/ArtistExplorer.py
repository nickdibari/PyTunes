#!/usr/bin/python

#* Nicholas DiBari, Chris George, & Matt Satalino                   *#
#* Artist Explorer                                                  *#
#* Finds information on a given artist                              *#
#  ----------------------------------------------------------------- #                                             
#* Implemented Features:                                            *#
#* Opens different webpages for a given artist                      *# 
#* Saves previous entries into database                             *#
#  ----------------------------------------------------------------- #
#* TODO                                                             *#
#* Use Spotify API to suggest new artists based on previous entries *#

import webbrowser
import sys
import shelve

#Creates database file of artists to be entered
artistFile = shelve.open('Entries.db')

#Initializes prev_entries to the list value of the contents of artistFile
prev_entries = list(artistFile.values())
prev_entries.sort()

#Prompts user to decide which option to choose
while(True):
    choice=raw_input('Please decide which input you would like.\n1.Enter a new artist\n2.View previous entries\n')

    if choice == ('1'):
        #Get artist to search
        artist=raw_input('Please enter an artist to search for: ')
        break
    
    elif choice == ('2'):
        #Show user previous entries
        print('You have previously entered:')
        for i in range(len(prev_entries)):
            print (str(i+1) + ('. ') + prev_entries[i])
        choice=raw_input('Which artist would you like to see? Please choose the number: ')
        choice = int(choice)
        while choice>len(prev_entries) or choice<0:
            choice=raw_input('Not a valid input. Please enter a number within the range of the list: ')
        choice = choice-1
        artist = prev_entries[choice]
        break
    
    else:
        choice=raw_input('That is an invalid input. Please input 1 for a new artist or 2 to view previous entries ')
#If user wants to, opens ultimate guitar page as well
choice=raw_input('Do you want to see the guitar explorer page for ' +artist +'? (y/n) ')
print('Loading...')

#Genius page
webbrowser.open('http://genius.com/search?q={0}'.format(artist))

#Wikipedia page
webbrowser.open('https://en.wikipedia.org/wiki/{0}'.format(artist))

#Youtube Page
webbrowser.open('https://www.youtube.com/results?search_query={0}'.format(artist))

#Soundcloud Page
webbrowser.open('https://soundcloud.com/search?q={0}'.format(artist))

#Ultimate Guitar Page
if choice == 'y' or choice == 'Y':
    webbrowser.open('http://www.ultimate-guitar.com/search.php?search_type=title&value={0}'.format(artist))

#Enters artist entered into the list of previous entries
if artist not in prev_entries:
    prev_entries.append(artist)

#Writes new list of previous entries to the data file
for a in range(len(prev_entries)):
    artistFile['Artist:' + str(a)]=prev_entries[a]

artistFile.close()
