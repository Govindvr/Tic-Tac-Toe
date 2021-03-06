value = [' 'for i in range(9)]            #List in which the input from both human and computer is stored
markp = ""                                #Stores the mark of the player
markc = ""                                #Stores the mark of the computer
def instructions():                       #To display intruction and board layout at the begining
    print("\n\nChoose a cell numbered from 1 to 9 as below and play")
    print("\n\n\t\t\t1 | 2  | 3  ")
    print("\t\t\t----------")
    print("\t\t\t4 | 5  | 6  ")
    print("\t\t\t----------")
    print("\t\t\t7 | 8  | 9  ")
    print("\n-------------------------------------------------------")

def input_values(markp,markc,pos):         #Function to accept input from the player
    positon =  pos -1
    if value[positon]==markc:
        print("\t\t\tDON'T EVEN TRY, STUPID CHEATER!!!")
        exit(0)
    value[positon] = markp

def computer(markp,markc):                #Function which plays the game as computer
    row1 = value[0:3]
    row2 = value[3:6]
    row3 = value[6:9]
    col1 = value[0:7:3]
    col2 = value[1:8:3]
    col3 = value[2:9:3]
    dia1 = [value[0],value[4],value[8]]
    dia2 = [value[2],value[4],value[6]]
    corner = [0,2,6,8]

    def attack_corner():
        for i in corner:
            if value[i]==" ":
                value[i] = markc
                break

    def scan(first,last,skip):
        for i in range(first,last,skip):
            if value[i] == " ":
                value[i] = markc
            else:
                continue

    def comp_logic(mark,id = 2):          #Function which analyse all possible winning moves and play accordingly
            if row1.count(mark)==2 and row1.count(" ") != 0:
                scan(0,3,1)
            elif row2.count(mark)==2 and row2.count(" ") != 0:
                scan(3,6,1)
            elif row3.count(mark)==2 and row3.count(" ") != 0:
                scan(6,9,1)
            elif col1.count(mark)==2 and col1.count(" ") != 0:
                scan(0,7,3)
            elif col2.count(mark)==2 and col2.count(" ") != 0:
                scan(1,8,3)
            elif col3.count(mark)==2 and col3.count(" ") != 0:
                scan(2,9,3)
            elif dia1.count(mark)==2 and dia1.count(" ") != 0:
                scan(0,9,4)
            elif dia2.count(mark)==2 and dia2.count(" ") != 0:
                scan(2,7,2)
            else:
                if id == 1:
                    return True
                elif markc == "X":
                    attack_corner()
                elif value[4] == " ":
                    value[4]=markc
                elif value.count(" ")==1:
                    value[value.index(" ")] = markc
                else:
                    attack_corner()                   
                return False

    if comp_logic(markc,1):
        comp_logic(markp)
       
def check_result(markp,markc):             #To check if any player won and to display winning message
    def who(w):
        if value[w] == markp:
                print("\t\t\tSomthing went wrong, you won!")
        else:
            print("\t\t\tHAHA NOOB!!!, COMPUTER WON ")
            exit(0)

    for i in range(0,7,3):
        if (value[i]==value[i+1]== value[i+2]) and value[i] != " ":                  
            who(i)
            return False 
    for i in range(3):
        if (value[i]==value[i+3]==value[i+6]) and value[i] !=" ":
            who(i)
            return False 
    if (value[0]==value[4]==value[8]) and value[0] != " ": 
        who(0)
        return False 
    if (value[2]==value[4]==value[6]) and value[2] != " ": 
        who(2)
        return False 
    if value.count(" ") == 0:
        print("\t\t\tFINALLY!!, A WORTHY OPPONENT, Its a Draw!!!")
        return False
    return True
        
def display():                          #To display the board with player moves
    print("\n")
    print("\t\t\t-------------")
    for i in range(0,7,3):
        print("\t\t\t|",value[i],"|",value[i+1],"|",value[i+2],"|")
        print("\t\t\t-------------")
    print("\n-------------------------------------------------------")

#Main body of the program 

user=input("\n\t\tchoose your letter (X or O)")    #player choosing his character
user = user.upper()
if user == "X":
    AI = "O"
else:
    AI = "X"
instructions()

loop = True
while(loop):                                      
    if user == "X":
        choice = int(input("\nEnter your choice: "))
        input_values(user,AI,choice)
        computer(user, AI)
        display()
        loop = check_result(user,AI)
    else:
        computer(user, AI)
        display()
        loop = check_result(user,AI)
        choice = int(input("\nEnter your choice: "))
        input_values(user,AI,choice)        
        loop = check_result(user,AI)