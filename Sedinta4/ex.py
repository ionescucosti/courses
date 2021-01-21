from random import randrange

board = [['1','2','3'],['4','5','6'],['7','8','9']]

def DisplayBoard(board):
    for i in board:
        print()
        for j in i:
            print(j,end='   ')
    print('\n\n\n')

def EnterMove(board):
    freepicks = MakeListOfFreeFields(board) # lista locuri libere
    squaremove=input('Alegeti casuta target: ')
    if squaremove not in freepicks:
        squaremove=input('Casuta gresita, introduceti din nou')
    if freepicks!=[]:
        for e in board:
            if squaremove in e:
                e[e.index(squaremove)]='0'
                break
    else:
        print('Game over!')

def MakeListOfFreeFields(board):
    free = []
    [free.append(j) for i in board for j in i]
    return free

def VictoryFor(board):
    if board[0]==['0','0','0'] or board[1] == ['0', '0', '0'] or board[2] == ['0', '0', '0'] or \
            board[0][0]+board[1][0]+board[2][0]=='000' or\
            board[0][1]+board[1][1]+board[2][1]=='000' or\
            board[0][3]+board[1][3]+board[2][3]=='000' or\
            board[0][0]+board[1][1]+ board[2][2]=='000' or\
            board[0][2]+board[1][1]+board[2][0]=='000':
        print('User won')
    elif board[0] == ['X', 'X', 'X'] or\
            board[1] == ['X', 'X', 'X'] or\
            board[2] == ['X', 'X', 'X'] or\
            board[0][0] + board[1][0] + board[2][0] == '000' or\
            board[0][1] + board[1][1] + board[2][1] == '000' or\
            board[0][3] + board[1][3] + board[2][3] == '000' or\
            board[0][0] + board[1][1] + board[2][2] == '000' or\
            board[0][2] + board[1][1] + board[2][0] == '000':
        print('Computer won')
    else:
        print('Game is not over.')

def DrawMove(board):
    freepicks = MakeListOfFreeFields(board)  # lista locuri libere
    pick = int(randrange(len(freepicks) - 1))  # alegere aleatoare index loc
    squaremove = freepicks[pick]  # locul ales

    if MakeListOfFreeFields(board)!=[]:
        for e in board:
            if squaremove in e:
                e[e.index(squaremove)] = 'X'
                break
    else:
        print('Game over!')

while True:

    if MakeListOfFreeFields(board)==[]:
        VictoryFor(board)
    else:
        if board[1][1] not in ['0', '1']: board[1][1] == 'X'
        DrawMove(board)
        print(DisplayBoard(board))
        EnterMove(board)