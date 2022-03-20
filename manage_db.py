
import csv, os, pandas as pd, sqlite3 as sl
from os.path import exists

def Create_DB():
	# Setup Filepath
	dir_path = os.path.join(os.environ['APPDATA'], 'CivGen')
	if not os.path.exists(dir_path):
	     os.makedirs(dir_path)

	# Check if resources.db exists
	resources_path = os.path.join(dir_path, 'resources.db') # Static DB
	res_exists = os.path.exists(resources_path)
	if (not res_exists):
		# Create resources.db
		resources = sl.connect(resources_path)
		res = resources.cursor()

		# Create Tables
		res.execute('''CREATE TABLE 'CLASS_LIST' (
		'id' integer not null primary key autoincrement,
		'class' text not null,
		'subclass' text not null
		)''')
		res.execute('CREATE TABLE COMMUNITY_SIZE_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('CREATE TABLE ECONOMIC_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('CREATE TABLE MILITARY_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('CREATE TABLE POLITICAL_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('''CREATE TABLE PROFICIENCIES (
		id INTEGER PRIMARY KEY,
		name varchar(255) NOT NULL,
		type varchar(255) NOT NULL,
		description varchar(255) NOT NULL
		)''')
		res.execute('''	CREATE TABLE RACIAL_FEATURE (
		id INTEGER PRIMARY KEY,
		name varchar(255) NOT NULL,
		type varchar(255) NOT NULL,
		description varchar(255) NOT NULL
		)''')
		res.execute('CREATE TABLE RELIGION_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('CREATE TABLE SOCIAL_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')
		res.execute('CREATE TABLE SPERM_LIST (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)')

		# Commit Changes
		resources.commit()

		# Populate Tables
		res.execute('insert into sqlite_sequence (name, seq) values (\'COMMUNITY_SIZE_LIST\',\'3\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'SPERM_LIST\',\'5\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'SOCIAL_LIST\',\'5\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'POLITICAL_LIST\',\'5\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'ECONOMIC_LIST\',\'8\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'RELIGION_LIST\',\'4\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'MILITARY_LIST\',\'4\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'CLASS_LIST\',\'116\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'PROFICIENCIES\',\'104\');')
		res.execute('insert into sqlite_sequence (name, seq) values (\'RACIAL_FEATURE\',\'57\');')
		res.execute('insert into \'SPERM_LIST\' (\'id\', \'name\') values (1, \'Social Activities\');')
		res.execute('insert into \'SPERM_LIST\' (\'id\', \'name\') values (2, \'Politics\');')
		res.execute('insert into \'SPERM_LIST\' (\'id\', \'name\') values (3, \'Economy\');')
		res.execute('insert into \'SPERM_LIST\' (\'id\', \'name\') values (4, \'Religion\');')
		res.execute('insert into \'SPERM_LIST\' (\'id\', \'name\') values (5, \'Military\');')
		res.execute('insert into \'SOCIAL_LIST\' (\'id\', \'name\') values (1, \'Taverns\');')
		res.execute('insert into \'SOCIAL_LIST\' (\'id\', \'name\') values (2, \'Theater\');')
		res.execute('insert into \'SOCIAL_LIST\' (\'id\', \'name\') values (3, \'Museum\');')
		res.execute('insert into \'SOCIAL_LIST\' (\'id\', \'name\') values (4, \'Library\');')
		res.execute('insert into \'SOCIAL_LIST\' (\'id\', \'name\') values (5, \'Restaurants\');')
		res.execute('insert into \'RELIGION_LIST\' (\'id\', \'name\') values (1, \'Monotheistic\');')
		res.execute('insert into \'RELIGION_LIST\' (\'id\', \'name\') values (2, \'Polytheistic\');')
		res.execute('insert into \'RELIGION_LIST\' (\'id\', \'name\') values (3, \'Atheistic\');')
		res.execute('insert into \'RELIGION_LIST\' (\'id\', \'name\') values (4, \'Agnostic\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have Resistance to acid Damage.\', 1, \'Acid Resistance\', \'Condition\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have Resistance to cold Damage.\', 2, \'Cold Resistance\', \'Condition\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have Resistance to fire Damage.\', 3, \'Fire Resistance\', \'Condition\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have Resistance to lightning Damage.\', 4, \'Lightning Resistance\', \'Condition\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have Resistance to poison Damage.\', 5, \'Poison Resistance\', \'Condition\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Common.\', 6, \'Language (Common)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Dwarvish.\', 7, \'Language (Dwarvish)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Elvish.\', 8, \'Language (Elvish)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Giant.\', 9, \'Language (Giant)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Gnomish.\', 10, \'Language (Gnomish)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Goblin.\', 11, \'Language (Goblin)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Halfling.\', 12, \'Language (Halfling)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Orc.\', 13, \'Language (Orc)\', \'Language\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size Small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan\'\'s Tools, such as leatherworker\'\'s Tools.\', 14, \'Cunning Artisan\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have advantage on saving throws against being charmed, and magic can’t put you to sleep.\', 15, \'Fey Ancestry\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed.\', 16, \'Friend Of The Sea\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'When you damage a creature with an attack or a spell and the creature\'\'s size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your level. Once you use this trait, you can\'\'t use it again until you finish a short or long rest.\', 17, \'Fury Of The Small\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You can hold your breath for up to 15 minutes at a time.\', 18, \'Hold Breath\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'When you make a melee attack on your turn, your reach for it is 5 feet greater than normal.\', 19, \'Long Limbed\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.\', 20, \'Mask Of The Wild\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You can move through the space of any creature that is of a size larger than yours.\', 21, \'Nimbleness\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.\', 22, \'Powerful Build\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.\', 23, \'Relentless Endurance\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.\', 24, \'Savage Attacks\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.\', 25, \'Speak With Small Beasts\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.\', 26, \'Stonecunning\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.\', 27, \'Sunlight Sensitivity\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.\', 28, \'Toughness\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Your darkvision has a radius of 120 feet.\', 29, \'Darkvision 120ft\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Your darkvision has a radius of 60 feet.\', 30, \'Darkvision 60ft\', \'Special\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a climbing speed of 20 feet.\', 31, \'Climbing Speed 20\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a climbing speed of 25 feet.\', 32, \'Climbing Speed 25\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a climbing speed of 30 feet.\', 33, \'Climbing Speed 30\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'Your base walking speed is 25 feet.\', 34, \'Walking Speed 25\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a swim speed of 20 feet.\', 35, \'Swim Speed 20\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a swim speed of 25 feet.\', 36, \'Swim Speed 25\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You have a swim speed of 30 feet.\', 37, \'Swim Speed 30\', \'Speed\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Animal Friendship spell and can cast it once a day without using a Spell Slot.\', 38, \'Spell Animal Friendship\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Burning Hands spell and can cast it once a day without using a Spell Slot.\', 39, \'Spell Burning Hands\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Create Or Destroy Water spell and can cast it once a day without using a Spell Slot.\', 40, \'Spell Create Or Destroy Water\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Dancing Lights Cantrip.\', 41, \'Spell Dancing Lights\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Darkness spell and can cast it once a day without using a Spell Slot.\', 42, \'Spell Darkness\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Druidcraft Cantrip.\', 43, \'Spell Druidcraft\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Faerie Fire spell and can cast it once a day without using a Spell Slot.\', 44, \'Spell Faerie Fire\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Fog Cloud spell and can cast it once a day without using a Spell Slot.\', 45, \'Spell Fog Cloud\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Friends Cantrip.\', 46, \'Spell Friends\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Gust Of Wind spell and can cast it once a day without using a Spell Slot.\', 47, \'Spell Gust Of Wind\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Hex spell and can cast it once a day without using a Spell Slot.\', 48, \'Spell Hex\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Levitate spell and can cast it once a day without using a Spell Slot.\', 49, \'Spell Levitate\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Light Cantrip.\', 50, \'Spell Light\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Mage Hand Cantrip.\', 51, \'Spell Mage Hand\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Minor Illusion Cantrip.\', 52, \'Spell Minor Illusion\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Pass Without Trace spell and can cast it once a day without using a Spell Slot.\', 53, \'Spell Pass Without Trace\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Produce Flame Cantrip.\', 54, \'Spell Produce Flame\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Shape Water Cantrip.\', 55, \'Spell Shapewater\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Thaumaturgy Cantrip.\', 56, \'Spell Thaumaturgy\', \'Spell\');')
		res.execute('insert into \'RACIAL_FEATURE\' (\'description\', \'id\', \'name\', \'type\') values (\'You know the Wall Of Water spell and can cast it once a day without using a Spell Slot.\', 57, \'Spell Wall Of Water\', \'Spell\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Abyssal.\', 1, \'Language (Abyssal)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Celestial.\', 2, \'Language (Celestial)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Deep Speech.\', 3, \'Language (Deep Speech)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Draconic.\', 4, \'Language (Draconic)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Infernal.\', 5, \'Language (Infernal)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Primordial.\', 6, \'Language (Primordial)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Sylvan.\', 7, \'Language (Sylvan)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You know how to read/write/speak Undercommon.\', 8, \'Language (Undercommon)\', \'Language\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Bagpipes.\', 9, \'Bagpipes\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Drum.\', 10, \'Drum\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Dulcimer.\', 11, \'Dulcimer\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Flute.\', 12, \'Flute\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Horn.\', 13, \'Horn\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Lute.\', 14, \'Lute\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Lyre.\', 15, \'Lyre\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Pan Flute.\', 16, \'Pan Flute\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Shawm.\', 17, \'Shawm\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Viol.\', 18, \'Viol\', \'Musical Instrument\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Acrobatics Skill.\', 19, \'Acrobatics\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Animal Handling Skill.\', 20, \'Animal Handling\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Arcana Skill.\', 21, \'Arcana\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Athletics Skill.\', 22, \'Athletics\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Deception Skill.\', 23, \'Deception\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the History Skill.\', 24, \'History\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Insight Skill.\', 25, \'Insight\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Intimidation Skill.\', 26, \'Intimidation\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Investigation Skill.\', 27, \'Investigation\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Medicine Skill.\', 28, \'Medicine\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Nature Skill.\', 29, \'Nature\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Perception Skill.\', 30, \'Perception\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Performance Skill.\', 31, \'Performance\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Persuasion Skill.\', 32, \'Persuasion\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Religion Skill.\', 33, \'Religion\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Sleight of Hand Skill.\', 34, \'Sleight of Hand\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Stealth Skill.\', 35, \'Stealth\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with the Survival Skill.\', 36, \'Survival\', \'Skill\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Alchemist\'\'s Supplies.\', 37, \'Alchemist\'\'s Supplies\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Brewer\'\'s Supplies.\', 38, \'Brewer\'\'s Supplies\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Calligrapher\'\'s Supplies.\', 39, \'Calligrapher\'\'s Supplies\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Carpenter\'\'s Tools.\', 40, \'Carpenter\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Cartographer\'\'s Tools.\', 41, \'Cartographer\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Cobbler\'\'s Tools.\', 42, \'Cobbler\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Cook\'\'s Utensils.\', 43, \'Cook\'\'s Utensils\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Dice Set.\', 44, \'Dice Set\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Disguise Kit.\', 45, \'Disguise Kit\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Dragonchess Set.\', 46, \'Dragonchess Set\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Forgery Kit.\', 47, \'Forgery Kit\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Glassblower\'\'s Tools.\', 48, \'Glassblower\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Herbalism Kit.\', 49, \'Herbalism Kit\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Jeweler\'\'s Tools.\', 50, \'Jeweler\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Land Vehicles.\', 51, \'Land Vehicles\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Leatherworker\'\'s Tools.\', 52, \'Leatherworker\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Mason\'\'s Tools.\', 53, \'Mason\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Navigator\'\'s Tools.\', 54, \'Navigator\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Painter\'\'s Supplies.\', 55, \'Painter\'\'s Supplies\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Playing Card Set.\', 56, \'Playing Card Set\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Poisoner\'\'s kit.\', 57, \'Poisoner\'\'s kit\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Potter\'\'s Tools.\', 58, \'Potter\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Smith\'\'s Tools.\', 59, \'Smith\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Thieves\'\' Tools.\', 60, \'Thieves\'\' Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Three-Dragon Ante Set.\', 61, \'Three-Dragon Ante Set\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Tinker\'\'s Tools.\', 62, \'Tinker\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Water Vehicles.\', 63, \'Water Vehicles\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Weaver\'\'s Tools.\', 64, \'Weaver\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Woodcarver\'\'s Tools.\', 65, \'Woodcarver\'\'s Tools\', \'Tool\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Battleaxes.\', 66, \'Battleaxe\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Blowguns.\', 67, \'Blowgun\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Clubs.\', 68, \'Club\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Daggers.\', 69, \'Dagger\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Darts.\', 70, \'Dart\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Flails.\', 71, \'Flail\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Glaives.\', 72, \'Glaive\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Greataxes.\', 73, \'Greataxe\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Greatclubs.\', 74, \'Greatclub\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Greatswords.\', 75, \'Greatsword\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Halberds.\', 76, \'Halberd\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Hand Crossbows.\', 77, \'Hand Crossbow\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Handaxes.\', 78, \'Handaxe\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Heavy Crossbows.\', 79, \'Heavy Crossbow\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Improvised Weapons.\', 80, \'Improvised Weapon\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Javelins.\', 81, \'Javelin\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Lances.\', 82, \'Lance\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Light Crossbows.\', 83, \'Light Crossbow\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Light Hammers.\', 84, \'Light Hammer\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Longbows.\', 85, \'Longbow\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Longswords.\', 86, \'Longsword\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Maces.\', 87, \'Mace\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Mauls.\', 88, \'Maul\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Morningstars.\', 89, \'Morningstar\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Nets.\', 90, \'Net\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Pikes.\', 91, \'Pike\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Quarterstaffs.\', 92, \'Quarterstaff\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Rapiers.\', 93, \'Rapier\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Scimitars.\', 94, \'Scimitar\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Shortbows.\', 95, \'Shortbow\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Shortswords.\', 96, \'Shortsword\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Sickles.\', 97, \'Sickle\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Slings.\', 98, \'Sling\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Spears.\', 99, \'Spear\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Tridents.\', 100, \'Trident\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Unarmed Strikes.\', 101, \'Unarmed Strike\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with War Picks.\', 102, \'War Pick\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Warhammers.\', 103, \'Warhammer\', \'Weapon\');')
		res.execute('insert into \'PROFICIENCIES\' (\'description\', \'id\', \'name\', \'type\') values (\'You are proficient with Whips.\', 104, \'Whip\', \'Weapon\');')
		res.execute('insert into \'POLITICAL_LIST\' (\'id\', \'name\') values (1, \'A Democratically Elected Leader\');')
		res.execute('insert into \'POLITICAL_LIST\' (\'id\', \'name\') values (2, \'The Monarchy\');')
		res.execute('insert into \'POLITICAL_LIST\' (\'id\', \'name\') values (3, \'A Military Government\');')
		res.execute('insert into \'POLITICAL_LIST\' (\'id\', \'name\') values (4, \'Anarchy\');')
		res.execute('insert into \'POLITICAL_LIST\' (\'id\', \'name\') values (5, \'An Oligarchy\');')
		res.execute('insert into \'MILITARY_LIST\' (\'id\', \'name\') values (1, \'A Local Militia\');')
		res.execute('insert into \'MILITARY_LIST\' (\'id\', \'name\') values (2, \'A Royal Guard Post\');')
		res.execute('insert into \'MILITARY_LIST\' (\'id\', \'name\') values (3, \'A Hunting Party\');')
		res.execute('insert into \'MILITARY_LIST\' (\'id\', \'name\') values (4, \'A Formal Town Guard\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (1, \'Agriculture\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (2, \'Farming\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (3, \'Fishing\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (4, \'Fashion\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (5, \'Technology\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (6, \'Travel\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (7, \'Mining\');')
		res.execute('insert into \'ECONOMIC_LIST\' (\'id\', \'name\') values (8, \'Lumber\');')
		res.execute('insert into \'COMMUNITY_SIZE_LIST\' (\'id\', \'name\') values (1, \'Village\');')
		res.execute('insert into \'COMMUNITY_SIZE_LIST\' (\'id\', \'name\') values (2, \'Town\');')
		res.execute('insert into \'COMMUNITY_SIZE_LIST\' (\'id\', \'name\') values (3, \'City\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Artificer\', 1, \'Alchemist\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Artificer\', 2, \'Armorer\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Artificer\', 3, \'Artillerist\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Artificer\', 4, \'Battle Smith\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 5, \'Path of the Ancestral Guardian\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 6, \'Path of the Battlerager\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 7, \'Path of the Beast\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 8, \'Path of the Berserker\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 9, \'Path of the Storm Herald\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 10, \'Path of the Totem Warrior\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 11, \'Path of Wild Magic\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Barbarian\', 12, \'Path of the Zealot\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 13, \'College of Creation\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 14, \'College of Eloquence\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 15, \'College of Glamour\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 16, \'College of Lore\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 17, \'College of Spirits\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 18, \'College of Swords\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 19, \'College of Valor\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Bard\', 20, \'College of Whispers\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 21, \'Arcana Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 22, \'Death Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 23, \'Forge Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 24, \'Grave Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 25, \'Knowledge Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 26, \'Life Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 27, \'Light Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 28, \'Nature Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 29, \'Order Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 30, \'Peace Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 31, \'Tempest Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 32, \'Trickery Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 33, \'Twilight Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Cleric\', 34, \'War Domain\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 35, \'Circle of Dreams\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 36, \'Circle of the Land\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 37, \'Circle of the Moon\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 38, \'Circle of the Shepherd\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 39, \'Circle of Spores\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 40, \'Circle of Stars\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Druid\', 41, \'Circle of Wildfire\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 42, \'Arcane Archer\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 43, \'Banneret\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 44, \'Battle Master\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 45, \'Cavalier\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 46, \'Champion\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 47, \'Echo Knight\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 48, \'Eldritch Knight\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 49, \'Psi Warrior\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 50, \'Rune Knight\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Fighter\', 51, \'Samurai\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 52, \'Way of Mercy\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 53, \'Way of the Ascendant Dragon\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 54, \'Way of the Astral Self\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 55, \'Way of the Drunken Master\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 56, \'Way of the Four Elements\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 57, \'Way of the Kensei\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 58, \'Way of the Long Death\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 59, \'Way of the Open Hand\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 60, \'Way of Shadow\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Monk\', 61, \'Way of the Sun Soul\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 62, \'Oath of the Ancients\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 63, \'Oath of Conquest\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 64, \'Oath of the Crown\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 65, \'Oath of Devotion\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 66, \'Oath of Glory\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 67, \'Oath of Redemption\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 68, \'Oath of Vengeance\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 69, \'Oath of the Watchers\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Paladin\', 70, \'Oathbreaker\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 71, \'Beast Master Conclave\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 72, \'Drakewarden\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 73, \'Fey Wanderer\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 74, \'Gloom Stalker Conclave\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 75, \'Horizon Walker Conclave\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 76, \'Hunter Conclave\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 77, \'Monster Slayer Conclave\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Ranger\', 78, \'Swarmkeeper\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 79, \'Arcane Trickster\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 80, \'Assassin\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 81, \'Inquisitive\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 82, \'Mastermind\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 83, \'Phantom\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 84, \'Scout\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 85, \'Soulknife\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 86, \'Swashbuckler\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Rogue\', 87, \'Thief\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 88, \'Aberrant Mind\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 89, \'Clockwork Soul\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 90, \'Draconic Bloodline\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 91, \'Divine Soul\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 92, \'Shadow Magic\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 93, \'Storm Sorcery\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Sorcerer\', 94, \'Wild Magic\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 95, \'Archfey\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 96, \'Celestial\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 97, \'Fathomless\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 98, \'Fiend\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 99, \'The Genie\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 100, \'Great Old One\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 101, \'Hexblade\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 102, \'Undead\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Warlock\', 103, \'Undying\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 104, \'School of Abjuration\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 105, \'School of Bladesinging\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 106, \'School of Chronurgy\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 107, \'School of Conjuration\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 108, \'School of Divination\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 109, \'School of Enchantment\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 110, \'School of Evocation\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 111, \'School of Graviturgy\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 112, \'School of Illusion\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 113, \'School of Necromancy\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 114, \'Order of Scribes\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 115, \'School of Transmutation\');')
		res.execute('insert into \'CLASS_LIST\' (\'class\', \'id\', \'subclass\') values (\'Wizard\', 116, \'School of War Magic\');')

		# Commit Changes and Close
		resources.commit()
		resources.close()

	## civilizations.db
	# Check if civilizations.db exists
	civdb_path = os.path.join(dir_path, 'civilizations.db') # Dynamic DB
	civ_exists = exists(civdb_path)
	if (not civ_exists):
		civilizations = sl.connect(civdb_path)
		civ = civilizations.cursor()

		# Create Tables
		civ.execute('''CREATE TABLE civilizations (
			id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			civ_name text NOT NULL,
			kingdom text NOT NULL,
			community_size text NOT NULL,
			sperm text NOT NULL,
			social text NOT NULL,
			political text NOT NULL,
			economic text NOT NULL,
			religion text NOT NULL,
			military text NOT NULL,
			racial_feature text NOT NULL,
			proficiencies text NOT NULL,
			subclasses text NOT NULL
		)''')
		civ.execute('''CREATE TABLE proficiencies (
			id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			proficiency1 text NOT NULL,
			proficiency2 text NOT NULL,
			proficiency3 text NOT NULL,
			proficiency4 text NOT NULL
		)''')
		civ.execute('''CREATE TABLE racial_feature (
			id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
			feature1 text NOT NULL,
			feature2 text NOT NULL,
			feature3 text NOT NULL,
			feature4 text NOT NULL
		)''')
		civ.execute('''CREATE TABLE subclasses (
			id integer not null primary key autoincrement,
			class1 text null,
			subclass1 text null,
			class2 text null,
			subclass2 text null
		)''')

		# Commit Changes
		civilizations.commit()

		# Populate Tables
		civ.execute('insert into sqlite_sequence (name, seq) values (\'civilizations\',\'0\');')
		civ.execute('insert into sqlite_sequence (name, seq) values (\'proficiencies\',\'0\');')
		civ.execute('insert into sqlite_sequence (name, seq) values (\'racial_feature\',\'0\');')
		civ.execute('insert into sqlite_sequence (name, seq) values (\'subclasses\',\'0\');')

		# Commit Changes and Close
		civilizations.commit()
		civilizations.close()

		return 1


def Export_DB(database):
	dir_path = os.path.join(os.environ['APPDATA'], 'CivGen')
	db_path = os.path.join(dir_path, database)
	path_exists = os.path.exists(os.path.join(dir_path,database.replace('.db','')))
	try: os.mkdir(f"{os.getcwd()}\{database.replace('.db','')}")
	except: pass
	conn = sl.connect(db_path, isolation_level=None,detect_types=sl.PARSE_COLNAMES)

	db_all_tables = pd.read_sql_query("SELECT name FROM sqlite_sequence", conn)
	db_all_table_names = db_all_tables.values.tolist()
	for i in db_all_table_names:
		print(i[0])
		db_tables = pd.read_sql_query(f"SELECT * FROM {i[0]}", conn)
		db_tables.to_csv(f"{database.replace('.db','')}/{i[0]}.csv", sep='\t', index=False)

	conn.close()

	return 1


def Import_DB(database):
	dir_path = os.path.join(os.environ['APPDATA'], 'CivGen')
	db_path = os.path.join(dir_path, database)
	path_exists = os.path.exists(os.path.join(dir_path,database.replace('.db','')))
	conn = sl.connect(db_path, isolation_level=None,detect_types=sl.PARSE_COLNAMES)

	return 1


if __name__ == "__main__":
	Import_DB('resources.db')
	Import_DB('civilizations.db')
	pass
