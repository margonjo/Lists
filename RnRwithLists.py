#Marc Gonzalez
#9/12/14
#list RnR 1.2

count = 0

studentA = input("please enter the name of the first student: ")
studentB = input("please enter the name of the second student: ")
studentC = input("please enter the name of the third student: ")
studentD = input("please enter the name of the fourth student: ")
studentE = input("please enter the name of the fifth student: ")
studentF = input("please enter the name of the sixth student: ")
studentG = input("please enter the name of the seventh student: ")
studentH = input("please enter the name of the eighth student: ")

names = [studentA,studentB,studentC,studentD,studentE,studentF,studentG,studentH]

for each in names:
    count = count +1
    print("{0}.{1}".format(count,each))


select = int(input(" please select a student to edit: "))

actual_select = select - 1


change = input("please enter their new name: ")

names.pop(actual_select)

names.insert(actual_select, change)

count = 0
for each in names:
    count = count +1
    print("{0}.{1}".format(count,each))
