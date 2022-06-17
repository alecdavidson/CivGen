## Imports
import CivGen, os, sys, tkinter as tk
from CivGen import Civilization, READ_LIST
from functools import partial
from tkinter import *
from tkinter import Canvas, Menu, scrolledtext, ttk
from PIL import Image, ImageTk
import pyi_splash

# Update the text on the splash screen
pyi_splash.update_text("PyInstaller is a great software!")
pyi_splash.update_text("Second time's a charm!")

# Close the splash screen. It does not matter when the call
# to this function is made, the splash screen remains open until
# this function is called or the Python program is terminated.
pyi_splash.close()

## Establish Functions and Variables
civ = ""
added_input = False
try:
    local_path = sys._MEIPASS
except:
    local_path = os.path.abspath(".")

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
    new_id = civ.id
    if civ.id == -1:
        new_id = civ.SAVE_DB()
    else:
        civ.UPDATE_DB()

    print(f"Saved {civ.CIV_NAME} of {civ.KINGDOM} (ID: {new_id})")
    output.insert(END, f"Saved {civ.CIV_NAME} of {civ.KINGDOM} (ID: {new_id})")
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
        output.insert(
            END,
            f" {civ.RACIAL_FEATURE_LIST[i]}",
            "List",
        )
        output.insert(END, "\n")

    output.insert(END, "\n")

    output.insert(
        END,
        "Anyone who has spent a decent amount of time here, likely has honed one or more of the following skills:\n",
    )

    for i in range(len(civ.PROFICIENCIES_LIST)):
        output.insert(END, "\u25C6", "List")
        output.insert(
            END,
            f" {civ.PROFICIENCIES_LIST[i]}",
            "List",
        )
        output.insert(END, "\n")

    output.insert(END, "\n")

    output.insert(END, "Adventurers who have found their start in ")
    output.insert(END, civ.CIV_NAME, "Entry")
    output.insert(END, " tend to become ")
    output.insert(END, f"{civ.SUBCLASSES_LIST[1]}s ({civ.SUBCLASSES_LIST[0]})", "Entry")
    output.insert(END, " or ")
    output.insert(END, f"{civ.SUBCLASSES_LIST[3]}s ({civ.SUBCLASSES_LIST[2]})", "Entry")
    output.insert(END, "\n")

    output.insert(END, "_____________________________________________\n\n")
    output.see(END)

    return 1


