"""
CivGen V3 by Alec Davidson
"""
## Import Modules
import argparse, random, sqlite3 as sl, sys

## Global References
# Connect to DBs
resources = sl.connect('resources.db') # Static DB
civdb = sl.connect('civilizations.db') # Dynamic DB

# Define Classes
class Civilization():
	# Initialize the class with variables matching the table headers from the DB
	def __init__(self, id=-1, CIV_NAME="", COMMUNITY_SIZE="", SPERM="", POLITICAL="", ECONOMIC="", MILITARY="", SOCIAL="", RELIGION="", RACIAL_FEATURE_LIST = [], PROFICIENCIES_LIST = [], SUBCLASSES_LIST = []):
		self.id=id
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

	## Functions
	# Read the DB for existing Civilization
	def READ_DB(self):
		# Format and execute SQL command to Civilization DB
		sql = f"select * from civilizations where civ_name='{str(self.CIV_NAME)}';"
		with civdb:
			civ = civdb.execute(sql)

		# Parse variable and extract values to store in self
		for i in civ:
			self.id = i[0]
			self.CIV_NAME = i[1]
			self.COMMUNITY_SIZE = i[2]
			self.SPERM = i[3]
			self.SOCIAL = i[4]
			self.POLITICAL = i[5]
			self.ECONOMIC = i[6]
			self.RELIGION = i[7]
			self.MILITARY = i[8]

			# Lists are more complex, store to temp variable
			temp_RACIAL_FEATURE = i[9]
			temp_PROFICIENCIES = i[10]
			temp_SUBCLASSES = i[11]

			# Create temp lists
			temp_RACIAL_FEATURE_LIST = []
			temp_PROFICIENCIES_LIST = []
			temp_SUBCLASSES_LIST = []

			# The main table stores the ID of the list, but not the values
			# Make a new connection and query the additional tables
			with civdb:
				com = f"select * from racial_feature where id = {temp_RACIAL_FEATURE}"
				racial_feature = civdb.execute(com)
				# Nested for loops to store list for easier parsing later
				for i in racial_feature:
					for j in i:
						temp_RACIAL_FEATURE_LIST.append(j)
				# First value is the ID, we don't need that
				del temp_RACIAL_FEATURE_LIST[0]

				# Rinse and Repeat
				com = f"select * from proficiencies where id = {temp_PROFICIENCIES}"
				proficiencies = civdb.execute(com)
				for i in proficiencies:
					for j in i:
						temp_PROFICIENCIES_LIST.append(j)
				del temp_PROFICIENCIES_LIST[0]

				# And again
				com = f"select * from subclasses where id = {temp_SUBCLASSES}"
				subclasses = civdb.execute(com)
				for i in subclasses:
					for j in i:
						temp_SUBCLASSES_LIST.append(j)
				del temp_SUBCLASSES_LIST[0]

			# Now we get to store to self
			self.RACIAL_FEATURE_LIST = temp_RACIAL_FEATURE_LIST
			self.PROFICIENCIES_LIST = temp_PROFICIENCIES_LIST
			self.SUBCLASSES_LIST = temp_SUBCLASSES_LIST

		return self.id

	# Save Generated town to the DB for future References
	def SAVE_DB(self):
		# Save Racial Features to a seperate table on the DB
		# Format query and data
		sql_feature = 'INSERT INTO racial_feature (feature1,feature2,feature3,feature4,feature5) values(?,?,?,?,?)'
		data_feature = [
			(self.RACIAL_FEATURE_LIST[0],self.RACIAL_FEATURE_LIST[1],self.RACIAL_FEATURE_LIST[2],self.RACIAL_FEATURE_LIST[3],self.RACIAL_FEATURE_LIST[4])
		]
		# Connect to Civ DB and execute command
		with civdb:
			civdb.executemany(sql_feature, data_feature)
			# Get the ID of the entry we just created by making a query to sqlite_sequence table
			racial_feature = civdb.execute("select seq from sqlite_sequence where name = 'racial_feature'")
			racial_feature = [i[0] for i in racial_feature][0]

		# RInse and Repete with Proficiencies
		sql_proficiencies = 'INSERT INTO proficiencies (proficiency1,proficiency2,proficiency3,proficiency4,proficiency5) values(?,?,?,?,?)'
		data_proficiencies = [
			(self.PROFICIENCIES_LIST[0],self.PROFICIENCIES_LIST[1],self.PROFICIENCIES_LIST[2],self.PROFICIENCIES_LIST[3],self.PROFICIENCIES_LIST[4])
		]
		with civdb:
			civdb.executemany(sql_proficiencies, data_proficiencies)
			proficiencies = civdb.execute("select seq from sqlite_sequence where name = 'proficiencies'")
			proficiencies = [i[0] for i in proficiencies][0]

		# And Again with Subclasses
		sql_class = 'INSERT INTO subclasses (class1,subclass1,class2,subclass2) values(?,?,?,?)'
		data_class = [
			(self.SUBCLASSES_LIST[0],self.SUBCLASSES_LIST[1],self.SUBCLASSES_LIST[2],self.SUBCLASSES_LIST[3])
		]
		with civdb:
			civdb.executemany(sql_class, data_class)
			subclasses = civdb.execute("select seq from sqlite_sequence where name = 'subclasses'")
			subclasses = [i[0] for i in subclasses][0]

		# Finally, for Civilization we do the same as above, but with the ID references are stored instead of the actual data for the lists
		sql = f'INSERT INTO civilizations (civ_name,community_size,sperm,social,political,economic,religion,military,racial_feature,proficiencies,subclasses) values(?,?,?,?,?,?,?,?,?,?,?)'
		data = [
			(str(self.CIV_NAME),str(self.COMMUNITY_SIZE),str(self.SPERM),str(self.SOCIAL),str(self.POLITICAL),str(self.ECONOMIC),str(self.RELIGION),str(self.MILITARY),str(racial_feature),str(proficiencies),str(subclasses))
		]
		with civdb:
			civdb.executemany(sql, data)
			id = civdb.execute("select seq from sqlite_sequence where name = 'civilizations'")
			id = [i[0] for i in id][0]

		return id

	# If an existing entry was found, update that one instead of creating something new
	def UPDATE_DB(self):
		# Get ids for other tables
		sql_ids = f"select racial_feature,proficiencies,subclasses from civilizations where id='{int(self.id)}';"
		with civdb:
			idlist = []
			idlist_raw = civdb.execute(sql_ids)
			for i in idlist_raw:
				idlist.append(i)
		idlist = idlist[0]

		# Starting with Racial Features, Update the table
		sql_feature = 'UPDATE racial_feature SET feature1 = ? , feature2 = ? , feature3 = ? , feature4 = ? , feature5 = ? WHERE id = ?'
		data_feature = [
			(self.RACIAL_FEATURE_LIST[0],self.RACIAL_FEATURE_LIST[1],self.RACIAL_FEATURE_LIST[2],self.RACIAL_FEATURE_LIST[3],self.RACIAL_FEATURE_LIST[4],idlist[0])
		]
		with civdb:
			civdb.executemany(sql_feature, data_feature)

		# You know the drill... Proficiencies
		sql_proficiencies = 'UPDATE proficiencies SET proficiency1 = ? , proficiency2 = ? , proficiency3 = ? , proficiency4 = ? , proficiency5 = ? WHERE id = ?'
		data_proficiencies = [
			(self.PROFICIENCIES_LIST[0],self.PROFICIENCIES_LIST[1],self.PROFICIENCIES_LIST[2],self.PROFICIENCIES_LIST[3],self.PROFICIENCIES_LIST[4],idlist[1])
		]
		with civdb:
			civdb.executemany(sql_proficiencies, data_proficiencies)

		# Yup... Subclasses
		sql_class = 'UPDATE subclasses SET class1 = ? , subclass1 = ? , class2 = ? , subclass2 = ? WHERE id = ?'
		data_class = [
			(self.SUBCLASSES_LIST[0],self.SUBCLASSES_LIST[1],self.SUBCLASSES_LIST[2],self.SUBCLASSES_LIST[3],idlist[2])
		]
		with civdb:
			civdb.executemany(sql_class, data_class)

		# Finally... Civilization
		# Note, we store the IDs of the other tables instead of the full lists.
		sql = f'UPDATE civilizations SET civ_name = ? , community_size = ? , sperm = ? , social = ? , political = ? , economic = ? , religion = ? , military = ? , racial_feature = ? , proficiencies  = ? , subclasses = ? WHERE id = ?'
		data = [
			(str(self.CIV_NAME),str(self.COMMUNITY_SIZE),str(self.SPERM),str(self.SOCIAL),str(self.POLITICAL),str(self.ECONOMIC),str(self.RELIGION),str(self.MILITARY),idlist[0],idlist[1],idlist[2],self.id)
		]
		with civdb:
			civdb.executemany(sql, data)

		return self.id

	# Organized Print out of the Civilization
	def PRINT_CIV(self):
		# It prints
		print("")
		print(f"{self.CIV_NAME} is a {self.COMMUNITY_SIZE} with a large focus on its {self.SPERM}.")
		print(f"This {self.COMMUNITY_SIZE} is governed by {self.POLITICAL} where it's main export is {self.ECONOMIC}.")
		print(f"{self.MILITARY} oversees all conflict in {self.CIV_NAME}.")
		print(f"The locals of {self.CIV_NAME} spend their free time at one of its many {self.SOCIAL}.")
		print(f"Those who live here often find themselves {self.RELIGION}, but are tolerant of others beliefs.")
		print()
		print(f"The families that have been here for generations tend to have one or more of the following racial features:")
		for i in range(len(self.RACIAL_FEATURE_LIST)):
			print(f"\t*{self.RACIAL_FEATURE_LIST[i]}")
		print()
		print(f"Anyone who has spent a decent amount of time here, likely has developed one or more of the following skills:")
		for i in range(len(self.PROFICIENCIES_LIST)):
			print(f"\t*{self.PROFICIENCIES_LIST[i]}")
		print()
		print(f"Adventurers who have found their start in {self.CIV_NAME} tend to become {self.SUBCLASSES_LIST[0]}s ({self.SUBCLASSES_LIST[1]}) or {self.SUBCLASSES_LIST[2]}s ({self.SUBCLASSES_LIST[3]})")

		return 1

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
					temp.append(i[0])
					temp.append(i[1])
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

	# Generate a Civilization using the previous 2 functions
	def GEN_CIV(self):
		# Use the name of the Civilization as a seed for random
		random.seed(self.CIV_NAME)
		# Set each field using GET_DB_RANDOM and BUILD_RANDOM_LIST
		self.COMMUNITY_SIZE = self.GET_DB_RANDOM(table='COMMUNITY_SIZE_LIST')
		self.SPERM = self.GET_DB_RANDOM(table='SPERM_LIST')
		self.SOCIAL = self.GET_DB_RANDOM(table='SOCIAL_LIST')
		self.POLITICAL = self.GET_DB_RANDOM(table='POLITICAL_LIST')
		self.ECONOMIC = self.GET_DB_RANDOM(table='ECONOMIC_LIST')
		self.RELIGION = self.GET_DB_RANDOM(table='RELIGION_LIST')
		self.MILITARY = self.GET_DB_RANDOM(table='MILITARY_LIST')
		self.RACIAL_FEATURE_LIST = self.BUILD_RANDOM_LIST(table='RACIAL_FEATURE',total=5)
		self.PROFICIENCIES_LIST = self.BUILD_RANDOM_LIST(table='PROFICIENCIES',total=5)
		temp_SUBCLASSES_LIST = self.BUILD_RANDOM_LIST(table='CLASS_LIST',total=2)
		# For better formatting, break up the returned Class/Subclass's
		SUBCLASSES_LIST = []
		SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[0][0])
		SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[0][1])
		SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[1][0])
		SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[1][1])
		self.SUBCLASSES_LIST = SUBCLASSES_LIST

		return self

	# Main function of the class
	def BUILD_CIVILIZATION(self):
		# Store current values, they may contain manually entered values
		COMMUNITY_SIZE = self.COMMUNITY_SIZE
		SPERM = self.SPERM
		SOCIAL = self.SOCIAL
		POLITICAL = self.POLITICAL
		ECONOMIC = self.ECONOMIC
		RELIGION = self.RELIGION
		MILITARY = self.MILITARY
		RACIAL_FEATURE_LIST = self.RACIAL_FEATURE_LIST
		PROFICIENCIES_LIST = self.PROFICIENCIES_LIST
		SUBCLASSES_LIST = self.SUBCLASSES_LIST

		# Create a second Civ object with the same civ_name and generate details
		base = Civilization(CIV_NAME=self.CIV_NAME)
		base = base.GEN_CIV()

		# READ_DB overwrites the values in self with anything stored in the DB
		self.READ_DB()

		# If this is a new generation (id==-1) or user requests a RESET, overwrite self with base
		if self.id==-1 or COMMUNITY_SIZE=="RESET": self.COMMUNITY_SIZE = base.COMMUNITY_SIZE
		if self.id==-1 or SPERM=="RESET": self.SPERM = base.SPERM
		if self.id==-1 or SOCIAL=="RESET": self.SOCIAL = base.SOCIAL
		if self.id==-1 or POLITICAL=="RESET": self.POLITICAL = base.POLITICAL
		if self.id==-1 or ECONOMIC=="RESET": self.ECONOMIC = base.ECONOMIC
		if self.id==-1 or RELIGION=="RESET": self.RELIGION = base.RELIGION
		if self.id==-1 or MILITARY=="RESET": self.MILITARY = base.MILITARY
		if self.id==-1 or "RESET" in RACIAL_FEATURE_LIST: self.RACIAL_FEATURE_LIST = base.RACIAL_FEATURE_LIST
		if self.id==-1 or "RESET" in PROFICIENCIES_LIST: self.PROFICIENCIES_LIST = base.PROFICIENCIES_LIST
		if self.id==-1 or "RESET" in SUBCLASSES_LIST: self.SUBCLASSES_LIST = base.SUBCLASSES_LIST

		# Now check for anything else manually entered
		if COMMUNITY_SIZE != "RESET" and COMMUNITY_SIZE != "": self.COMMUNITY_SIZE = COMMUNITY_SIZE
		if SPERM != "RESET" and SPERM != "": self.SPERM = SPERM
		if SOCIAL != "RESET" and SOCIAL != "": self.SOCIAL = SOCIAL
		if POLITICAL != "RESET" and POLITICAL != "": self.POLITICAL = POLITICAL
		if ECONOMIC != "RESET" and ECONOMIC != "": self.ECONOMIC = ECONOMIC
		if RELIGION != "RESET" and RELIGION != "": self.RELIGION = RELIGION
		if MILITARY != "RESET" and MILITARY != "": self.MILITARY = MILITARY

		# For the lists, we overwrite in order.
		for i in range(len(self.RACIAL_FEATURE_LIST)):
			# If RESET was entered, use base
			if RACIAL_FEATURE_LIST[i]=="RESET": RACIAL_FEATURE_LIST[i] = base.RACIAL_FEATURE_LIST[i]
			# If nothing was entered, use self
			if RACIAL_FEATURE_LIST[i]=="": RACIAL_FEATURE_LIST[i] = self.RACIAL_FEATURE_LIST[i]
			# Both ifs will fail if something other than RESET is manually entered, and that value will be used
		self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST

		# And a 2
		for i in range(len(self.PROFICIENCIES_LIST)):
			if PROFICIENCIES_LIST[i]=="RESET": PROFICIENCIES_LIST[i] = base.PROFICIENCIES_LIST[i]
			if PROFICIENCIES_LIST[i]=="": PROFICIENCIES_LIST[i] = self.PROFICIENCIES_LIST[i]
		self.PROFICIENCIES_LIST = PROFICIENCIES_LIST

		# And a 3
		for i in range(len(self.SUBCLASSES_LIST)):
			if SUBCLASSES_LIST[i]=="RESET": SUBCLASSES_LIST[i] = base.SUBCLASSES_LIST[i]
			if SUBCLASSES_LIST[i]=="": SUBCLASSES_LIST[i] = self.SUBCLASSES_LIST[i]
		self.SUBCLASSES_LIST = SUBCLASSES_LIST

		return self.id

