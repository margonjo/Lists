shopping_list = [] #The actual shopping list
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")#input
    if shopping_item == "-1":#repeat until
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

for index, lists in enumerate(shopping_list):
    print("item {0} is {1}".format(index+1,lists ))
