"""
by Alec Davidson
"""
import CivGen, os, sys, tkinter as tk
import ctypes
from CivGen import Civilization, READ_LIST
from functools import partial
from tkinter import *
from tkinter import Canvas, Menu, scrolledtext, ttk
from PIL import Image, ImageTk

ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Auto Scaling

# Close Splash Screen
try:
    import pyi_splash

    pyi_splash.close()
except:
    pass

civ = ""
added_input = False

try:
    local_path = sys._MEIPASS
except:
    local_path = os.path.abspath(".")


def read():
    """Read entries from civilizations.db using funcitons from CivGen"""
    global kingdom

    civ_list = READ_LIST(kingdom.get())

    print(civ_list)
    output.insert(END, "City in Kingdom\n------------------------------\n")
    for i in civ_list:
        output.insert(END, "\u25C6", "List")
        output.insert(END, f" {i}\n", "List")
    output.insert(END, "_____________________________________________\n\n")
    output.see(END)

    return


def save():
    """Save latest generated Civilization to civilizations.db using funcitons
    from CivGen


    """
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

    return


def generate():
    """Create Civilization object and execute BUILD_CIVILIZATION()"""
    global civ

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

    civ.PRINT_CIV()

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

    return


def dbimport(db):
    """Convert CSVs to DB

    :param db:

    """
    result = CivGen.Import_DB(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


def dbexport(db):
    """Export DB content into CSVs

    :param db:

    """
    result = CivGen.Export_DB(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


def dbrollback(db):
    """Rollback DB to previous version

    :param db:

    """
    result = CivGen.dbrollback(db)
    output.insert(END, f"\n-- {result} --\n")
    return 1


def about(about_type):
    """Create a new window with information

    :param about_type:

    """

    about_window = Tk()
    about_window.title("Civilization Generator by Alec Davidson")
    about_window.geometry("750x650")
    about_window["background"] = "#999999"
    about_window.iconbitmap(os.path.join(local_path, "d20.ico"))

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

    textbox = Text(about_window)
    textbox.insert(END, data)
    textbox.pack(expand=True, fill=BOTH)

    return


def add_input():
    """Allow for User input for other details"""
    global added_input

    if added_input == False:
        community_sizelbl.pack(anchor="w", padx=25)
        community_size.pack(anchor="w", padx=25, fill=X)
        spermlbl.pack(anchor="w", padx=25)
        sperm.pack(anchor="w", padx=25, fill=X)
        sociallbl.pack(anchor="w", padx=25)
        social.pack(anchor="w", padx=25, fill=X)
        politicallbl.pack(anchor="w", padx=25)
        political.pack(anchor="w", padx=25, fill=X)
        economiclbl.pack(anchor="w", padx=25)
        economic.pack(anchor="w", padx=25, fill=X)
        religionlbl.pack(anchor="w", padx=25)
        religion.pack(anchor="w", padx=25, fill=X)
        militarylbl.pack(anchor="w", padx=25)
        military.pack(anchor="w", padx=25, fill=X)

        racial_feature_listlbl.pack(anchor="w", padx=25)
        racial_feature_list.pack(anchor="w", padx=25, fill=X)
        proficiencies_listlbl.pack(anchor="w", padx=25)
        proficiencies_list.pack(anchor="w", padx=25, fill=X)
        subclasses_listlbl.pack(anchor="w", padx=25)
        subclasses_list.pack(anchor="w", padx=25, fill=X)

        buffer.pack_forget()
        d20canvas.pack_forget()

        buffer.pack(padx=30)

        added_input = True

        enable_scroll("On")
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

        buffer.pack_forget()

        buffer.pack(padx=30)
        d20canvas.pack(fill=BOTH, expand=True)

        added_input = False

        leftcanvas.unbind_all("<MouseWheel>")
        leftcanvas.unbind("<Enter>")
        leftcanvas.unbind("<Leave>")
    return


def enable_scroll(v):
    """Toggle the ability to Scroll the Left Frame

    :param v:

    """
    leftcanvas.bind_all(
        "<MouseWheel>",
        lambda e: leftcanvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
    )

    leftcanvas.bind(
        "<Enter>",
        lambda _: leftcanvas.bind_all(
            "<MouseWheel>",
            lambda e: leftcanvas.yview_scroll(int(-1 * (e.delta / 120)), "units"),
        ),
    )
    leftcanvas.bind("<Leave>", lambda _: leftcanvas.unbind_all("<MouseWheel>"))
    return 1


if __name__ == "__main__":
    # Create gui and Label it
    gui = Tk()
    gui.title("Civilization Generator by Alec Davidson")
    gui.geometry("950x1000")
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
    im_menu.add_separator()
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
    leftframe = ttk.Frame(gui)
    leftcanvas = Canvas(
        leftframe, background="#999999", highlightthickness=0, width=500, height=1000
    )
    leftcanvas.itemconfigure("leftframe")
    scrollbar = ttk.Scrollbar(leftframe, orient="vertical", command=leftcanvas.yview)
    scrollable_frame = Frame(leftcanvas, width=500, height=1000)
    scrollable_frame["background"] = "#999999"
    scrollable_frame.bind(
        "<Configure>",
        lambda e: leftcanvas.configure(scrollregion=leftcanvas.bbox("all")),
    )
    leftcanvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    leftcanvas.configure(yscrollcommand=scrollbar.set)

    rightframe = ttk.Frame(gui)
    rightcanvas = Canvas(
        leftframe, background="#999999", highlightthickness=0, width=450, height=1000
    )
    rightcanvas.itemconfigure("rightframe")
    rightcanvas.create_window((0, 0), anchor="ne")

    # Create Title and Output
    Title = tk.Label(
        scrollable_frame,
        text="Civilization Generator",
        bg="#999999",
        font=("Calibri 18 bold underline"),
        width=31,
    )
    outputlbl = tk.Label(rightcanvas, text="Results:", bg="#999999")
    output = scrolledtext.ScrolledText(
        rightcanvas,
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
    d20canvas = Canvas(scrollable_frame, bg="#999999", highlightthickness=0)
    d20canvas.create_image(250, 300, anchor="s", image=d20pic)
    # d20lbl = Label(scrollable_frame, image=d20pic)

    # Create User Input Fields and Global Variables
    kingdomlbl = tk.Label(
        scrollable_frame, text="What is the name of your Kingdom?", bg="#999999"
    )
    kingdom = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    kingdom.insert(0, "Kingdom")
    civ_namelbl = tk.Label(
        scrollable_frame, text="What is the name of your Civilization?", bg="#999999"
    )
    civ_name = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    civ_name.insert(0, "Civ")

    community_sizelbl = tk.Label(
        scrollable_frame,
        text="How would you describe the Size of your Civilization?",
        bg="#999999",
    )
    community_size = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    spermlbl = tk.Label(
        scrollable_frame,
        text="What is the main Focus of your Civilization?",
        bg="#999999",
    )
    sperm = tk.Entry(scrollable_frame, relief=tk.SUNKEN)

    sociallbl = tk.Label(
        scrollable_frame,
        text="What is the key Social aspect of your Civilization?",
        bg="#999999",
    )
    social = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    politicallbl = tk.Label(
        scrollable_frame,
        text="What is the Policial structure of your Civilization?",
        bg="#999999",
    )
    political = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    economiclbl = tk.Label(
        scrollable_frame,
        text="What is the primary Export of your Civilization?",
        bg="#999999",
    )
    economic = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    religionlbl = tk.Label(
        scrollable_frame,
        text="What is the nature of your Civilizations Religion?",
        bg="#999999",
    )
    religion = tk.Entry(scrollable_frame, relief=tk.SUNKEN)
    militarylbl = tk.Label(
        scrollable_frame,
        text="What enforces the law in your Civilization?",
        bg="#999999",
    )
    military = tk.Entry(scrollable_frame, relief=tk.SUNKEN)

    racial_feature_listlbl = tk.Label(
        scrollable_frame,
        text="What are features of the families in your Civilization? (Limit 4)",
        bg="#999999",
    )
    racial_feature_list = tk.Text(
        scrollable_frame, width=40, height=4, relief=tk.SUNKEN
    )
    proficiencies_listlbl = tk.Label(
        scrollable_frame,
        text="What skills are honed by the people of your Civilization? (Limit 4)",
        bg="#999999",
    )
    proficiencies_list = tk.Text(scrollable_frame, width=40, height=4, relief=tk.SUNKEN)
    subclasses_listlbl = tk.Label(
        scrollable_frame,
        text="What type of Adventurer got their start in your Civilization?\n(Limit 2, alternate lines for 'Class' and 'Subclass')",
        bg="#999999",
        justify=LEFT,
    )
    subclasses_list = tk.Text(scrollable_frame, width=40, height=4, relief=tk.SUNKEN)

    buffer = tk.Label(
        scrollable_frame,
        text="",
        bg="#999999",
        justify=LEFT,
    )

    # Create Buttons
    generate = tk.Button(
        scrollable_frame,
        relief=tk.RAISED,
        text="Generate Civilization",
        command=generate,
    )
    read = tk.Button(
        scrollable_frame,
        relief=tk.RAISED,
        text="Print Saved Civilizations",
        command=read,
    )
    save = tk.Button(
        scrollable_frame,
        relief=tk.RAISED,
        text="Save Latest Civilization",
        command=save,
    )
    add_inputbtn = tk.Button(
        scrollable_frame,
        relief=tk.RAISED,
        text="Manually Enter Details",
        command=add_input,
    )

    # Pack Fields
    Title.pack()
    kingdomlbl.pack(padx=25)
    kingdom.pack(padx=25, fill=X)
    civ_namelbl.pack(padx=25)
    civ_name.pack(padx=25, fill=X)

    generate.pack(fill=X, pady=(5, 2), padx=70)
    save.pack(fill=X, padx=70, pady=2)
    read.pack(fill=X, padx=70, pady=2)
    add_inputbtn.pack(fill=X, padx=70, pady=2)

    buffer.pack(padx=30)
    d20canvas.pack(fill=BOTH, expand=True)

    outputlbl.pack()
    output.pack(padx=(0, 10), pady=(0, 10))

    rightcanvas.pack(side="right", anchor=NE)
    rightcanvas.pack_propagate(0)

    leftframe.pack()
    leftcanvas.pack(side="left", anchor=NW, expand=True)

    scrollbar.pack(side="right", fill="y")

    # Open gui
    print("You can minimize this window, but do not close!")
    gui.mainloop()
