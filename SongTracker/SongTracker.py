#! /usr/bin/python3.4

#* Nicholas DiBari                      *#
#* Song Tracker                         *#
#* Logs user progress on multiple songs *#
#  ------------------------------------- #
import shelve

#1  Class defintion of Song Type
class Song:
    def __init__(self):
        name = " "
        tempo = 0
        key = " "
        thoughts = " "
        todo = " "
        instruments = " "
        sample = " "    

#Declares list of songs previously entered
song_File = shelve.open('Songs.db')

#Get previous entries from database
entries= list(song_File.values())
entries.sort()

#   Clear Screen
for i in range(25):
    print (" ") 
print("Welcome to Song Tracker!")    


#2. Print entire list of songs
def PrintList(entries):
    print(" ")
    #If list is empty, tell user that the list is empty
    if not entries:
        print("Your list is empty! Add at least one song first.")
    
    #Print contents of all songs in list
    for i in range(len(entries)):
        print("Song: " + entries[i].name)
        print("Tempo: " + str(entries[i].tempo) + " bpm")
        print("Key: " + entries[i].key)
        print("Thoughts: ") 
        print(entries[i].thoughts)
        print("ToDo: ") 
        print(entries[i].todo)
        print("Instruments used: " + entries[i].instruments)
        print("Sample song: " + entries[i].sample)
        print(" ")
    print(" ")
    

#3. Add song to list
def AddSong(entries):    
    newSong = Song()
    newSong.name = input("Please enter the name of your song: ")
    newSong.tempo=input("Please enter the tempo of your song: ")
    newSong.key=input("Now enter the key of your song (if applicable): ")
    #Wanted to leave enough room for the ideas section
    print("Enter some thoughts on your song (mood, genre, ideas, etc.): ")
    newSong.thoughts=input()
    #Ditto for the to do list
    print("The todo list of your song (separate with commas): ")
    newSong.todo=input()
    newSong.instruments=input("Enter the instruments used in your song: ")
    newSong.sample=input("Enter the name of your sample (if applicable): ")
    entries.append(newSong)

#4. Edit a song in the list
def EditSong(entries):
    print(" ")
    #If the list is empty, return to the main menu
    if not entries:
        print("Your list is empty! Add at least one song first.")
        
    else:
        print("Please pick a song to edit: ")
        #Prints names of all songs
        for i in range(len(entries)):
            print(str(i+1)+". "+entries[i].name)
        
        #Gets desired song to change
        choice = int(input())
        choice -= 1
        
        #Displays chosen song to edit
        print("You want to edit " + entries[choice].name)
        
        
        #Loop to edit multiple pieces of information
        while True:
            #Prompts user to pick what information to edit
            print("Please select what information you would like to edit: ")
            print("1. Name")
            print("2. Tempo")
            print("3. Key")
            print("4. Notes")
            print("5. Todo")
            print("6. Instruments")
            print("7. Sample Name")
            print("8. Exit")
            pick = int(input())
            if pick == 1:
                entries[choice].name=input("Name: ")
            elif pick == 2:
                entries[choice].tempo=input("Tempo: ")
            elif pick == 3:
                entries[choice].key=input("Key: ")
            elif pick == 4:
                print("Thoughts: ")
                entries[choice].thoughts=input()
            elif pick == 5:
                print("Todo (separate with commas): ")
                entries[choice].todo=input()
            elif pick == 6:
                entries[choice].instruments=input("Instruments: ")
            elif pick == 7:
                entries[choice].sample=input("Sample Name: ")
            elif pick == 8:
                break
            else:
                print("That is an invalid entry. Please pick a valid option")
        choice=input("Would you like to edit another song? (y/n): ")
        if choice == 'y':
            EditSong(entries)
        print(" ")


#5. Delete a song from the list
def DeleteSong(entries):
    print(" ")
    #If list is empty, return to main menu
    if not entries:
        print("Your list is empty! Add at least one song first.")
    
    #Prompt user to select which song to delete
    print("Which song would you like to delete?")
    for i in range(len(entries)):
        print(str(i+1)+". "+entries[i].name)
    choice = int(input())
    choice = choice-1
    confirm=input("Are you sure you want to delete " + entries[choice].name + "? (y/n) ")
    if confirm == 'y':
        del entries[choice]
    
#6. Search for a song in the list
def SearchList(entries):
    #If tere are no entries, return to main menu
    if not entries:
        print("Your list is empty! Add at least one song first.")
    
    else:
        #Prompt user for search key
        print("Please select the search key: ")
        print("1. Name")
        print("2. Key")
        print("3. Instruments")
        print("4. Sample Name")
        key=int(input())
        #Name search
        if key == 1:
            name_search=input("Please enter the name of the song: ")
            for i in range(len(entries)):
                if entries[i].name == name_search:
                    hold = entries[i]
        #Key search
        elif key == 2:
            key_search=input("Please enter the key of the song: ")
            for i in range(len(entries)):
                if entries[i].key == key_search:
                    hold = entries[i]    
        #Instrument search
        elif key == 3:
            instrument_search=input("Please enter the instruments of the song: ")
            for i in range(len(entries)):
                if entries[i].instruments == instruments_search:
                    hold = entries[i] 
        #Sample search
        elif key == 4:
            sample_search=input("Please enter the name of the sample used in the song: ")
            for i in range(len(entries)):
                if entries[i].key == key_search:
                    hold = entries[i] 
        #Print the found song
        print(" ")
        print("I found " + hold.name + " that matched your search:")
        print("Song: " + hold.name)
        print("Tempo: " + str(hold.tempo) + " bpm")
        print("Key: " + hold.key)
        print("Thoughts: ") 
        print(hold.thoughts)
        print("ToDo: ") 
        print(hold.todo)
        print("Instruments used: " + hold.instruments)
        print("Sample song: " + hold.sample)
        print(" ")
    


#7. Main Loop
def MainLoop():    
    #Main Menu
    while True:
        print(" ")
        print("What would you like to do?")
        print("1. Print all Songs")
        print("2. Add a new song to the list")
        print("3. Edit a song in the list")
        print("4. Delete a song from the list")
        print("5. Search for a song in the list")
        print("6. Exit program")
        choice = int(input())
        if choice == 1:
            PrintList(entries)
        elif choice == 2:
            AddSong(entries)
        elif choice == 3:
            EditSong(entries)
        elif choice == 4:
            DeleteSong(entries)
        elif choice == 5:
            SearchList(entries)
        elif choice == 6:
            break
        else:
            choice=input("That is not a valid input. Please enter a number from the options ")
    print("Goodbye!")
    
    

MainLoop()
#Saves entries into database
for a in range(len(entries)):
    song_File["Song: " + str(a)]=entries[a]
song_File.close()
