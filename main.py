from fractions import Fraction
import random
import argparse
import sys


## INIT PARAMS
parser = argparse.ArgumentParser(description='claculates...')
parser.add_argument('--days_in_year', type=int,
                    help='An optional to insert amount of days in year, default value is 365')

parser.add_argument('--people', type=int,
                    help='Specified number of people in the room.', required=True)

parser.add_argument('--number_of_runs', type=int,
                    help='Specified number of runs.', required=True)

args = parser.parse_args()



days_in_year = 365 if args.days_in_year is None else args.days_in_year
if args.people is None:
    print("'--people' is a Required param")
    sys.exit()

people = args.people
number_of_runs = args.number_of_runs

counter = {'shared': 0, 'not_shared': 0}

# LOGIC

def generate_random_birthday():
    try:
        days = []
        for _ in range(people):
            day = random.randint(0, days_in_year)
            days.append(day)

        return days
    except Exception as e:
        print('Exception error from generate_random_birthday(), message: ' + str(e))
        return None


def culculate():
    for _ in range(number_of_runs):
        original_list = generate_random_birthday()
        disctinct_list = generate_random_birthday()
        if original_list is None or disctinct_list is None:
            print('This program is terminated.')
            return

        disctinct_list = set(disctinct_list)
        if(len(original_list) == len(disctinct_list)):
            counter['shared'] += 1
        else:
            counter['not_shared'] += 1



culculate()
if counter['shared'] == 0 or counter['not_shared'] == 0:
    print("counter dictionary paras is is equal to zero, something went wrong.")
    sys.exit()

p = counter['shared'] / (counter['shared'] + counter['not_shared'])
output_value = 1 - p
print("Given " + str(people) + " people, the chance of a shared birthday is " + str(output_value))



#print(decinal(365))