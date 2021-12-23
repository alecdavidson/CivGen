


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
import argparse, os, random, sys

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

class Civilization():

	def __init__(self, CITY_NAME="", COMMUNITY_SIZE="", SPERM="", POLITICAL="", ECONOMIC="", MILITARY="", SOCIAL="", RELIGION="", RACIAL_FEATURE_LIST = [], PROFICIENCIES_LIST = []):
		self.CITY_NAME = CITY_NAME
		self.COMMUNITY_SIZE = COMMUNITY_SIZE
		self.SPERM = SPERM
		self.POLITICAL = POLITICAL
		self.ECONOMIC = ECONOMIC
		self.MILITARY = MILITARY
		self.SOCIAL = SOCIAL
		self.RELIGION = RELIGION
		self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST
		self.PROFICIENCIES_LIST =  PROFICIENCIES_LIST

	##Functions
	#Get a random line from an external file
	def GET_EXTERNAL_RANDOM(self, rsv):
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
	def main(self):
		#Get user input and set seed
		random.seed(self.CITY_NAME)

		#Let's get them deets
		self.COMMUNITY_SIZE = COMMUNITY_SIZE_LIST[random.randint(0,len(COMMUNITY_SIZE_LIST)-1)]
		self.SPERM = SPERM_LIST[random.randint(0,len(SPERM_LIST)-1)]
		self.POLITICAL = POLITICAL_LIST[random.randint(0,len(POLITICAL_LIST)-1)]
		self.ECONOMIC = ECONOMIC_LIST[random.randint(0,len(ECONOMIC_LIST)-1)]
		self.MILITARY = MILITARY_LIST[random.randint(0,len(MILITARY_LIST)-1)]
		self.SOCIAL = SOCIAL_LIST[random.randint(0,len(SOCIAL_LIST)-1)]
		self.RELIGION = RELIGION_LIST[random.randint(0,len(RELIGION_LIST)-1)]

		#More files, more deets
		#Generational Features
		for i in range(5):
			RACIAL_FEATURE = self.GET_EXTERNAL_RANDOM(rsv='RACIAL_FEATURE')
			while (RACIAL_FEATURE in self.RACIAL_FEATURE_LIST):
				RACIAL_FEATURE = self.GET_EXTERNAL_RANDOM(rsv='RACIAL_FEATURE')
			self.RACIAL_FEATURE_LIST.append(RACIAL_FEATURE)
		self.RACIAL_FEATURE_LIST.sort()

		#Background Proficiencies
		for i in range(5):
			PROFICIENCIES = self.GET_EXTERNAL_RANDOM(rsv='PROFICIENCIES')
			while (PROFICIENCIES in self.PROFICIENCIES_LIST):
				PROFICIENCIES = self.GET_EXTERNAL_RANDOM(rsv='PROFICIENCIES')
			self.PROFICIENCIES_LIST.append(PROFICIENCIES)
		self.PROFICIENCIES_LIST.sort()

		#Classes
		CLASS_0 = self.GET_EXTERNAL_RANDOM(rsv='CLASS_LIST')
		CLASS_1 = self.GET_EXTERNAL_RANDOM(rsv='CLASS_LIST')
		while (CLASS_1 == CLASS_0):
			CLASS_1 = self.GET_EXTERNAL_RANDOM(rsv='CLASS_LIST')



		#Print
		print(f'{self.CITY_NAME} is a {self.COMMUNITY_SIZE} with a large focus on {self.SPERM}.')
		print(f'This {self.COMMUNITY_SIZE} is governed by {self.POLITICAL} where it\'s main economic exploit is {self.ECONOMIC}.')
		print(f'{self.MILITARY} oversees all conflict in {self.CITY_NAME}.')
		print(f'The locals of {self.CITY_NAME} spend their free time at its {self.SOCIAL}.')
		print(f'Those who live here often find themselves {self.RELIGION}, but are tolerant of others beliefs.')
		print('')
		print('The families that have been here for generations tend to have one or more of the following racial features:')
		for i in self.RACIAL_FEATURE_LIST:
			print(f'\t* {i}')
		print('')
		print('Anyone who has spent a decent amount of time here, likely has developed one or more of the following Skill Proficiencies:')
		for i in self.PROFICIENCIES_LIST:
			print(f'\t* {i}')
		print('')
		print(f'Adventurers who have found their start in {self.CITY_NAME} tend to become a {CLASS_0} or a {CLASS_1}')


##Execute
if __name__=="__main__":
	parser = argparse.ArgumentParser()#formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-c', '--city_name', help='Set City Name. *REQUIRED*')
	parser.add_argument('--community_size', help='Set Community Size', default='')
	parser.add_argument('--sperm', help='Set Focus', default='')
	parser.add_argument('--social', help='Set Social', default='')
	parser.add_argument('--political', help='Set Political', default='')
	parser.add_argument('--economic', help='Set Economy', default='')
	parser.add_argument('--religion', help='Set Religion', default='')
	parser.add_argument('--military', help='Set Military', default='')
	parser.add_argument('--racial_feature_list', action='append', help='Add Racial Feature', default='')
	parser.add_argument('--proficiencies_list', action='append', help='Add Proficiency', default='')
	args = parser.parse_args()

	print(f'city_name: {args.city_name}')
	print(f'community_size: {args.community_size}')
	print(f'focus: {args.sperm}')
	print(f'social: {args.social}')
	print(f'political: {args.political}')
	print(f'economic: {args.economic}')
	print(f'religion: {args.religion}')
	print(f'military: {args.military}')
	print(f'racial_feature_list: {args.racial_feature_list}')
	print(f'proficiencies_list: {args.proficiencies_list}')
	print()

	civ = Civilization(CITY_NAME=args.city_name, COMMUNITY_SIZE=args.community_size, SPERM=args.sperm, POLITICAL=args.social, ECONOMIC=args.political, MILITARY=args.economic, SOCIAL=args.religion, RELIGION=args.military, RACIAL_FEATURE_LIST=args.racial_feature_list, PROFICIENCIES_LIST=args.proficiencies_list)
	print(f'city_name: {civ.CITY_NAME}')
	print(f'community_size: {civ.COMMUNITY_SIZE}')
	print(f'focus: {civ.SPERM}')
	print(f'social: {civ.POLITICAL}')
	print(f'political: {civ.ECONOMIC}')
	print(f'economic: {civ.MILITARY}')
	print(f'religion: {civ.SOCIAL}')
	print(f'military: {civ.RELIGION}')
	print(f'racial_feature_list: {civ.RACIAL_FEATURE_LIST}')
	print(f'proficiencies_list: {civ.PROFICIENCIES_LIST}')
	print()

	for i in civ:
		print(i)


#	civ.main()
