## Import Modules
import argparse, random, sqlite3 as sl, sys

## Global References
# Connect to DBs
resources = sl.connect('resources.db')

# Define Classes
class Civilization():
	def __init__(self, CIV_NAME="", COMMUNITY_SIZE="", SPERM="", POLITICAL="", ECONOMIC="", MILITARY="", SOCIAL="", RELIGION="", RACIAL_FEATURE_LIST = [], PROFICIENCIES_LIST = [], SUBCLASSES_LIST = []):
		self.CIV_NAME = CIV_NAME
		self.COMMUNITY_SIZE = COMMUNITY_SIZE
		self.SPERM = SPERM
		self.POLITICAL = POLITICAL
		self.ECONOMIC = ECONOMIC
		self.MILITARY = MILITARY
		self.SOCIAL = SOCIAL
		self.RELIGION = RELIGION
		self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST
		self.PROFICIENCIES_LIST =  PROFICIENCIES_LIST
		self.SUBCLASSES_LIST =  SUBCLASSES_LIST
		# Use the name of the Civilization as a seed for random
		random.seed(self.CIV_NAME)

	## Functions
	# Get a single random entry from DB
	def GET_DB_RANDOM(self, table):
		# Just need to know what table to use for the lookup
		with resources:
			# Get the total size of the table
			limit = resources.execute(f'select count() from {table};')
			# Format for funcitonality
			limit = [i[0] for i in limit][0]
			# Random entry
			id = random.randint(1,limit)
			# Grab entry
			try:
				#Most of these lists use name as their key
				entry = resources.execute(f'select name from {table} where id = {id};')
				entry = [i[0] for i in entry][0]
			except:
				#I decided it was a good idea to do Class/Subclass differently
				entry = resources.execute(f'select class,subclass from {table} where id = {id};')
				temp = []
				for i in entry:
					temp.append(i[0] + " (" + i[1] + ")")
				entry = temp
				#self.SUBCLASSES_LIST.replace('[','').replace(']','')
			# Final Result is returned
			return entry

	# Sometimes we need more than one entry for a field
	def BUILD_RANDOM_LIST(self, table, total):
		list = []
		# Use for/while loops to check for duplicates
		for i in range(total):
			temp = self.GET_DB_RANDOM(table)
			while temp in list: temp = self.GET_DB_RANDOM(table)
			list.append(temp)
		return list

	# Main function
	def BUILD_CIVILIZATION(self):
		# First generate something for each field based ONLY on the seed (Civilization Name)
		COMMUNITY_SIZE = self.GET_DB_RANDOM(table='COMMUNITY_SIZE_LIST')
		SPERM = self.GET_DB_RANDOM(table='SPERM_LIST')
		SOCIAL = self.GET_DB_RANDOM(table='SOCIAL_LIST')
		POLITICAL = self.GET_DB_RANDOM(table='POLITICAL_LIST')
		ECONOMIC = self.GET_DB_RANDOM(table='ECONOMIC_LIST')
		RELIGION = self.GET_DB_RANDOM(table='RELIGION_LIST')
		MILITARY = self.GET_DB_RANDOM(table='MILITARY_LIST')
		RACIAL_FEATURE_LIST = self.BUILD_RANDOM_LIST(table='RACIAL_FEATURE',total=5)
		PROFICIENCIES_LIST = self.BUILD_RANDOM_LIST(table='PROFICIENCIES',total=5)
		SUBCLASSES_LIST = self.BUILD_RANDOM_LIST(table='CLASS_LIST',total=2)

		# Now check for anything manually entered, only overwrite what's missing
		if self.COMMUNITY_SIZE == "": self.COMMUNITY_SIZE = COMMUNITY_SIZE
		if self.SPERM == "": self.SPERM = SPERM
		if self.SOCIAL == "": self.SOCIAL = SOCIAL
		if self.POLITICAL == "": self.POLITICAL = POLITICAL
		if self.ECONOMIC == "": self.ECONOMIC = ECONOMIC
		if self.RELIGION == "": self.RELIGION = RELIGION
		if self.MILITARY == "": self.MILITARY = MILITARY

		# For the lists, we overwrite in order.
		# 3 entered items will overwrite the first 3 random entities
		if self.RACIAL_FEATURE_LIST == []: self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST
		else:
			for i in range(len(self.RACIAL_FEATURE_LIST)):
				RACIAL_FEATURE_LIST[i] = self.RACIAL_FEATURE_LIST[i]
			self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST

		if self.PROFICIENCIES_LIST== []: self.PROFICIENCIES_LIST = PROFICIENCIES_LIST
		else:
			for i in range(len(self.PROFICIENCIES_LIST)):
				PROFICIENCIES_LIST[i] = self.PROFICIENCIES_LIST[i]
			self.PROFICIENCIES_LIST = PROFICIENCIES_LIST

		if self.SUBCLASSES_LIST== []: self.SUBCLASSES_LIST = SUBCLASSES_LIST
		else:
			for i in range(len(self.SUBCLASSES_LIST)):
				SUBCLASSES_LIST[i] = self.SUBCLASSES_LIST[i]
			self.SUBCLASSES_LIST = SUBCLASSES_LIST

		return 0


