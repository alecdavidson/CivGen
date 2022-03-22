## Imports
import manage_db, tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from CivGen import Civilization
from CivGen import READ_LIST

## Establish Functions and Variables
civ = ""

# Read entries from civilizations.db
def read():
    # Grab global variables
    global kingdom
    # Execute READ_LIST()
    civ_list = READ_LIST(kingdom.get())
    # Print to CLI and output
    print(civ_list)
    output.insert(END, "City in Kingdom\n------------------------------\n")
    for i in civ_list:
        output.insert(END, "\u25C6", "List")
        output.insert(END, f" {i}\n", "List")
    output.insert(END, "_____________________________________________\n\n")
    output.see(END)

    return 1


# Save latest generated Civilization to civilizations.db
def save():
    global civ
    print(f"Saving {civ.CIV_NAME} of {civ.KINGDOM} (ID: {civ.id})")
    if civ.id == -1:
        civ.SAVE_DB()
    else:
        civ.UPDATE_DB()

    output.insert(END, f"Saving {civ.CIV_NAME} of {civ.KINGDOM} (ID: {civ.id})")
    output.insert(END, "\n_____________________________________________\n\n")
    output.see(END)

    return 1


# Create Civilization object and execute BUILD_CIVILIZATION()
def generate():
    global civ
    # Fromat List Inputs
    racial_feature_list_formated = [
        racial_feature_list.get("1.0", "1.0 lineend"),
        racial_feature_list.get("2.0", "2.0 lineend"),
        racial_feature_list.get("3.0", "3.0 lineend"),
        racial_feature_list.get("4.0", "4.0 lineend"),
    ]
    proficiencies_list_formated = [
        proficiencies_list.get("1.0", "1.0 lineend"),
        proficiencies_list.get("2.0", "2.0 lineend"),
        proficiencies_list.get("3.0", "3.0 lineend"),
        proficiencies_list.get("4.0", "4.0 lineend"),
    ]
    subclass_list_formated = [
        subclasses_list.get("1.0", "1.0 lineend"),
        subclasses_list.get("2.0", "2.0 lineend"),
        subclasses_list.get("3.0", "3.0 lineend"),
        subclasses_list.get("4.0", "4.0 lineend"),
    ]
    # Create Civilization Object
    civ = Civilization(
        CIV_NAME=civ_name.get(),
        KINGDOM=kingdom.get(),
        COMMUNITY_SIZE=community_size.get(),
        SPERM=sperm.get(),
        SOCIAL=social.get(),
        POLITICAL=political.get(),
        ECONOMIC=economic.get(),
        RELIGION=religion.get(),
        MILITARY=military.get(),
        RACIAL_FEATURE_LIST=racial_feature_list_formated,
        PROFICIENCIES_LIST=proficiencies_list_formated,
        SUBCLASSES_LIST=subclass_list_formated,
    )
    id = civ.BUILD_CIVILIZATION()
    # Print in CMD with PRINT_CIV()
    civ.PRINT_CIV()
    # Format Output
    output.insert(END, civ.CIV_NAME, "Entry")
    output.insert(END, " is a ")
    output.insert(END, civ.COMMUNITY_SIZE, "Entry")
    output.insert(END, " in ")
    output.insert(END, civ.KINGDOM, "Entry")
    output.insert(END, " with a large focus on its ")
    output.insert(END, civ.SPERM, "Entry")
    output.insert(END, ".\n")

    output.insert(END, "This ")
    output.insert(END, civ.COMMUNITY_SIZE, "Entry")
    output.insert(END, " is governed by ")
    output.insert(END, civ.POLITICAL, "Entry")
    output.insert(END, " where it's main export is ")
    output.insert(END, civ.ECONOMIC, "Entry")
    output.insert(END, ".\n")

    output.insert(END, civ.MILITARY, "Entry")
    output.insert(END, " oversees all conflict in ")
    output.insert(END, civ.CIV_NAME, "Entry")
    output.insert(END, ".\n")

    output.insert(END, "The locals of ")
    output.insert(END, civ.CIV_NAME, "Entry")
    output.insert(END, " spend their free time at one of its many ")
    output.insert(END, civ.SOCIAL, "Entry")
    output.insert(END, ".\n")

    output.insert(END, "Those who live here often find themselves ")
    output.insert(END, civ.RELIGION, "Entry")
    output.insert(END, ", but are tolerant of others beliefs.\n")

    output.insert(END, "\n")

    output.insert(
        END,
        "Families that have lived here for generations tend to have one or more of the following features:\n",
    )

    for i in range(len(civ.RACIAL_FEATURE_LIST)):
        output.insert(END, "\u25C6", "List")
        output.insert(END, f" {civ.RACIAL_FEATURE_LIST[i]}", "List")
        output.insert(END, "\n")

    output.insert(END, "\n")

    output.insert(
        END,
        "Anyone who has spent a decent amount of time here, likely has honed one or more of the following skills:\n",
    )

    for i in range(len(civ.PROFICIENCIES_LIST)):
        output.insert(END, "\u25C6", "List")
        output.insert(END, f" {civ.PROFICIENCIES_LIST[i]}", "List")
        output.insert(END, "\n")

    output.insert(END, "\n")

    output.insert(END, "Adventurers who have found their start in ")
    output.insert(END, civ.CIV_NAME, "Entry")
    output.insert(END, " tend to become ")
    output.insert(END, f"{civ.SUBCLASSES_LIST[0]}s ({civ.SUBCLASSES_LIST[1]})", "Entry")
    output.insert(END, " or ")
    output.insert(END, f"{civ.SUBCLASSES_LIST[2]}s ({civ.SUBCLASSES_LIST[3]})", "Entry")
    output.insert(END, ")\n")

    output.insert(END, "_____________________________________________\n\n")
    output.see(END)

    return 1


