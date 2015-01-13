# Program to search for a name in a list

NamesList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']
found = False
name = input('Enter the name you are searching for : ')
while found == False:
    
    if name in NamesList:
        print('{0} was in element {1} in the list'.format(name, count))
        found = True


    else:
         
if found == False:
    print("Not found")
    
