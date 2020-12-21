value = [' 'for i in range(9)]
markp = ""
markc = ""
def instructions():
    print("\n\nChoose a cell numbered from 1 to 9 as below and play")
    print("\n\n\t\t\t1 | 2  | 3  ")
    print("\t\t\t----------")
    print("\t\t\t4 | 5  | 6  ")
    print("\t\t\t----------")
    print("\t\t\t7 | 8  | 9  ")
    print("\n-------------------------------------------------------")

def input_values(markp,pos):
    positon =  pos -1
    value[positon] = markp

def computer(markp,markc):
    row1 = value[0:3]
    row2 = value[3:6]
    row3 = value[6:9]
    col1 = value[0:7:3]
    col2 = value[1:8:3]
    col3 = value[2:9:3]
    dia1 = [value[0],value[4],value[8]]
    dia2 = [value[2],value[4],value[6]]
    x=[]
    def scan(x):
        for i in range(3):
            if x[i]==markp:
                continue
            else:
                x[i]=markc

    if row1.count(markp)==2:
        scan(row1)
    elif row2.count(markp)==2:
        scan(row2)
    elif row3.count(markp)==2:
        scan(row3)
    elif col1.count(markp)==2:
        scan(col1)
    elif col2.count(markp)==2:
        scan(col2)
    elif col3.count(markp)==2:
        scan(col3)
    elif dia1.count(markp)==2:
        scan(dia1)
    elif dia2.count(markp)==2:
        scan(dia2)
    else:
        value[5]=2 #dummy        
    print(x) #dummy

        
def check_result():

    for i in range(0,7,3):
        if value[i]==value[i+1]==value[i+2]:
            print("you won")
            return

    for i in range(3):
        if value[i]==value[i+3]==value[i+6]:
            print("you won")
            return 

    if value[0]==value[4]==value[8]: 
        print("you won")
        return 

    if value[2]==value[4]==value[6]: 
        print("you won")
        return 

    print("you lost")
        
def display():
    print("\n")
    for i in range(0,7,3):
        print("\t\t\t",value[i],"|",value[i+1],"|",value[1+2])
        print("\t\t\t-----------")
    print("\n-------------------------------------------------------")

input_values("x",1)
input_values("x",7)
computer("x","y")
display()