import random
 
emojis = {
    'r' : '🪨',
    'p' : '🧻',
    's' : '✂️',
}

value = ['r','p','s']
computer = random.choice(value)
user = input("Enter Rock, Papper, Scissor as (r/p/s) : ").lower()

def game():
    while True:
       if 'r' in user or 'p' in user or 's' in user:
            if(user == 'r'):
                Rock()
                break
            elif(user == 'p'):
                Paper()
                break
            elif(user == 's'):
                Scissor()
                break

       else:
           print("Enter a Valid input")
           pass 
def Rock():
    if(computer == 'r'):
        print(emojis[user]," vs",emojis[computer])
        print("IT's a DRAW !! ")
    elif(computer == 'p'):
        print(emojis[user]," vs",emojis[computer])
        print("You LOSE !! ")
    elif(computer == 's'):
        print(emojis[user]," vs",emojis[computer])
        print("YOoo.. YOU WON !! ")

def Paper():
    if(computer == 'r'):
        print(emojis[user]," vs",emojis[computer])
        print("YOoo.. YOU WON !! ")
    elif(computer == 'p'):
        print(emojis[user]," vs",emojis[computer])
        print("IT's a DRAW !! ")
    elif(computer == 's'):
        print(emojis[user]," vs",emojis[computer])
        print("You LOSE !! ")

def Scissor():
    if(computer == 'r'):
        print(emojis[user]," vs",emojis[computer])
        print("You LOSE !! ")
    elif(computer == 'p'):
        print(emojis[user]," vs",emojis[computer])
        print("YOoo.. YOU WON !! ")
    elif(computer == 's'):
        print(emojis[user]," vs",emojis[computer])
        print("IT's a DRAW !! ")

while True:
  game()