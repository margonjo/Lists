#Marc Gonzalez
#20/12/14
#dev 1

countries=['spain','france', 'hugary', 'italy', 'germany' , 'russia','slovenia','norway', 'china','japan']

capital=['madrid','paris','budapest','rome','berlin', 'moscow','ljubljiana', 'oslo','beijin','tokyo']

for count in range(10):
    print("{0:<14}{1:<14}".format(countries[count], capital[count]))

import random

country = random.randint(0,10)
print("what is the capital of {0}: ".format(countries[country]))

answer = input("")

if answer == capital[country]:
    print("congratulations correct!")

else:
    print(" wrong answer")