def imexport():
    imex = Toplevel(gui)
    imex.geometry("400x200")
    imex["background"] = "#999999"
    imex.title("Import/Export Databases")

    leftframe = Frame(imex)
    leftframe.pack(side="top", anchor=NW)
    rightframe = Frame(imex)
    rightframe.pack(side="top", anchor=NE)

    exp_res_lbl = tk.Label(leftframe, text="", bg="#999999")
    exp_res_btn = tk.Button(
        leftframe,
        relief=tk.RAISED,
        text="Export Resources to CSV",
        command=lambda: manage_db.Export_DB("resources.db"),
    )
    exp_res_lbl.pack(side="top")
    exp_res_btn.pack(side="top")

    return 1


## Execute
if __name__ == "__main__":
    # Create gui and Label it
    gui = tk.Tk()
    gui.title("5e Civilization Generator by Alec Davidson")
    gui.geometry("950x850")
    gui["background"] = "#999999"
    gui.iconbitmap("d20.ico")

    # Create Frames
    topframe = Frame(gui)
    topframe.pack(side="left", anchor=NW)
    topframe["background"] = "#999999"
    midframe = Frame(gui)
    midframe.pack(side="top")
    midframe["background"] = "#999999"
    botframe = Frame(gui)
    botframe.pack(side="left", anchor=NE)
    botframe["background"] = "#999999"

    # Create Title and Output
    Title = tk.Label(
        topframe,
        text="5e Civilization Generator",
        bg="#999999",
        font=("Calibri 18 bold underline"),
    )
    outputlbl = tk.Label(botframe, text="Results:", bg="#999999")
    output = scrolledtext.ScrolledText(
        botframe,
        wrap=tk.WORD,
        width=450,
        height=700,
        font=("Calibri 12"),
        bg="#000000",
        fg="#FFFFFF",
    )
    output.tag_config("Entry", foreground="pink", font="Calibri 12 bold underline")
    output.tag_config(
        "List",
        foreground="pink",
        font="Calibri 12 bold underline",
        lmargin1="10m",
        lmargin2="15m",
        tabs=["15m"],
    )

    # Create User Input Fields and Global Variables
    kingdomlbl = tk.Label(
        topframe, text="What is the name of your Kingdom?", bg="#999999"
    )
    kingdom = tk.Entry(topframe, relief=tk.SUNKEN)
    kingdom.insert(0, "Kingdom")
    civ_namelbl = tk.Label(
        topframe, text="What is the name of your Civilization?", bg="#999999"
    )
    civ_name = tk.Entry(topframe, relief=tk.SUNKEN)
    civ_name.insert(0, "Civ")

    community_sizelbl = tk.Label(
        topframe,
        text="How would you describe the Size of your Civilization?",
        bg="#999999",
    )
    community_size = tk.Entry(topframe, relief=tk.SUNKEN)
    spermlbl = tk.Label(
        topframe, text="What is the main Focus of your Civilization?", bg="#999999"
    )
    sperm = tk.Entry(topframe, relief=tk.SUNKEN)

    sociallbl = tk.Label(
        topframe,
        text="What is the key Social aspect of your Civilization?",
        bg="#999999",
    )
    social = tk.Entry(topframe, relief=tk.SUNKEN)
    politicallbl = tk.Label(
        topframe,
        text="What is the Policial structure of your Civilization?",
        bg="#999999",
    )
    political = tk.Entry(topframe, relief=tk.SUNKEN)
    economiclbl = tk.Label(
        topframe, text="What is the primary Export of your Civilization?", bg="#999999"
    )
    economic = tk.Entry(topframe, relief=tk.SUNKEN)
    religionlbl = tk.Label(
        topframe,
        text="What is the nature of your Civilizations Religion?",
        bg="#999999",
    )
    religion = tk.Entry(topframe, relief=tk.SUNKEN)
    militarylbl = tk.Label(
        topframe, text="What enforces the law in your Civilization?", bg="#999999"
    )
    military = tk.Entry(topframe, relief=tk.SUNKEN)

    racial_feature_listlbl = tk.Label(
        topframe,
        text="What are some features of the families in your Civilization? (Limit 4)",
        bg="#999999",
    )
    racial_feature_list = tk.Text(topframe, width=40, height=4, relief=tk.SUNKEN)
    proficiencies_listlbl = tk.Label(
        topframe,
        text="What are some skills honed by the people of your Civilization? (Limit 4)",
        bg="#999999",
    )
    proficiencies_list = tk.Text(topframe, width=40, height=4, relief=tk.SUNKEN)
    subclasses_listlbl = tk.Label(
        topframe,
        text="What type of Adventurer got their start in your Civilization?\n(Limit 2, alternate lines for 'Class' and 'Subclass')",
        bg="#999999",
    )
    subclasses_list = tk.Text(topframe, width=40, height=4, relief=tk.SUNKEN)

    # Create Buttons
    space = tk.Label(topframe, text="", bg="#999999")
    generate = tk.Button(
        topframe, relief=tk.RAISED, text="Generate Civilization", command=generate
    )
    read = tk.Button(
        topframe, relief=tk.RAISED, text="Print Saved Civilizations", command=read
    )
    save = tk.Button(
        topframe, relief=tk.RAISED, text="Save Latest Civilization", command=save
    )
    imex = tk.Button(
        topframe, relief=tk.RAISED, text="Import/Export Databases", command=imexport
    )

    # Pack Fields
    Title.pack(side="top")
    kingdomlbl.pack(side="top")
    kingdom.pack(side="top")
    civ_namelbl.pack(side="top")
    civ_name.pack(side="top")

    community_sizelbl.pack(side="top")
    community_size.pack(side="top")
    spermlbl.pack(side="top")
    sperm.pack(side="top")
    sociallbl.pack(side="top")
    social.pack(side="top")
    politicallbl.pack(side="top")
    political.pack(side="top")
    economiclbl.pack(side="top")
    economic.pack(side="top")
    religionlbl.pack(side="top")
    religion.pack(side="top")
    militarylbl.pack(side="top")
    military.pack(side="top")

    racial_feature_listlbl.pack(side="top")
    racial_feature_list.pack(side="top")
    proficiencies_listlbl.pack(side="top")
    proficiencies_list.pack(side="top")
    subclasses_listlbl.pack(side="top")
    subclasses_list.pack(side="top")

    space.pack(side="top")
    generate.pack(side="top")
    save.pack(side="top")
    read.pack(side="top")
    imex.pack(side="top")

    outputlbl.pack(side="top")
    output.pack(side="top")

    # Open gui
    print("You can minimize this gui, but do not close!")
    gui.mainloop()
