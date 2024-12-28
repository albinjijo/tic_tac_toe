def print_board(x,y):
    zero="X" if x[0]==1 else ("Y" if y[0] else "0")
    one="X" if x[1]==1 else ("Y" if y[1] else "1")
    two="X" if x[2]==1 else ("Y" if y[2] else "2")
    three="X" if x[3]==1 else ("Y" if y[3] else "3")
    four="X" if x[4]==1 else ("Y" if y[4] else "4")
    five="X" if x[5]==1 else ("Y" if y[5] else "5")
    six="X" if x[6]==1 else ("Y" if y[6] else "6")
    seven="X" if x[7]==1 else ("Y" if y[7] else "7")
    eight="X" if x[8]==1 else ("Y" if y[8] else "8")
    print(f"{zero} | {one} | {two}")
    print(f"{three} | {four} | {five}")
    print(f"{six} | {seven} | {eight}")
    
def sum(a,b,c):
    return a+b+c
    
def check(x,y):
    wins=[[0,1,2],[3,4,5],[6,7,8,],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(x[win[0]],x[win[1]],x[win[2]])==3:
            print('X wins')
            return 1
        if sum(y[win[0]],y[win[1]],y[win[2]])==3:
            print('O wins')
            return 1
    return 0
            
    

x_state = [0,0,0,0,0,0,0,0,0]
o_state = [0,0,0,0,0,0,0,0,0]
turn=True
while True:
    print_board(x_state,o_state)
    if turn:
        print("X turn")
        val=int(input("Enter no: "))
        x_state[val]=1
    else:
        print("O turn")
        val=int(input("Enter no: "))
        o_state[val]=1
    z=check(x_state,o_state)
    if z:
        break
        
    turn=not turn
