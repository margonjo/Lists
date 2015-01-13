#Marc Gonzalez
#13/1/15
#dev 1

countries=['Spain','France', 'Hungary', 'Italy', 'Germany' , 'Russia','Slovenia','Norway', 'China','Japan']

capital=['Madrid','Paris','Budapest','Rome','Berlin', 'Moscow','Ljubljiana', 'Oslo','Beijing','Tokyo']

for count in range(10):
    print("{0:<14}{1:<14}".format(countries[count], capital[count]))
score = 0
import random
for count in range(5):
    country = random.randint(0,9)
    print("what is the capital of {0}: ".format(countries[country]))

    answer = input("")

    if answer == capital[country]:
        print("congratulations correct!")
        score = score + 1

    else:
        print(" wrong answer")
print (" your final score is {0} / 5".format (score))
