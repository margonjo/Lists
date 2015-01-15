##def asklist():
##    lists = int(input("how many lists would you like: "))
##    for thing in range(lists):
##        
##    
##    items = int(input("please eneter how many items will be in your list: "))
##    table = []
##
##    for question in range(items):
##        answer = input("what item would you like to add: ")
##        table.append(answer)
##
##    print(table)
##asklist()

length = 0
def getlength(nestedlist):
    length = 0
    for item in nestedlist[0]:
        if len(item) > length:
            length = len(item)
        
    print(length)


nestedlist = [["123346","122675"],["1234", "12345678","1"]]

getlength(nestedlist)


