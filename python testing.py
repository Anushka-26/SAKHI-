import random 

def play():
    user = input("whats your choice ? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if win(user, computer):
        return 'You won!'
    return 'you lost!'
    
    #r > s, s > p, p > r
    def win(player,opponent):
        
        if(player=='r' and opponent =='s') or (player=='s' and opponent =='p') or (player=='p' and opponent =='r'):
            return 'you won!'
    
    print(play())