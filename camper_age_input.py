"""
Program: camper_age_input.py
Author: Sherri Maya
Last date modified: 06/21/2020



The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp
and convert the age in months to years via a function call then print the result.
"""

def convert_to_months(age_in_years):
    try:
        age_in_months = int(age_in_years) * 12
        print ('Camper is',age_in_months,'months old.')
    except ValueError:
        print(age_in_years, 'is not a valid age.  Try again!')

    return age_in_months

if __name__ == '__main__':
    age_in_years = input('What is the campers age?')
    age_in_years = (age_in_years)
    convert_to_months(age_in_years)

