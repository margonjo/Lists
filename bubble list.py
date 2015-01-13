#Marc Gonzalez
#08/01/15
#bubble sort

def bubble_list(items):
    swap = True 
    while swap:
        count = 0
        swap = False
        while count < len(items)-1:
            if items[count] > items[count+1]:
                temp = items[count]
                items[count] = items[count+1]
                items[count+1] = temp

                count = count +1
                swap = True
            else:
                count = count + 1







items = ["bacon", "pork", "lamb", "henry", "john" , "babys"]

bubble_list(items)
print(items)
