
#age = int (input('type your age: '))

#while age <= 10 :
    #print('\t' + str(age))
    #age+=1

#print('closed loop')

#now will we go to learn comand for

mtable = int (input('type your number for print multiplication them : '))

print('multiplication table of number :  ', mtable )

#comand for in python is : for( valor =0,valor < 10, valor++)
for value in range( 0, 11, 1):
    print(str(mtable) + ' x ' + str(value) + ' = ' + str((mtable *value)))
