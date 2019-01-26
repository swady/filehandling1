def crtfile():                                                  ##creating function crtfile()
    print('create function')                                    
    a=input('enter the name of the student ')                   ##taking input from user
    b=input('enter the class ')                                 
    c=input('enter the roll number ')                           
    f=open('g://filehandling//'+fl+'.txt','w')                  ##creating a file in g drive in the folder filehandling
    f.write('Name = '+a)                                        ##adding name of the student
    f.write('\nclass = '+b)                                     ##adding class of the student
    f.write('\nRoll num = '+c)                                  ##adding roll number of the student
    f.close()

    return(f)                                                   ##returning the function
def appnd():                                                    ##creating an the append function to append the next values
    print('appned function')            
    f=open('g://filehandling//'+fl+'.txt','a')                  ##open function for appending the values
    a1=input('enter the name of the student ')                  ##taking input from user
    b1=input('enter the class ')
    c1=input('enter the roll number ')
    f.write('\nName = '+a1)                                     ##adding valuses from the file
    f.write('\nClass = '+b1)
    f.write('\nRoll num = '+c1)
    f.close()
    return(f)                                                   ##retuen the values in the function
loop=0                                                          ##loop value
while(loop==0):                                                 ##loop for continous ittrations
    fl=input('enter the file name ')                            ##taking file name from user
    new=input('is it a new file? Y/N ')                         
    task=input('read or write in the file? R/W ')
    if(task=='W' or task=='w'):                                 ##check whether to write or not
        if(new=='y' or new=='Y'):                               ##check whether a new file or not
            crtfile()                                           ##if new then create a file
        elif(new=='n' or new=='N'):
            appnd()                                             ##when existing file append the values
        else:
            print('invalid input')                              ##for any other value
            continue
        d=1                                                     ##loop value
        while(d>0):                                             ##loop condition
            cont=input('do you want to add more? Y/N ')         ##input from user if it want to add more values
            if(cont=='Y' or cont=='y'):                         ##check condition is true
                appnd()                                         ##go to append function
            else:
                d=0                                             ## else get out of the loop
        read=input('do you want to read file? Y/N ')            ## ask if user wants to read the data in the file
        if(read=='Y' or read=='y'):                             ## check if the confition is true
            f=open('g://filehandling//'+fl+'.txt','r+')         ## read command
            for i in f:                                         ## for loop for all the values in the file
                print(i)
            f.close()
            break                                               ## get out of loop once the file is read
        elif(read=='n' or read=='N'):                           ##if the user is not willing to read
            newfile=input('do you want to creat a new file? Y/N ') ## ask if the user wants to create a new file
            if(newfile=='y' or newfile=='Y'):                   ## check if the condition is true
                continue                                        ## continue from the begining
            else:
                break                                           ## get out of the loop
        else:
            print('wrong command')                              ##if the user has input anything appart from the desired input
    elif(task=='R' or task=='r'):                               ##check if the user wants to read the file
        f=open('g://filehandling//'+fl+'.txt','r+')             ##open the file to read
        for i in f:                                             ##read the file from top to bottom using for loop
            print(i)
        f.close()
        ex=input('do you want to exit? Y/N ')                   ## ask if the user wants to exit or continue
        if(ex=='Y' or ex=='y'):                                 ## check if the condition is true or not
            break
        else:
            continue
    else:                                                       ## if the user has entered anything appart from the desired input
        print('invalid command')
        ex=input('do you want to exit? Y/N ')                   ## ask if the user wants to continue or exit
        if(ex=='Y' or ex=='y'):                                 ## check the input by the user
            break
        else:
            continue
