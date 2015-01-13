#Marc Gonzalez
#06/01/15
#2d

k1llmAchine = ["k1llmAchine","51","49"]
bob7424 = ["bob7424","5","99"]
hAxOr12 = ["hAxOr12","72","30"]

table = [k1llmAchine, bob7424, hAxOr12]
print("|--------------|---------------|---------------|")

print("|{0:<14}| {1:<14}| {2:<14}|" .format("Name", "Kills" , "Deaths"))
print("|--------------|---------------|---------------|")
count= 0 
for thing in table:
    print("|{0:<14}| {1:<14}| {2:<14}|".format( table[count][0] , table[count][1] ,table[count][2]))

    print("|--------------|---------------|---------------|")

    count = count+1