## Global Functions
# Get a list of all saved Civilizations
def READ_LIST():
	# COnnect to Civilizations DB and grab all civ_names
	sql = "select civ_name from civilizations;"
	with civdb:
		civ_list = civdb.execute(sql)

	# Parse through the returned data and restore for easier use
	civ_name_list = []
	for i in civ_list:
		civ_name_list.append(i[0])

	return civ_name_list

##Execute
if __name__=="__main__":
	# Parse the CLI for manually entered entities
	parser = argparse.ArgumentParser()#formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-r', '--read', action='store_true', help='If set, prints out existing Civs and enables Generation Looping', default=False)
	parser.add_argument('-c', '--civ_name', help='Set Civilization Name. *REQUIRED*', default='NULL')
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

	# Append nothing to the lists in order to match desired length
	while len(args.racial_feature_list) < 5: args.racial_feature_list.append("")
	while len(args.proficiencies_list) < 5: args.proficiencies_list.append("")
	while len(args.subclasses_list) < 4: args.subclasses_list.append("")

	# This main funciton will be used to loop generation in the CLI
	def main():
		# Give a list of all saved Civs
		READ_LIST()

		# Grab user name, all other fields will be generated randomly
		print("What is the name of your Civilization?")
		civ_name = input("> ")

		# Initialize object and build
		civ = Civilization(CIV_NAME=civ_name)
		civ.BUILD_CIVILIZATION()

		# Print out results
		civ.PRINT_CIV()

		# Set args.read to true to prevent additional generation
		args.read = True
		return 1

	# If True run main(), if False generate one Civ using any/all manually entered values
	while False: main()

	# If args.read==True, display saved Civs and do nothing, else generate
	if args.read: print(READ_LIST())
	else:
		# Create object with CLI Arguments and Build
		civ = Civilization(CIV_NAME=args.civ_name, COMMUNITY_SIZE=args.community_size, SPERM=args.sperm, POLITICAL=args.social, ECONOMIC=args.political, MILITARY=args.economic, SOCIAL=args.religion, RELIGION=args.military, RACIAL_FEATURE_LIST=args.racial_feature_list, PROFICIENCIES_LIST=args.proficiencies_list, SUBCLASSES_LIST=args.subclasses_list)
		id = civ.BUILD_CIVILIZATION()

		# Print out results and ask to save/update
		civ.PRINT_CIV()
		print("")
		print("Do you want to save this Civilization? (Y\\N)")
		save = input("> ")
		if save.lower() == 'y':
			if id==-1: civ.SAVE_DB()
			else: civ.UPDATE_DB()





























# Listen I just like to have some extra space at the end and ATOM is being a real cheese about it
