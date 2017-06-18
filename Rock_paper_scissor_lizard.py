# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if name=='rock' :
        return 0
    elif name=='Spock': 
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard': 
        return 3
    else: 
        return 4

def number_to_name(number):
    if number==0 :
        return 'rock'
    elif number==1: 
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3: 
        return 'lizard'
    else: 
        return 'scissors'



def rpsls(player_choice): 
    print ''
    
    print "you have chosen "+" " + player_choice
    
    
    x = name_to_number(player_choice)
 
   
    comp_number= random.randrange(0,4)
    comp_choice= number_to_name(comp_number)  

    print "computer has chosen " + comp_choice

    
    value=(comp_number-x)%5
    
    if value==0: 
        print "computer and player ties"
    elif value== 1 or value==2:
        print "computer wins"
    else:
        print "player wins"
    

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



