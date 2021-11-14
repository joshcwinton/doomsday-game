import datetime
import random
import argparse

# REcord how many games have been played
# Start from beginning of current year
def getDayOfWeek(date):
    return date.strftime('%A')

# returns a random date
def randomDate():
    today = datetime.date.today()
    end_date = today.replace(month=12, day=31)
    start_date = today.replace(month=1, day=1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date
    
def main():
    parser = argparse.ArgumentParser(description='Guess the weekday for a random date')
    parser.add_argument('--max_guesses', default=3, dest='max_guesses', type=int)
    args = parser.parse_args()
    
    random_date = randomDate()
    weekday = getDayOfWeek(random_date)
    print(random_date)
    
    max_guesses = args.max_guesses
    guesses = 0
    
    while guesses < max_guesses:
        guess = input("make a guess: ")

        if(guess.lower() == weekday.lower()):
            print("Correct!")
            return
        else:
            print("Incorrect!")
        guesses += 1

    print("Game over!")

if __name__ == '__main__':
  main()
  
 
