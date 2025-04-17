import random

Rock = 'r'
Scissors = 's'
Paper = 'p'

dic = {'r' : "⚫", 's' : "✂️", 'p' : "📄"}
choices = tuple(dic.keys())

def get_userchoice():
    while True:
        user_choice =  input("Choose one rock, paper or scissors(r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Input")
        
def result(user_choice, comp_choice): 
     if ((user_choice == Rock and  comp_choice == Scissors) or
            (user_choice == Paper and comp_choice == Rock) or
            (user_choice == Scissors and comp_choice == Paper)) :
            print("You win the game!")
     elif user_choice == comp_choice:
            print("Tie")    
     else:
            print("You lose the game.")       


def main():
    
    print("------ROCK SCISSORS PAPER GAME------")
    while(True):
        
        user_choice = get_userchoice()
        
        print("You choose ",dic[user_choice])
        comp_choice = random.choice(choices)
        print("Computer choose ",dic[comp_choice])
       
        result(user_choice, comp_choice)  
        
        cont = input("Do you want to continue or Quit(q): ").lower()
        if(cont=='q'):
            break
    

if __name__ == "__main__":
    main()                               
        