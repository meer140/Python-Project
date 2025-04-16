import random

list = ['r','s','p']
dic = {'r' : "⚫", 's' : "✂️", 'p' : "📄"}

def get_userchoice():
    while True:
        user_choice =  input("Choose one rock, paper or scissors(r/p/s): ").lower()
        if user_choice in list:
            return user_choice
        else:
            print("Invalid Input")
        
def result(user_choice, comp_choice): 
     if ((user_choice == 'r' and  comp_choice == 'scissors') or
            (user_choice == 'p' and comp_choice == 'rock') or
            (user_choice == 's' and comp_choice == 'paper')) :
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
        comp_choice = random.choice(list)
        print("Computer choose ",dic[comp_choice])
       
        result(user_choice, comp_choice)  
        
        cont = input("Do you want to continue or Quit(q): ").lower()
        if(cont=='q'):
            break
    

if __name__ == "__main__":
    main()                               
        