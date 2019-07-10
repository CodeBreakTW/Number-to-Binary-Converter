'''
Created on Feb 21, 2019

@author: tyler
'''


cont = True
while cont == True:
    number = int(input("Please input a number to convert to binary "))
    savenumber = number
    continput = ""
    binary = []
    for x in range(8):
        binary.append(int(number%2))
        if binary[x] == 1:
            number = int((number-1) / 2)
        else:
            number = int(number/2)
    for y in range(len(binary)):
        if binary[len(binary) - 1] == 0:
            binary.pop(len(binary)-1)
    
    binary = reversed(binary)
    
    
    
    print(*binary, sep=" " , end= " is " + str(savenumber) + " in binary")
    print()
    continput= input("To convert another number, please type y ")
    if continput is "y":
        cont = True
    else:
        cont = False
end = input("Press any key to exit")
        
    
