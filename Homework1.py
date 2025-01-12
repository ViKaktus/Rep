
playfield = [
            ['',    '',    ''],
            ['',    '',    ''],
            ['',    '',    ''],
           ]
for row in playfield:
    print(row)

start = None
def start_function():
    global start
    start = input('Hey, lets play! Would you like to be x or 0? ')
    if start == 'X':
        print(f'ok, you chose X')
    elif start == '0':
        print(f'ok, you go with 0')
    else:
        print ('didnt get it, say again!')
        return start_function()
start_function()
def validate_input(func):
    def wrapper(*args, **kwargs):
        i, j = args
        while True:
            if 1 <= i <= 3 and 1 <= j <= 3:
                if playfield[i - 1][j - 1] == '':
                    return func(*args, **kwargs)
                else:
                    print("This field is taken, try another.")
                    i = int(input('Your turn! What row? '))
                    j = int(input('What column? '))
                    args = (i, j)
            else:
                print("Invalid input! Please enter row and column between 1 and 3.")
                i = int(input('Your turn! What row? '))
                j = int(input('What column? '))
                args = (i, j)
    return wrapper
@validate_input
def step(i, j):
    global start
    playfield[i-1][j-1] = start
    for row in playfield:
        print(row)
i = int(input('Your turn! What row? '))
j = int(input('What column? '))
step(i,j)
n = None
if start == 'X':
    n = '0'
else:
    n = 'X'
def empty_check(n):
    print('My turn')
    for outer_index, row in enumerate(playfield):
        for inner_index, element in enumerate(row):
            if element == '':
                playfield[outer_index][inner_index] = n
                for row in playfield:
                    print(row)
                return
    return None
empty_check(n)
i = int(input('Your turn! What row? '))
j = int(input('What column? '))
step(i,j)
empty_check(n)
def win_check(playfield):
    if any([playfield[0][0] == playfield[0][1] == playfield[0][2] !='',
            playfield[1][0] == playfield[1][1] == playfield[1][2] !='',
            playfield[2][0] == playfield[2][1] == playfield[2][2] !='',
            playfield[0][0] == playfield[1][0] == playfield [2][0] !='',
            playfield[0][1] == playfield[1][1] == playfield[2][1] !='',
            playfield[0][2] == playfield[1][2] == playfield[2][2] !='',
            playfield[0][0] == playfield[1][1] == playfield[2][2] !='',
            playfield[0][2] == playfield[1][1] == playfield[2][0] !=''
            ]):
        print("Game over! Last step was winning!")
        return True
    else:
        print("No winner yet.")
        return False
win_check(playfield)
while True:
    i = int(input('Your turn! What row? '))
    j = int(input('What column? '))
    step(i, j)
    if win_check(playfield):
        break
    else:
        empty_check(n)
        if win_check(playfield):
            break


























