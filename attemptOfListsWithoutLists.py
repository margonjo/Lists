#Marc Gonzalez
#9/12/14
#list RnR 1.1

studentA = input("please enter the name of the first student: ")
studentB = input("please enter the name of the second student: ")
studentC = input("please enter the name of the third student: ")
studentD = input("please enter the name of the fourth student: ")
studentE = input("please enter the name of the fifth student: ")
studentF = input("please enter the name of the sixth student: ")
studentG = input("please enter the name of the seventh student: ")
studentH = input("please enter the name of the eighth student: ")

for count in range(1,9):
    if count == 1:
        student = studentA
    elif count == 2:
        student = studentB
    elif count == 3:
        student = studentC
    elif count == 4:
        student = studentD
    elif count == 5:
        student = studentE
    elif count == 6:
        student = studentF
    elif count == 7:
        student = studentG
    else:
        student = studentH

    
        
        
        
    print("{0}. {1}".format(count, student))

select = int(input(" please select a student to edit: "))




change = input("please enter their new name: ")


if select ==1:
    for count in range(1,9):
        if count == 1:
            student = change
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))

elif select == 2:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = change
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))
elif select ==3:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = change
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))
elif select ==4:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = change
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))

elif select ==5:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = change
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))
elif select ==6:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = change
        elif count == 7:
            student = studentG
        else:
            student = studentH
        print("{0}. {1}".format(count, student))

elif select ==7:
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = change
        else:
            student = studentH
        print("{0}. {1}".format(count, student))

elif select ==8 :
    for count in range(1,9):
        if count == 1:
            student = studentA
        elif count == 2:
            student = studentB
        elif count == 3:
            student = studentC
        elif count == 4:
            student = studentD
        elif count == 5:
            student = studentE
        elif count == 6:
            student = studentF
        elif count == 7:
            student = studentG
        else:
            student = change
        print("{0}. {1}".format(count, student))
else:
    print("Exit program")



            
