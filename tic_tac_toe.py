#project 1 - tic tac to

def board(x):
    print(x[7] + "|" + x[8] + "|" + x[9])
    print("-|-|-")
    print(x[4] + "|" + x[5] + "|" + x[6])
    print("-|-|-")
    print(x[1] + "|" + x[2] + "|" + x[3])

def choose():
    player1_m = input().upper()
    if player1_m in ["O"]:
        player2_m = 'X'
    else:
        player2_m = 'O'
    return (player1_m, player2_m)

def input_user():
    c=int(input('enter position '))
    return c

def check(z,mark):
    b=((z[2]==z[5]==z[6]==mark)or(z[1]==z[4]==z[7]==mark)or(z[3]==z[6]==z[9]==mark)or(z[1]==z[2]==z[3]==mark)or(z[4]==z[5]==z[6]==mark)or(z[7]==z[8]==z[9]==mark)or(z[7]==z[5]==z[3]==mark)or(z[1]==z[5]==z[9]==mark))
    return b
import random
def choose_first():
    flip=random.randint(0,1)
    if flip == 0:
        return "player1"
    else:
        return "player2"

def set(m,mar):
    u=True
    while u:
        h = input_user()
        if space_check(m, h) == True:
            m[h] = mar
            board(m)
            u = False
        else:
            print("sorry position already taken ")


def space_check(n,k):
    return n[k]==" "

def full(y):
    for i in range(1,10):
        if space_check(y,i)==True:
            return False

    return True


print("welcome to tic tac toe game")
y=[""," "," "," "," "," "," "," "," "," "]
q=['#','1','2','3','4','5','6','7','8','9']
print("player 1 enter X or O ")
mark1, mark2 = choose()
board(q)
jimo = True
turn = choose_first()
print(turn + " goes first")
while jimo:
    if turn in "player1":
        print("player 1 chance")
        set(y, mark1)
        win = check(y, mark1)
        if win:
            print('CONGRATULATION player 1 won   !!!!')
            jimo = False

        else:
            if full(y) :
                print('the match is draw')
                jimo = False
            else:
                turn = "player2"
    elif turn in "player2":
        print("player 2 chance")
        set(y, mark2)
        win = check(y, mark2)
        if win:
            print('CONGRATULATION player 2 won  !!!!')
            jimo = False

        else:
            if full(y) :
                print('the match is draw')
                jimo = False
            else:
                turn = "player1"