# Convert CSVs to DB
def dbimport(db):
    result = CivGen.Import_DB(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


# Export DB content into CSVs
def dbexport(db):
    result = CivGen.Export_DB(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


# Rollback DB to previous version
def dbrollback(db):
    result = CivGen.dbrollback(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


# Create a new window with information
def about(about_type):
    # Create new Window
    about_window = Tk()
    about_window.title("Civilization Generator by Alec Davidson")
    about_window.geometry("750x650")
    about_window["background"] = "#999999"
    about_window.iconbitmap(os.path.join(local_path, "d20.ico"))

    # Open file
    data = ""
    if about_type == "readme":
        aboutf = open(os.path.join(local_path, "README.md"), "r")
        for i in aboutf:
            data += i
    elif about_type == "how":
        aboutf = open(os.path.join(local_path, "INSTRUCTIONS.md"), "r")
        for i in aboutf:
            data += i
    else:
        pass

    # pack textbox with text
    textbox = Text(about_window)
    textbox.insert(END, data)
    textbox.pack(expand=True, fill=BOTH)

    return 1


# Allow for User input for other details
def add_input():
    global added_input

    if added_input == False:
        community_sizelbl.pack(anchor="w", padx=25)
        community_size.pack(anchor="w", padx=25, fill=BOTH)
        spermlbl.pack(anchor="w", padx=25)
        sperm.pack(anchor="w", padx=25, fill=BOTH)
        sociallbl.pack(anchor="w", padx=25)
        social.pack(anchor="w", padx=25, fill=BOTH)
        politicallbl.pack(anchor="w", padx=25)
        political.pack(anchor="w", padx=25, fill=BOTH)
        economiclbl.pack(anchor="w", padx=25)
        economic.pack(anchor="w", padx=25, fill=BOTH)
        religionlbl.pack(anchor="w", padx=25)
        religion.pack(anchor="w", padx=25, fill=BOTH)
        militarylbl.pack(anchor="w", padx=25)
        military.pack(anchor="w", padx=25, fill=BOTH)

        racial_feature_listlbl.pack(anchor="w", padx=25)
        racial_feature_list.pack(anchor="w", padx=25, fill=BOTH)
        proficiencies_listlbl.pack(anchor="w", padx=25)
        proficiencies_list.pack(anchor="w", padx=25, fill=BOTH)
        subclasses_listlbl.pack(anchor="w", padx=25)
        subclasses_list.pack(anchor="w", padx=25, fill=BOTH)

        d20canvas.pack_forget()

        added_input = True
    else:
        community_sizelbl.pack_forget()
        community_size.pack_forget()
        spermlbl.pack_forget()
        sperm.pack_forget()
        sociallbl.pack_forget()
        social.pack_forget()
        politicallbl.pack_forget()
        political.pack_forget()
        economiclbl.pack_forget()
        economic.pack_forget()
        religionlbl.pack_forget()
        religion.pack_forget()
        militarylbl.pack_forget()
        military.pack_forget()

        racial_feature_listlbl.pack_forget()
        racial_feature_list.pack_forget()
        proficiencies_listlbl.pack_forget()
        proficiencies_list.pack_forget()
        subclasses_listlbl.pack_forget()
        subclasses_list.pack_forget()

        d20canvas.pack(fill=BOTH, expand=True)

        added_input = False
    return 1


## Execute
if __name__ == "__main__":
    # Create gui and Label it
    gui = Tk()
    gui.title("Civilization Generator by Alec Davidson")
    gui.geometry("950x850")
    gui["background"] = "#999999"
    gui.iconbitmap(os.path.join(local_path, "d20.ico"))

    # Create the Menubar
    menubar = Menu(gui)
    gui.config(menu=menubar)
    # Import and Export
    imex_menu = Menu(menubar, tearoff=False)
    ex_menu = Menu(menubar, tearoff=False)
    im_menu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Import/Export", menu=imex_menu)
    imex_menu.add_cascade(label="Export", menu=ex_menu)
    imex_menu.add_cascade(label="Import", menu=im_menu)
    im_menu.add_command(
        label="Import Civilizations",
        command=lambda: dbimport("civilizations.db"),
    )
    im_menu.add_command(
        label="Import Resources", command=lambda: dbimport("resources.db")
    )
    im_menu.add_command(
        label="Rollback Civilizations",
        command=lambda: dbrollback("civilizations.db"),
    )
    im_menu.add_command(
        label="Rollback Resources",
        command=lambda: dbrollback("Resources.db"),
    )
    ex_menu.add_command(
        label="Export Civilizations",
        command=lambda: dbexport("civilizations.db"),
    )
    ex_menu.add_command(
        label="Export Resources", command=lambda: dbexport("resources.db")
    )

    # About CivGen
    about_menu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="How to use", command=lambda: about("how"))
    about_menu.add_command(label="About CivGen", command=lambda: about("readme"))

    # Create Frames
    leftframe = Frame(
        gui,
        width=450,
        height=900,
    )
    leftframe.pack(side="left", anchor=NW)
    leftframe.pack_propagate(0)
    leftframe["background"] = "#999999"
    rightframe = Frame(
        gui,
        width=500,
        height=900,
    )
    rightframe.pack(side="right", anchor=NE)
    rightframe.pack_propagate(0)
    rightframe["background"] = "#999999"

    # Create Title and Output
    Title = tk.Label(
        leftframe,
        text="Civilization Generator",
        bg="#999999",
        font=("Calibri 18 bold underline"),
    )
    outputlbl = tk.Label(rightframe, text="Results:", bg="#999999")
    output = scrolledtext.ScrolledText(
        rightframe,
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

    # Add d20 image
    d20image = Image.open(os.path.join(local_path, "d20.png")).convert("RGBA")
    d20pic = ImageTk.PhotoImage(d20image)
    d20canvas = Canvas(leftframe, bg="#999999", highlightthickness=0)
    d20canvas.create_image(200, 400, image=d20pic)
    # d20lbl = Label(leftframe, image=d20pic)

    # Create User Input Fields and Global Variables
    kingdomlbl = tk.Label(
        leftframe, text="What is the name of your Kingdom?", bg="#999999"
    )
    kingdom = tk.Entry(leftframe, relief=tk.SUNKEN)
    kingdom.insert(0, "Kingdom")
    civ_namelbl = tk.Label(
        leftframe, text="What is the name of your Civilization?", bg="#999999"
    )
    civ_name = tk.Entry(leftframe, relief=tk.SUNKEN)
    civ_name.insert(0, "Civ")

    community_sizelbl = tk.Label(
        leftframe,
        text="How would you describe the Size of your Civilization?",
        bg="#999999",
    )
    community_size = tk.Entry(leftframe, relief=tk.SUNKEN)
    spermlbl = tk.Label(
        leftframe, text="What is the main Focus of your Civilization?", bg="#999999"
    )
    sperm = tk.Entry(leftframe, relief=tk.SUNKEN)

    sociallbl = tk.Label(
        leftframe,
        text="What is the key Social aspect of your Civilization?",
        bg="#999999",
    )
    social = tk.Entry(leftframe, relief=tk.SUNKEN)
    politicallbl = tk.Label(
        leftframe,
        text="What is the Policial structure of your Civilization?",
        bg="#999999",
    )
    political = tk.Entry(leftframe, relief=tk.SUNKEN)
    economiclbl = tk.Label(
        leftframe, text="What is the primary Export of your Civilization?", bg="#999999"
    )
    economic = tk.Entry(leftframe, relief=tk.SUNKEN)
    religionlbl = tk.Label(
        leftframe,
        text="What is the nature of your Civilizations Religion?",
        bg="#999999",
    )
    religion = tk.Entry(leftframe, relief=tk.SUNKEN)
    militarylbl = tk.Label(
        leftframe, text="What enforces the law in your Civilization?", bg="#999999"
    )
    military = tk.Entry(leftframe, relief=tk.SUNKEN)

    racial_feature_listlbl = tk.Label(
        leftframe,
        text="What are some features of the families in your Civilization? (Limit 4)",
        bg="#999999",
    )
    racial_feature_list = tk.Text(leftframe, width=40, height=4, relief=tk.SUNKEN)
    proficiencies_listlbl = tk.Label(
        leftframe,
        text="What are some skills honed by the people of your Civilization? (Limit 4)",
        bg="#999999",
    )
    proficiencies_list = tk.Text(leftframe, width=40, height=4, relief=tk.SUNKEN)
    subclasses_listlbl = tk.Label(
        leftframe,
        text="What type of Adventurer got their start in your Civilization?\n(Limit 2, alternate lines for 'Class' and 'Subclass')",
        bg="#999999",
        justify=LEFT,
    )
    subclasses_list = tk.Text(leftframe, width=40, height=4, relief=tk.SUNKEN)

    # Create Buttons
    generate = tk.Button(
        leftframe, relief=tk.RAISED, text="Generate Civilization", command=generate
    )
    read = tk.Button(
        leftframe, relief=tk.RAISED, text="Print Saved Civilizations", command=read
    )
    save = tk.Button(
        leftframe, relief=tk.RAISED, text="Save Latest Civilization", command=save
    )
    add_inputbtn = tk.Button(
        leftframe, relief=tk.RAISED, text="Manually Enter Details", command=add_input
    )

    # Pack Fields
    Title.pack()
    kingdomlbl.pack(anchor="w", padx=25)
    kingdom.pack(anchor="w", padx=25, fill=BOTH)
    civ_namelbl.pack(anchor="w", padx=25)
    civ_name.pack(anchor="w", padx=25, fill=BOTH)

    generate.pack(fill=BOTH, pady=(5, 2), padx=70)
    save.pack(fill=BOTH, padx=70, pady=2)
    read.pack(fill=BOTH, padx=70, pady=2)
    add_inputbtn.pack(fill=BOTH, padx=70, pady=2)

    d20canvas.pack(fill=BOTH, expand=True)

    outputlbl.pack()
    output.pack(padx=(0, 10), pady=(0, 10))

    # Open gui
    print("You can minimize this window, but do not close!")
    gui.mainloop()
