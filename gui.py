## Imports
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from CivGen import Civilization
from CivGen import READ_LIST

## Establish Functions
# Read entries from civilizations.db
def read():
	# Grab global variables
	global kingdom
	# Execute READ_LIST()
	civ_list = READ_LIST(kingdom.get())
	# Print to CLI and output
	print(civ_list)
	output.insert(END,"City in Kingdom\n_______________\n")
	for i in civ_list:
		output.insert(END,f"{i}\n")
	output.insert(END,"\n")

# Create Civilization object and execute BUILD_CIVILIZATION()
def generate():
	# Grab global variables
	global kingdom,civ_name
	# Create Civilization Object
	civ = Civilization(CIV_NAME=civ_name.get(), KINGDOM=kingdom.get(), COMMUNITY_SIZE='', SPERM='', POLITICAL='', ECONOMIC='', MILITARY='', SOCIAL='', RELIGION='', RACIAL_FEATURE_LIST=['','','',''], PROFICIENCIES_LIST=['','','',''], SUBCLASSES_LIST=['','','',''])
	id = civ.BUILD_CIVILIZATION()
	# Print in CMD with PRINT_CIV()
	civ.PRINT_CIV()
	# Format Output
	output.insert(END,civ.CIV_NAME,'Entry')
	output.insert(END," is a ")
	output.insert(END,civ.COMMUNITY_SIZE,'Entry')
	output.insert(END," in ")
	output.insert(END,civ.KINGDOM,'Entry')
	output.insert(END," with a large focus on its ")
	output.insert(END,civ.SPERM,'Entry')
	output.insert(END,".\n")

	output.insert(END,"This ")
	output.insert(END,civ.COMMUNITY_SIZE,'Entry')
	output.insert(END," is governed by ")
	output.insert(END,civ.POLITICAL,'Entry')
	output.insert(END," where it's main export is ")
	output.insert(END,civ.ECONOMIC,'Entry')
	output.insert(END,".\n")

	output.insert(END,civ.MILITARY,'Entry')
	output.insert(END," oversees all conflict in ")
	output.insert(END,civ.CIV_NAME,'Entry')
	output.insert(END,".\n")

	output.insert(END,"The locals of ")
	output.insert(END,civ.CIV_NAME,'Entry')
	output.insert(END," spend their free time at one of its many ")
	output.insert(END,civ.SOCIAL,'Entry')
	output.insert(END,".\n")

	output.insert(END,"Those who live here often find themselves ")
	output.insert(END,civ.RELIGION,'Entry')
	output.insert(END,", but are tolerant of others beliefs.\n")

	output.insert(END,"\n")

	output.insert(END,"Families that have lived here for generations tend to have one or more of the following features:\n")

	for i in range(len(civ.RACIAL_FEATURE_LIST)):
		output.insert(END,"\t*")
		output.insert(END,civ.RACIAL_FEATURE_LIST[i],'Entry')
		output.insert(END,"\n")

	output.insert(END,"\n")

	output.insert(END,"Anyone who has spent a decent amount of time here, likely has honed one or more of the following skills:\n")

	for i in range(len(civ.PROFICIENCIES_LIST)):
		output.insert(END,"\t*")
		output.insert(END,civ.PROFICIENCIES_LIST[i],'Entry')
		output.insert(END,"\n")

	output.insert(END,"\n")

	output.insert(END,"Adventurers who have found their start in ")
	output.insert(END,civ.CIV_NAME,'Entry')
	output.insert(END," tend to become ")
	output.insert(END,f"{civ.SUBCLASSES_LIST[0]}s ({civ.SUBCLASSES_LIST[1]})",'Entry')
	output.insert(END," or ")
	output.insert(END,f"{civ.SUBCLASSES_LIST[2]}s ({civ.SUBCLASSES_LIST[3]})",'Entry')
	output.insert(END,")\n")

	output.insert(END,"-------------------------\n")

	output.insert(END,"\n")

	return 1

## Execute
if __name__=="__main__":
	# Create gui and Label it
	gui = tk.Tk()
	gui.geometry("900x700")
	gui['background']='#999999'

	# Create Frames
	topframe = Frame(gui)
	topframe.pack(side="top")
	topframe['background']='#BBBBBB'
	midframe = Frame(gui)
	midframe.pack()
	midframe['background']='#BBBBBB'
	botframe = Frame(gui)
	botframe.pack(side="bottom")
	botframe['background']='#999999'

	# Create Title and Output
	Title = tk.Label(topframe, text="5e Civilization Generator",bg='#BBBBBB')
	outputlbl = tk.Label(botframe, text="Results:",bg='#999999')
	output = scrolledtext.ScrolledText(botframe, wrap=tk.WORD,width=400,height=150,font=("Calibri 12"),bg='#000000',fg='#FFFFFF')
	output.tag_config('Entry',foreground='pink',font="Calibri 12 bold underline")

	# Create User Input Fields and Global Variables
	kingdomlbl = tk.Label(topframe, text="What is the name of your Kingdom?",bg='#BBBBBB')
	kingdom = tk.Entry(topframe, relief=tk.SUNKEN)
	kingdom.insert(0,'Kingdom')
	civ_namelbl = tk.Label(topframe, text="What is the name of your Civilization?",bg='#BBBBBB')
	civ_name = tk.Entry(topframe, relief=tk.SUNKEN)
	civ_name.insert(0,'Civ')

	#	parser.add_argument('-r', '--read', action='store_true', help='If set, prints out existing Civs and enables Generation Looping', default=False)
	#	parser.add_argument('-c', '--civ_name', help='Set Civilization Name. *REQUIRED*', default='NULL')
	#	parser.add_argument('-k', '--kingdom', help='Set Kingdom Name. *REQUIRED*', default='NULL')
	#	parser.add_argument('--community_size', help='Set Community Size', default='')
	#	parser.add_argument('--sperm', help='Set Focus', default='')
	#	parser.add_argument('--social', help='Set Social', default='')
	#	parser.add_argument('--political', help='Set Political', default='')
	#	parser.add_argument('--economic', help='Set Economy', default='')
	#	parser.add_argument('--religion', help='Set Religion', default='')
	#	parser.add_argument('--military', help='Set Military', default='')
	#	parser.add_argument('--racial_feature_list', action='append', help='Add Racial Feature', default=[])
	#	parser.add_argument('--proficiencies_list', action='append', help='Add Proficiency', default=[])
	#	parser.add_argument('--subclasses_list', action='append', help='Add SubClass', default=[])


	# Create Buttons
	generatelbl = tk.Label(topframe, text='', bg='#BBBBBB')
	generate = tk.Button(topframe, relief=tk.RAISED, text="Generate Civilization",command=generate)
	generatelbl2 = tk.Label(topframe, text='', bg='#BBBBBB')
	readlbl = tk.Label(topframe, text='', bg='#BBBBBB')
	read = tk.Button(topframe, relief=tk.RAISED, text="Output Civilizations",command=read)
	readlbl2 = tk.Label(topframe, text='', bg='#BBBBBB')

	# Pack Fields
	Title.pack(side="top")
	kingdomlbl.pack(side="top")
	kingdom.pack(side="top")
	civ_namelbl.pack(side="top")
	civ_name.pack(side="top")
	generatelbl.pack(side="top")
	generate.pack(side="top")
	generatelbl2.pack(side="top")
	readlbl.pack(side="top")
	read.pack(side="top")
	readlbl2.pack(side="top")
	outputlbl.pack()
	output.pack(side="bottom")

	# Open gui
	print("You can minimize this gui, but do not close!")
	gui.mainloop()
