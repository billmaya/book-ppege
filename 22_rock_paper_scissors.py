# Exercise 22 - Rock Paper Scissors

def rpsWinner(player1, player2):
    winner = ''

    match player1:
        case 'rock':
            match player2:
                case 'rock':
                    winner = 'tie'
                case 'paper':
                    winner = 'player two'
                case 'scissors':
                    winner = 'player one'
        case 'paper':
            match player2:
                case 'rock':
                    winner = 'player one'
                case 'paper':
                    winner = 'tie'
                case 'scissors':
                    winner = 'player two'
        case 'scissors':
            match player2:
                case 'rock':
                    winner = 'player two'
                case 'paper':
                    winner = 'player one'
                case 'scissors':    
                    winner = 'tie'


    return winner



assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
