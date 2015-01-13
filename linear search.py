#Marc Gonzalez
#08/01/15
#linear search
def linear_search(items, search):
    found = False
    counter = 0
    while not found and counter < len(items):
        if items [counter] == search:
            
            found = True
        else:
            
            counter = counter + 1
    return found

items = ["bacon", "pork", "lamb", "henry", "john" , "babe"]
search = input("what item are you searching for? : ")

found = linear_search(items, search)


if found:
    print("you have found item {0} ".format(search))
else:
    print(" item {0} has not been found".format(search))



    
