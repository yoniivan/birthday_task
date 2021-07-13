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

parser.add_argument('--digits_after_dot', type=int,
                    help='Specified number of digits after dot.')

args = parser.parse_args()

days_in_year = 365 if args.days_in_year is None else args.days_in_year
people = args.people
number_of_runs = args.number_of_runs
digit_after_dot = 10 if args.digits_after_dot is None else args.digits_after_dot

if digit_after_dot > 10 or digit_after_dot < 1:
    print("'--digits_after_dot' can't be larger than 10 or smaller than 1.")

if days_in_year < 100 or days_in_year > 1000:
    print("'--days_in_year' can't be less than 100 or larger than 1,000.")
    sys.exit()

if people < 2 or people > 1000:
    print("'--people' can't be less than 2 or larger than 1,000.")
    sys.exit()

if number_of_runs < 2 or number_of_runs > 10000:
    print("'--number_of_runs' can't be less than 2 or larger than 10,000.")
    sys.exit()

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
    try:
        for _ in range(number_of_runs):
            original_list = generate_random_birthday()
            disctinct_list = generate_random_birthday()
            if original_list is None or disctinct_list is None:
                print('This program is terminated.')
                return

            disctinct_list = set(disctinct_list)
            if (len(original_list) == len(disctinct_list)):
                counter['shared'] += 1
            else:
                counter['not_shared'] += 1
    except Exception as e:
        print('Exception error from culculate(), message: ' + str(e))
        sys.exit()



culculate()
if counter['shared'] == 0 and counter['not_shared'] == 0:
    print("counter dictionary paras is is equal to zero, something went wrong.")
    sys.exit()

if counter['shared'] == 0 or counter['not_shared'] == 0:
    print("Given " + str(people) + " people, the chance of a shared birthday is almost zero")
    sys.exit()

p = counter['shared'] / (counter['shared'] + counter['not_shared'])
output_value = round(1 - p, digit_after_dot)
print("Given " + str(people) + " people, the chance of a shared birthday is " + str(output_value))