##Execute
if __name__=="__main__":
	# Parse the CLI for manually entered entities
	parser = argparse.ArgumentParser()#formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-c', '--civ_name', help='Set Civilization Name. *REQUIRED*')
	parser.add_argument('--community_size', help='Set Community Size', default='')
	parser.add_argument('--sperm', help='Set Focus', default='')
	parser.add_argument('--social', help='Set Social', default='')
	parser.add_argument('--political', help='Set Political', default='')
	parser.add_argument('--economic', help='Set Economy', default='')
	parser.add_argument('--religion', help='Set Religion', default='')
	parser.add_argument('--military', help='Set Military', default='')
	parser.add_argument('--racial_feature_list', action='append', help='Add Racial Feature', default=[])
	parser.add_argument('--proficiencies_list', action='append', help='Add Proficiency', default=[])
	parser.add_argument('--subclasses_list', action='append', help='Add SubClass', default=[])
	args = parser.parse_args()

	# This main funciton will be used to loop generation in the CLI
	def main():
		# Grab user name, all other fields will be generated randomly
		# Parsed Arguments will be ignored
		print("What is the name of your Civilization?")
		civ_name = input("> ")
		civ = Civilization(CIV_NAME=civ_name)
		civ.BUILD_CIVILIZATION()

		# Print out results
		print(f"{civ.CIV_NAME} is a {civ.COMMUNITY_SIZE} with a large focus on its {civ.SPERM}.")
		print(f"This {civ.COMMUNITY_SIZE} is governed by {civ.POLITICAL} where it's main export is {civ.ECONOMIC}.")
		print(f"{civ.MILITARY} oversees all conflict in {civ.CIV_NAME}.")
		print(f"The locals of {civ.CIV_NAME} spend their free time at one of its many {civ.SOCIAL}.")
		print(f"Those who live here often find themselves {civ.RELIGION}, but are tolerant of others beliefs.")
		print()
		print(f"The families that have been here for generations tend to have one or more of the following racial features:")
		for i in range(len(civ.RACIAL_FEATURE_LIST)):
			print(f"\t*{civ.RACIAL_FEATURE_LIST[i]}")
		print()
		print(f"Anyone who has spent a decent amount of time here, likely has developed one or more of the following skills:")
		for i in range(len(civ.PROFICIENCIES_LIST)):
			print(f"\t*{civ.PROFICIENCIES_LIST[i]}")
		print()
		print(f"Adventurers who have found their start in {civ.CIV_NAME} tend to become {civ.SUBCLASSES_LIST[0][0]} or {str(civ.SUBCLASSES_LIST[1][0])}")

	#If False, generate once with CLI and ArgParser, if True ask name and loop
	while False: main()

	# Create object with CLI Arguments and Build
	civ = Civilization(CIV_NAME=args.civ_name, COMMUNITY_SIZE=args.community_size, SPERM=args.sperm, POLITICAL=args.social, ECONOMIC=args.political, MILITARY=args.economic, SOCIAL=args.religion, RELIGION=args.military, RACIAL_FEATURE_LIST=args.racial_feature_list, PROFICIENCIES_LIST=args.proficiencies_list, SUBCLASSES_LIST=args.subclasses_list)
	civ.BUILD_CIVILIZATION()

	# Print out results.
	print(f"{civ.CIV_NAME} is a {civ.COMMUNITY_SIZE} with a large focus on its {civ.SPERM}.")
	print(f"This {civ.COMMUNITY_SIZE} is governed by {civ.POLITICAL} where it's main export is {civ.ECONOMIC}.")
	print(f"{civ.MILITARY} oversees all conflict in {civ.CIV_NAME}.")
	print(f"The locals of {civ.CIV_NAME} spend their free time at one of its many {civ.SOCIAL}.")
	print(f"Those who live here often find themselves {civ.RELIGION}, but are tolerant of others beliefs.")
	print()
	print(f"The families that have been here for generations tend to have one or more of the following racial features:")
	for i in range(len(civ.RACIAL_FEATURE_LIST)):
		print(f"\t*{civ.RACIAL_FEATURE_LIST[i]}")
	print()
	print(f"Anyone who has spent a decent amount of time here, likely has developed one or more of the following skills:")
	for i in range(len(civ.PROFICIENCIES_LIST)):
		print(f"\t*{civ.PROFICIENCIES_LIST[i]}")
	print()
	print(f"Adventurers who have found their start in {civ.CIV_NAME} tend to become {civ.SUBCLASSES_LIST[0][0]} or {str(civ.SUBCLASSES_LIST[1][0])}")






























# Listen I just like to have some extra space at the end and ATOM is being a real cheese about it
