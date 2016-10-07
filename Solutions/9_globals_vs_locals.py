# Fix the following code for this score counting app

score = 0
diff = 1

def win():
    global score, diff
    score += diff
    output_score()

def lose():
    global score, diff
    score -= diff
    output_score()

def output_score():
    global score
    print("The score is currently: ", score)

while 1:
    result = input('win (w) or lose (l)?')
    if result.lower() == 'w':
        win()
    elif result.lower() == 'l':
        lose()
    else:
        print('Invalid letter')
