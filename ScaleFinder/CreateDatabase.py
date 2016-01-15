#! /usr/bin/python3.4

#* Nicholas DiBari                                                 *#
#* CreateDatabase                                                  *#
#* Creates a database of scales for Scale_Finder to search through *#
# ----------------------------------------------------------------  #
#* Implemented Features:                                           *#
#* Functional Prototype                                            *#
# ----------------------------------------------------------------  #
#* TODO:                                                           *#
#* Extend scales to include different scale shapes                 *#
#*      Lydian, Dorian, Acoustic, etc.                             *#

import shelve

scaleFile = shelve.open('Scales')

# Lists of common scales
AMaj = ['A Major' , 'B Minor' , 'C# Minor' , 'D Major' , 'E Major' , 'F# Minor' , 'G# Diminished']
BMaj = ['B Major' , 'C# Minor' , 'D# Minor' , 'E Major' , 'F# Major' , 'G# Minor' , 'A# Diminsihed']
CMaj = ['C Major' , 'D Minor' , 'E Minor' , 'F Major' , 'G Major' , 'A Minor' , 'B Diminished']
DMaj = ['D Major' , 'E Minor' , 'F# Minor' , 'G Major' , 'A Major' , 'B Minor' , 'C# Diminished']
EMaj = ['E Major' , 'F# Minor' , 'G# Minor' , 'A Major', 'B Major', 'C# Minor', 'D# Diminished']
FMaj = ['F Major' , 'G Minor' , 'A Minor' , 'Bb Major' , 'C Major' , 'D Minor' , 'E Diminished']
GMaj = ['G Major' , 'A Minor' , 'B Minor' , 'C Major' , 'D Major' , 'E Minor' , 'F# Diminished']
Major = [AMaj, BMaj, CMaj, DMaj, EMaj, FMaj, GMaj] 

#Master list of all available scales
MASTER = [Major]


#Write Scales to database file
for a in range(len(MASTER)):
    for b in range(len(MASTER[a])):
        print("Adding the " + str(MASTER[a][b][0]) + " scale")
        scaleFile["Scale: " + str(b)] = MASTER[a][b]
      

print("Done!")
