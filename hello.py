#tutorial done through cs50 live
import re
name = input('Please enter your name: ')
#names = name.lower().split()
#\s means a space the dot means any character
#^ means it has to start with this 
# $ it has to end with this

# fromt the carrot start at the beggining then give me a 
# capitol or lowercase O, followed by ctavio and 
# then \s give me one or more spaces to seperate it from everything else
# then optionaly give me (.+\s)*  0 or more times the 
#following stuff, any character with one or more space seperating it
# paranthesis indictes its optional so the middle name is not required
# then give me a cap or lower case S followed by errano and $= end of string
# so here we compare the left to the right 'name'

# add a flags parameter orf re.IGNORCASE 
#if re.search(r'^[Oo]ctavio\s+(.+\s)*[Ss]errano$', name):
if re.search(r'^octavio\s+(.+\s)*serrano$', name, re.IGNORECASE):
    print('Hello, ' + name.title() + ' :(')
#lower used to canonicalize data input
#lower returns a new string refactored to use capitalize
#.capitalize() goes one step further and canonicalize's and 
#makes it grammatically correct
#if names[0] == 'octavio' and names[-1] == 'serrano':
    #print('Hello, ' + name.title() + ' :(')
else:
    print('Hello, ' + name.title() + '!')
    
    
#name = input('Please enter your name: ')
#names = name.lower().split()

#if names[0] == 'octavio' and names[-1] == 'serrano':
    #print('Hello, ' + name.title() + ' :(')
    
#else:
    #print('Hello, ' + name.title() + '!')
    

