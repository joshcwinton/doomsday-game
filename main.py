import datetime
import random
import argparse
import os.path
import json

# Record how many games have been played
def getDayOfWeek(date):
    return date.strftime('%A')

# Returns a random date
def randomDate():
    today = datetime.date.today()
    end_date = today.replace(month=12, day=31)
    start_date = today.replace(month=1, day=1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def readResultsFile():
    today = datetime.date.today()
    filename = today.strftime('%Y%m')
    if(os.path.isfile(os.path.expanduser('~/.doomsday-scores/{0}'.format(filename))) != True):
       createResultsFile()

def updateResultsFile(win):
    if not os.path.exists('results.json'):
        createResultsFile()

    with open('results.json', 'r') as f:
        results = json.load(f)

    with open('results.json', 'w') as f: 
        results['games'] += 1
        if win:
            results['wins'] += 1
        f.write(json.dumps(results))
    win_rate = results['wins']/results['games']
    print("Your win rate is {:2.0%}".format(win_rate))

def createResultsFile():
    results = {'games': 0, 'wins': 0}
    with open('results.json', 'w') as f:
        f.write(json.dumps(results))

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
            updateResultsFile(True)
            return
        else:
            print("Incorrect!")
        guesses += 1

    print("Game over!")
    updateResultsFile(False)
    
if __name__ == '__main__':
  main()
  
 
