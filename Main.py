


"""
$CITY_NAME is a $COMMUNITY_SIZE with a large focus on its $SPERM(5).
This $COMMUNITY_SIZE(3) is governed by $POLITICAL(5) where it's main export is $ECONOMIC(8).
$MILITARY(4) oversees all conflict in $CITY_NAME.
The locals of $CITY_NAME spend their free time at one of its many $SOCIAL(5).
Those who live here often find themselves $RELIGION(4), but are tolerant of others beliefs.

The families that have been here for generations tend to have one or more of the following racial features:
RACIAL_FEATURE(5x)

Anyone who has spent a decent amount of time here, likely has developed one or more of the following skills:
PROFICIENCIES(5x)

Adventurers who have found their start in $CITY_NAME tend to become 5E_CLASS(116) or 5E_CLASS(116)
"""
##Import Modules
import random, os

##Global References
#Lists
COMMUNITY_SIZE_LIST = [
	'Village',
	'Town',
	'City'
]
SPERM_LIST = [
	'Social Activities',
	'Politics',
	'Economy',
	'Religion',
	'Military'
]
SOCIAL_LIST = [
	'Taverns',
	'Theater',
	'Museum',
	'Library',
	'Restaurants'
]
POLITICAL_LIST = [
	'A Democratically Elected Leader',
	'The Monarchy',
	'A Military Government',
	'Anarchy',
	'An Oligarchy'
]
ECONOMIC_LIST = [
	'Agriculture',
	'Farming',
	'Fishing',
	'Fashion',
	'Technology',
	'Travel',
	'Mining',
	'Lumber'
]
RELIGION_LIST = [
	'Monotheistic',
	'Polytheistic',
	'Atheistic',
	'Agnostic'
]
MILITARY_LIST = [
	'A Local Militia',
	'A Royal Guard Post',
	'A Hunting Party',
	'A Formal Town Guard'
]

#Variables
path = os.getcwd()

##Functions
#Get a random line from an external file
def GET_EXTERNAL_RANDOM(rsv):
    file_h = open(f"{path}\{rsv}.txt")
    limit = file_h.readline()
    limit = limit.replace('\n', '' )
    limit = int(limit)
    line = random.randint(0, limit - 1)

    for x in range(line):
        file_h.readline()
    phrase = file_h.readline()
    phrase = phrase.replace('\n', '')

    return(phrase)

#Main function
def main():
	#Get user input and set seed
	CITY_NAME = input("Enter Town Name: ")
	print()
	random.seed(CITY_NAME)

	#Let's get them deets
	COMMUNITY_SIZE = COMMUNITY_SIZE_LIST[random.randint(0,len(COMMUNITY_SIZE_LIST)-1)]
	SPERM = SPERM_LIST[random.randint(0,len(SPERM_LIST)-1)]
	POLITICAL = POLITICAL_LIST[random.randint(0,len(POLITICAL_LIST)-1)]
	ECONOMIC = ECONOMIC_LIST[random.randint(0,len(ECONOMIC_LIST)-1)]
	MILITARY = MILITARY_LIST[random.randint(0,len(MILITARY_LIST)-1)]
	SOCIAL = SOCIAL_LIST[random.randint(0,len(SOCIAL_LIST)-1)]
	RELIGION = RELIGION_LIST[random.randint(0,len(RELIGION_LIST)-1)]

	#More files, more deets
	#Generational Features
	RACIAL_FEATURE_LIST = []
	for i in range(5):
		RACIAL_FEATURE = GET_EXTERNAL_RANDOM('RACIAL_FEATURE')
		while (RACIAL_FEATURE in RACIAL_FEATURE_LIST):
			RACIAL_FEATURE = GET_EXTERNAL_RANDOM('RACIAL_FEATURE')
		RACIAL_FEATURE_LIST.append(RACIAL_FEATURE)

	#Background Proficiencies
	PROFICIENCIES_LIST = []
	for i in range(5):
		PROFICIENCIES = GET_EXTERNAL_RANDOM('PROFICIENCIES')
		while (PROFICIENCIES in PROFICIENCIES_LIST):
			PROFICIENCIES = GET_EXTERNAL_RANDOM('PROFICIENCIES')
		PROFICIENCIES_LIST.append(PROFICIENCIES)

	#Classes
	CLASS_0 = GET_EXTERNAL_RANDOM('CLASS_LIST')
	CLASS_1 = GET_EXTERNAL_RANDOM('CLASS_LIST')
	while (CLASS_1 == CLASS_0):
		CLASS_1 = GET_EXTERNAL_RANDOM('CLASS_LIST')



	#Print
	print(f'{CITY_NAME} is a {COMMUNITY_SIZE} with a large focus on {SPERM}.')
	print(f'This {COMMUNITY_SIZE} is governed by {POLITICAL} where it\'s main economic exploit is {ECONOMIC}.')
	print(f'{MILITARY} oversees all conflict in {CITY_NAME}.')
	print(f'The locals of {CITY_NAME} spend their free time at its {SOCIAL}.')
	print(f'Those who live here often find themselves {RELIGION}, but are tolerant of others beliefs.')
	print('')
	print('The families that have been here for generations tend to have one or more of the following racial features:')
	for i in RACIAL_FEATURE_LIST:
		print(f'\t* {i}')
	print('')
	print('Anyone who has spent a decent amount of time here, likely has developed one or more of the following Skill Proficiencies:')
	for i in PROFICIENCIES_LIST:
		print(f'\t* {i}')
	print('')
	print(f'Adventurers who have found their start in {CITY_NAME} tend to become a {CLASS_0} or a {CLASS_1}')


##Execute
main()
