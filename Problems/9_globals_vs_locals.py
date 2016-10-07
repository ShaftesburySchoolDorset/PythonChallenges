# Fix the following code for this score counting app

score = 0
diff = 1

def win():
    # todo

def lose():
    score -= diff
    output_score()

def output_score():
    print("The score is currently: x", )

while 1:
    result = input('win (w) or lose (l)?')
    if result.lower() == 'w':
        win()
    elseif result.lower() == 'l':
        #todo
    else
        print('?') #todo
