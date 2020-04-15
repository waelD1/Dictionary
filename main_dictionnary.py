import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open('data.json'))

def definition(dictio, keys):
    if keys in dictio:
        return dictio.get(keys) 

word = input('Enter a word : ')  
word = word.lower() # Definitions are in lower case in the database.

if word in data:
    if type(definition(data, word)) == list:
        for elem in definition(data, word):
            print(elem)
    else:
        print(definition(data, word))

elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
    if type(definition(data, word.title())) == list:
        for elem in definition(data, word.title()):
            print(elem)
    else:
        print(definition(data, word.title()))

elif word.upper() in data: #in case user enters words like USA or NATO
    if type(definition(data, word.upper())) == list:
        for elem in definition(data, word.upper()):
            print(elem)
    else:
        print(definition(data, word.upper()))
        
else:
    while word not in data:
        if len(get_close_matches(word, data.keys(), n=3, cutoff=0.85)) > 0:
            Reps = input(f'Do you mean one of this word : {get_close_matches(word, data.keys(), n=3)} ? Enter y or n: ')
            if Reps == 'y':
                for elem in get_close_matches(word, data.keys(), n=3):
                    Reps_precision = input(f'Do you mean this word : {elem} ? Enter y or n: ')
                    if Reps_precision == 'y':
                        word=elem
                        break
                    
            elif Reps == 'n':
                print('The word is not in the dictionary. Please enter an other word')            
                word = input('Enter a word : ').lower()
            else : 
                print('Enter only y or n : ')
        else:
            print('The word is not in the dictionary. Please enter an other word')            
            word = input('Enter a word : ').lower()

    if type(definition(data, word)) == list:
        for elem in definition(data, word):
            print(elem)
    else:
        print(definition(data, word))








            









