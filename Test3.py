def main():
    print('==================================Fitness Center==================================')
    print('Membership: $30.00 \nPersonal Training Sessions: $65.00')
    print('==================================================================================')
    senior = input('Welcome to the fitness center! Are you a senior citizen? (Y/N): ')
    months = 0 #initalize months
    if senior == 'Y' or senior == 'y': #30% discount
        months = int(input('Hello senior citizen you have earned a 30 percent discount! If you also plan to pay 12+ months in advance, you get another 15 percent discount! Please enter the amount of months you plan to pay.'))
    else:
         sessions = int(input('OK, got it. You can recieve a discount of 20 percent EACH session if you plan to pay more than 5 training sessions! How many training sessions would you like? '))
    if months >= 12: #15% discount
         sessions = int(input('You can recieve another discount for 20 percent EACH session if you plan to pay more than 5 training sessions! How many training sessions would you like? '))
    else:
        sessions = int(input('OK, got it. How many training sessions would you like? You can get a 20 percent discount for EACH session if you plan to pay more than 5 training sessions.'))
    if sessions > 5: #20% discount each
            print('Congratulations! You have earned the training sessions discount!')
    else:
        print('You did not get the discount for', sessions , 'sessions')
    membership_calculations()
    training_calculations()
    total_calculations()


def membership_calculations(senior, months):
    if senior == 'Y' or senior == 'y' and months >= 12:
     total_membership = (30*months)*(.55)
     print('Your total membership cost is:', total_membership)
    if senior == 'N' or  senior == 'n' and months >= 12:
     total_membership = (30*months)*(.85)
     print('Your total membership costs is:', total_membership)
    if senior == 'Y' or senior == 'y' and months < 12:
     total_membership = (30*months)*(.70)
     print('Your total membership cost is:', total_membership)
    if senior == 'N' or senior == 'n' and months < 12:
     total_membership = (30*months)
     


def training_calculations(sessions):
    if sessions > 5:
     total_sessions = (sessions*65)(.80)
     print('Your total amount for the sessions is: ', total_sessions)
    else:
     total_sessions = (sessions*65)
     print('Your total sessions are:', total_sessions)


def total_calculations(total_membership, total_sessions):
    total = total_membership + total_sessions
    print('Your entire total is: ', total)


main() #calls the function