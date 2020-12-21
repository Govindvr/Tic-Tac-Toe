value = ['G'for i in range(9)]


def instructions():
    print("\n\nChoose a cell numbered from 1 to 9 as below and play")
    print("\n\n\t\t\t1 | 2  | 3  ")
    print("\t\t\t----------")
    print("\t\t\t4 | 5  | 6  ")
    print("\t\t\t----------")
    print("\t\t\t7 | 8  | 9  ")
    print("\n-------------------------------------------------------")

def input_values(mark,pos):
    positon =  pos -1
    value[positon] = mark


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
        print("\t\t\t----------")
    print("\n-------------------------------------------------------")
    
