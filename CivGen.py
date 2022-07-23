"""
by Alec Davidson
"""
import argparse, manage_db, os, random, sqlite3 as sl, sys

db_path = os.path.join(os.environ["APPDATA"], "CivGen")
manage_db.Create_DB()

resourcesdb = os.path.join(db_path, "resources.db")  # Static DB
civdbdb = os.path.join(db_path, "civilizations.db")  # Dynamic DB

resources = sl.connect(resourcesdb)
civdb = sl.connect(civdbdb)


class Civilization:
    """A Class to represent a Civilization

    ...


    Attributes
    ----------
    id : int
            The id used to reference the Civilization in civilizations.db
    CIV_NAME : str, required
            The name of the Civilization
    KINGDOM : str, required
            The name of the Kingdom that the Civilization resides in
    COMMUNITY_SIZE : str
            The size or scale of the Civilization
    SPERM : str
            The main focus of the Civilization
    POLITICAL : str
            The Political Structure of the Civilization
    ECONOMIC : str
            The main Economic export of the Civilization
    MILITARY : str
            The type of Military the Civilization uses for protection
    SOCIAL : str
            The Social center of the Civilization
    RELIGION : str
            The primary Religious belief of the Civilization
    RACIAL_FEATURE_LIST : list
            A list of Features common in the races that live in the Civilization
    PROFICIENCIES_LIST : list
            A list of Proficiencies commonly found by anyone that lives in the
            Civilization
    SUBCLASSES_LIST : list
            A list of Classes/Subclasses that indiviuals of the Civilization may
    Methods
    -------
    READ_DB():
            Queries the DB for an entry in civilizations.db and returns the
            self.id.
    SAVE_DB():
            Save Civilization to the civilizations.db and return the id.
    UPDATE_DB():
            Update existing entry in civilizations.db and return the self.id.
    PRINT_CIV():
            Print the details of the Civilization with context and return 1.
    GET_DB_RANDOM(table):
            Grab a single entry at random from the given table in resources.db
            and return the entry.
    BUILD_RANDOM_LIST(table, total):
            Grab multiple, unique entries at random from the given table in
            resources.db and return two lists.
    GEN_CIV():
            Assigns random values to empty Attributes for the Civilization using
            the Kingdom and Civ Attributes as a seed and return self.
    BUILD_CIVILIZATION():
            Takes user assigned attributes and ensures all attributes are valid
            and non-empty for the Civilization and return self.id.
    """

    def __init__(
        self,
        id=-1,
        CIV_NAME="",
        KINGDOM="",
        COMMUNITY_SIZE="",
        SPERM="",
        POLITICAL="",
        ECONOMIC="",
        MILITARY="",
        SOCIAL="",
        RELIGION="",
        RACIAL_FEATURE_LIST=[],
        PROFICIENCIES_LIST=[],
        SUBCLASSES_LIST=[],
    ):
        """
        Constructs all the necessary attributes for the Civilization object.

        Parameters
        ----------
        id : int
                The id used to reference the Civilization in civilizations.db
        CIV_NAME : str, required
                The name of the Civilization
        KINGDOM : str, required
                The name of the Kingdom that the Civilization resides in
        COMMUNITY_SIZE : str
                The size or scale of the Civilization
        SPERM : str
                The main focus of the Civilization
        POLITICAL : str
                The Political Structure of the Civilization
        ECONOMIC : str
                The main Economic export of the Civilization
        MILITARY : str
                The type of Military the Civilization uses for protection
        SOCIAL : str
                The Social center of the Civilization
        RELIGION : str
                The primary Religious belief of the Civilization
        RACIAL_FEATURE_LIST : list
                A list of Features common in the races that live in the
                Civilization
        PROFICIENCIES_LIST : list
                A list of Proficiencies commonly found by anyone that lives in
                the Civilization
        SUBCLASSES_LIST : list
                A list of Classes/Subclasses that indiviuals of the Civilization
                may take
        """
        self.id = id
        self.CIV_NAME = CIV_NAME
        self.KINGDOM = KINGDOM
        self.COMMUNITY_SIZE = COMMUNITY_SIZE
        self.SPERM = SPERM
        self.POLITICAL = POLITICAL
        self.ECONOMIC = ECONOMIC
        self.MILITARY = MILITARY
        self.SOCIAL = SOCIAL
        self.RELIGION = RELIGION
        self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST
        self.PROFICIENCIES_LIST = PROFICIENCIES_LIST
        self.SUBCLASSES_LIST = SUBCLASSES_LIST

    def READ_DB(self):
        """Grabs an entry from civilization.db and updates the attributes of self.

        :param None:

        """
        sql = f"select * from civilizations where civ_name='{str(self.CIV_NAME)}' and kingdom='{str(self.KINGDOM)}';"
        with civdb:
            civ = civdb.execute(sql)

        for i in civ:
            self.id = i[0]
            self.CIV_NAME = i[1]
            self.KINGDOM = i[2]
            self.COMMUNITY_SIZE = i[3]
            self.SPERM = i[4]
            self.SOCIAL = i[5]
            self.POLITICAL = i[6]
            self.ECONOMIC = i[7]
            self.RELIGION = i[8]
            self.MILITARY = i[9]

            temp_RACIAL_FEATURE = i[10]
            temp_PROFICIENCIES = i[11]
            temp_SUBCLASSES = i[12]

            temp_RACIAL_FEATURE_LIST = []
            temp_PROFICIENCIES_LIST = []
            temp_SUBCLASSES_LIST = []

            with civdb:
                com = f"select * from racial_feature where id = {temp_RACIAL_FEATURE}"
                racial_feature = civdb.execute(com)

                for i in racial_feature:
                    for j in i:
                        temp_RACIAL_FEATURE_LIST.append(j)

                del temp_RACIAL_FEATURE_LIST[0]

                com = f"select * from proficiencies where id = {temp_PROFICIENCIES}"
                proficiencies = civdb.execute(com)
                for i in proficiencies:
                    for j in i:
                        temp_PROFICIENCIES_LIST.append(j)
                del temp_PROFICIENCIES_LIST[0]

                com = f"select * from subclasses where id = {temp_SUBCLASSES}"
                subclasses = civdb.execute(com)
                for i in subclasses:
                    for j in i:
                        temp_SUBCLASSES_LIST.append(j)
                del temp_SUBCLASSES_LIST[0]

            self.RACIAL_FEATURE_LIST = temp_RACIAL_FEATURE_LIST
            self.PROFICIENCIES_LIST = temp_PROFICIENCIES_LIST
            self.SUBCLASSES_LIST = temp_SUBCLASSES_LIST

        return self.id

    def SAVE_DB(self):
        """Saves the attributes of self to civilization.db.

        There are additional tables that store the contents of the lists.

        :param None:

        """
        sql_feature = "INSERT INTO racial_feature (feature1,feature2,feature3,feature4) values(?,?,?,?)"
        data_feature = [
            (
                self.RACIAL_FEATURE_LIST[0],
                self.RACIAL_FEATURE_LIST[1],
                self.RACIAL_FEATURE_LIST[2],
                self.RACIAL_FEATURE_LIST[3],
            )
        ]

        with civdb:
            civdb.executemany(sql_feature, data_feature)
            racial_feature = civdb.execute(
                "select seq from sqlite_sequence where name = 'racial_feature'"
            )
            racial_feature = [i[0] for i in racial_feature][0]

        sql_proficiencies = "INSERT INTO proficiencies (proficiency1,proficiency2,proficiency3,proficiency4) values(?,?,?,?)"
        data_proficiencies = [
            (
                self.PROFICIENCIES_LIST[0],
                self.PROFICIENCIES_LIST[1],
                self.PROFICIENCIES_LIST[2],
                self.PROFICIENCIES_LIST[3],
            )
        ]
        with civdb:
            civdb.executemany(sql_proficiencies, data_proficiencies)
            proficiencies = civdb.execute(
                "select seq from sqlite_sequence where name = 'proficiencies'"
            )
            proficiencies = [i[0] for i in proficiencies][0]

        sql_class = (
            "INSERT INTO subclasses (class1,subclass1,class2,subclass2) values(?,?,?,?)"
        )
        data_class = [
            (
                self.SUBCLASSES_LIST[0],
                self.SUBCLASSES_LIST[1],
                self.SUBCLASSES_LIST[2],
                self.SUBCLASSES_LIST[3],
            )
        ]
        with civdb:
            civdb.executemany(sql_class, data_class)
            subclasses = civdb.execute(
                "select seq from sqlite_sequence where name = 'subclasses'"
            )
            subclasses = [i[0] for i in subclasses][0]

        sql = f"INSERT INTO civilizations (civ_name,kingdom,community_size,sperm,social,political,economic,religion,military,racial_feature,proficiencies,subclasses) values(?,?,?,?,?,?,?,?,?,?,?,?)"
        data = [
            (
                str(self.CIV_NAME),
                str(self.KINGDOM),
                str(self.COMMUNITY_SIZE),
                str(self.SPERM),
                str(self.SOCIAL),
                str(self.POLITICAL),
                str(self.ECONOMIC),
                str(self.RELIGION),
                str(self.MILITARY),
                str(racial_feature),
                str(proficiencies),
                str(subclasses),
            )
        ]
        with civdb:
            civdb.executemany(sql, data)
            id = civdb.execute(
                "select seq from sqlite_sequence where name = 'civilizations'"
            )
            id = [i[0] for i in id][0]

        civdb.commit()
        return id

    def UPDATE_DB(self):
        """Update the civilization.db with the attributes of self.

        There are additional tables that store the contents of the lists.

        :param None:

        """

        sql_ids = f"select racial_feature,proficiencies,subclasses from civilizations where id='{int(self.id)}';"
        with civdb:
            idlist = []
            idlist_raw = civdb.execute(sql_ids)
            for i in idlist_raw:
                idlist.append(i)
        idlist = idlist[0]

        sql_feature = "UPDATE racial_feature SET feature1 = ? , feature2 = ? , feature3 = ? , feature4 = ? WHERE id = ?"
        data_feature = [
            (
                self.RACIAL_FEATURE_LIST[0],
                self.RACIAL_FEATURE_LIST[1],
                self.RACIAL_FEATURE_LIST[2],
                self.RACIAL_FEATURE_LIST[3],
                idlist[0],
            )
        ]
        with civdb:
            civdb.executemany(sql_feature, data_feature)

        sql_proficiencies = "UPDATE proficiencies SET proficiency1 = ? , proficiency2 = ? , proficiency3 = ? , proficiency4 = ? WHERE id = ?"
        data_proficiencies = [
            (
                self.PROFICIENCIES_LIST[0],
                self.PROFICIENCIES_LIST[1],
                self.PROFICIENCIES_LIST[2],
                self.PROFICIENCIES_LIST[3],
                idlist[1],
            )
        ]
        with civdb:
            civdb.executemany(sql_proficiencies, data_proficiencies)

        sql_class = "UPDATE subclasses SET class1 = ? , subclass1 = ? , class2 = ? , subclass2 = ? WHERE id = ?"
        data_class = [
            (
                self.SUBCLASSES_LIST[0],
                self.SUBCLASSES_LIST[1],
                self.SUBCLASSES_LIST[2],
                self.SUBCLASSES_LIST[3],
                idlist[2],
            )
        ]
        with civdb:
            civdb.executemany(sql_class, data_class)

        sql = f"UPDATE civilizations SET civ_name = ? , kingdom = ? , community_size = ? , sperm = ? , social = ? , political = ? , economic = ? , religion = ? , military = ? , racial_feature = ? , proficiencies  = ? , subclasses = ? WHERE id = ?"
        data = [
            (
                str(self.CIV_NAME),
                str(self.KINGDOM),
                str(self.COMMUNITY_SIZE),
                str(self.SPERM),
                str(self.SOCIAL),
                str(self.POLITICAL),
                str(self.ECONOMIC),
                str(self.RELIGION),
                str(self.MILITARY),
                idlist[0],
                idlist[1],
                idlist[2],
                self.id,
            )
        ]
        with civdb:
            civdb.executemany(sql, data)

        civdb.commit()
        return self.id

    def PRINT_CIV(self):
        """Prints out the attributes from self.

        :param None:

        """

        print("")
        print(
            f"{self.CIV_NAME} is a {self.COMMUNITY_SIZE} in {self.KINGDOM} with a large focus on its {self.SPERM}."
        )
        print(
            f"This {self.COMMUNITY_SIZE} is governed by {self.POLITICAL} where it's main export is {self.ECONOMIC}."
        )
        print(f"{self.MILITARY} oversees all conflict in {self.CIV_NAME}.")
        print(
            f"The locals of {self.CIV_NAME} spend their free time at one of its many {self.SOCIAL}."
        )
        print(
            f"Those who live here often find themselves {self.RELIGION}, but are tolerant of others beliefs."
        )
        print()
        print(
            f"Families that have lived here for generations tend to have one or more of the following features:"
        )
        for i in range(len(self.RACIAL_FEATURE_LIST)):
            print(f"\t* {self.RACIAL_FEATURE_LIST[i]}")
        print()
        print(
            f"Anyone who has spent a decent amount of time here, likely has honed one or more of the following skills:"
        )
        for i in range(len(self.PROFICIENCIES_LIST)):
            print(f"\t* {self.PROFICIENCIES_LIST[i]})")
        print()
        print(
            f"Adventurers who have found their start in {self.CIV_NAME} tend to become {self.SUBCLASSES_LIST[1]}s ({self.SUBCLASSES_LIST[0]}) or {self.SUBCLASSES_LIST[3]}s ({self.SUBCLASSES_LIST[2]})"
        )

        return

    def GET_DB_RANDOM(self, table):
        """Pulls random entries from resources.db

        :param table: The table from resources.db to search
        :type table: str, required

        """
        with resources:
            limit = resources.execute(f"select count() from {table};")
            limit = [i[0] for i in limit][0]
            id = random.randint(1, limit)

            try:
                entry = resources.execute(
                    f"select name,type,description from {table} where id = {id};"
                )
                temp = []
                for i in entry:
                    temp.append(i[0])
                    temp.append(i[1])
                    temp.append(i[2])
                entry = temp
            except:
                entry = resources.execute(f"select name from {table} where id = {id};")
                entry = [i[0] for i in entry][0]

            return entry

    def BUILD_RANDOM_LIST(self, table, total):
        """Use GET_DB_RANDOM to pull random entries and create a list of unique
        values.

        :param table: The table from resources.db to search
        :type table: str, required
        :param total: The number of entries to pull
        :type total: str, required

        """
        list = []
        list2 = []
        for i in range(total):  # Check for duplicates
            temp = self.GET_DB_RANDOM(table)
            for i in range(len(list)):
                if temp[1] == list2[i]:
                    while temp[1] in list2:
                        temp = self.GET_DB_RANDOM(table)

            list.append("")
            list2.append("")
            list[len(list) - 1] = temp[0], temp[2]
            list2[len(list) - 1] = temp[1]

        return list, list2

    def GEN_CIV(self):
        """Use the name of the Civilization as a seed for random.

        Set each string attributes using GET_DB_RANDOM. Set each list attributes
        using BUILD_RANDOM_LIST.


        """
        random.seed(str(self.CIV_NAME) + str(self.KINGDOM))
        self.COMMUNITY_SIZE = self.GET_DB_RANDOM(table="COMMUNITY_SIZE_LIST")
        self.SPERM = self.GET_DB_RANDOM(table="SPERM_LIST")
        self.SOCIAL = self.GET_DB_RANDOM(table="SOCIAL_LIST")
        self.POLITICAL = self.GET_DB_RANDOM(table="POLITICAL_LIST")
        self.ECONOMIC = self.GET_DB_RANDOM(table="ECONOMIC_LIST")
        self.RELIGION = self.GET_DB_RANDOM(table="RELIGION_LIST")
        self.MILITARY = self.GET_DB_RANDOM(table="MILITARY_LIST")

        RACIAL_FEATURE_LIST = []
        temp_RACIAL_FEATURE_LIST = self.BUILD_RANDOM_LIST(
            table="RACIAL_FEATURE", total=4
        )[0]

        for i in range(len(temp_RACIAL_FEATURE_LIST)):
            RACIAL_FEATURE_LIST.append(
                f"{temp_RACIAL_FEATURE_LIST[i][0]} ({temp_RACIAL_FEATURE_LIST[i][1]})"
            )
        self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST

        PROFICIENCIES_LIST = []
        temp_PROFICIENCIES_LIST = self.BUILD_RANDOM_LIST(
            table="PROFICIENCIES", total=4
        )[0]

        for i in range(len(temp_RACIAL_FEATURE_LIST)):
            PROFICIENCIES_LIST.append(
                f"{temp_PROFICIENCIES_LIST[i][0]} ({temp_PROFICIENCIES_LIST[i][1]})"
            )
        self.PROFICIENCIES_LIST = PROFICIENCIES_LIST

        SUBCLASSES_LIST = []
        temp_SUBCLASSES_LIST = self.BUILD_RANDOM_LIST(table="CLASS_LIST", total=2)
        SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[0][0][0])
        SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[1][0])
        SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[0][1][0])
        SUBCLASSES_LIST.append(temp_SUBCLASSES_LIST[1][1])
        self.SUBCLASSES_LIST = SUBCLASSES_LIST

        return self

    def BUILD_CIVILIZATION(self):
        """Takes user assigned attributes and ensures all attributes are valid and
        non-empty for the Civilization and return self.id.

        Store manually entered attributes to local variables.

        Create a second Civilization object (base) with the same CIV_NAME and
        KINGDOM execute GEN_CIV().

        Execute READ_DB() to pull values saved in the DB.

        If the Civilization is not in the DB, or the user indicated an attribute
        should be reset, overwrite the Attribute in self with the value from
        base.

        Save remaining manually entered values to the attributes of self.


        """
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

        base = Civilization(CIV_NAME=self.CIV_NAME, KINGDOM=self.KINGDOM)
        base = base.GEN_CIV()

        self.READ_DB()

        if self.id == -1 or COMMUNITY_SIZE == "RESET":
            self.COMMUNITY_SIZE = base.COMMUNITY_SIZE
        if self.id == -1 or SPERM == "RESET":
            self.SPERM = base.SPERM
        if self.id == -1 or SOCIAL == "RESET":
            self.SOCIAL = base.SOCIAL
        if self.id == -1 or POLITICAL == "RESET":
            self.POLITICAL = base.POLITICAL
        if self.id == -1 or ECONOMIC == "RESET":
            self.ECONOMIC = base.ECONOMIC
        if self.id == -1 or RELIGION == "RESET":
            self.RELIGION = base.RELIGION
        if self.id == -1 or MILITARY == "RESET":
            self.MILITARY = base.MILITARY
        if self.id == -1 or "RESET" in RACIAL_FEATURE_LIST:
            self.RACIAL_FEATURE_LIST = base.RACIAL_FEATURE_LIST
        if self.id == -1 or "RESET" in PROFICIENCIES_LIST:
            self.PROFICIENCIES_LIST = base.PROFICIENCIES_LIST
        if self.id == -1 or "RESET" in SUBCLASSES_LIST:
            self.SUBCLASSES_LIST = base.SUBCLASSES_LIST

        if COMMUNITY_SIZE != "RESET" and COMMUNITY_SIZE != "":
            self.COMMUNITY_SIZE = COMMUNITY_SIZE
        if SPERM != "RESET" and SPERM != "":
            self.SPERM = SPERM
        if SOCIAL != "RESET" and SOCIAL != "":
            self.SOCIAL = SOCIAL
        if POLITICAL != "RESET" and POLITICAL != "":
            self.POLITICAL = POLITICAL
        if ECONOMIC != "RESET" and ECONOMIC != "":
            self.ECONOMIC = ECONOMIC
        if RELIGION != "RESET" and RELIGION != "":
            self.RELIGION = RELIGION
        if MILITARY != "RESET" and MILITARY != "":
            self.MILITARY = MILITARY

        for i in range(
            len(self.RACIAL_FEATURE_LIST)
        ):  # For the lists, we overwrite in order.
            if RACIAL_FEATURE_LIST[i] == "RESET":  # If RESET was entered, use base
                RACIAL_FEATURE_LIST[i] = base.RACIAL_FEATURE_LIST[i]
            if RACIAL_FEATURE_LIST[i] == "":  # If nothing was entered, use self
                RACIAL_FEATURE_LIST[i] = self.RACIAL_FEATURE_LIST[i]
        self.RACIAL_FEATURE_LIST = RACIAL_FEATURE_LIST  # Both ifs will fail if something other than RESET is manually entered, and that value will be used

        for i in range(len(self.PROFICIENCIES_LIST)):
            if PROFICIENCIES_LIST[i] == "RESET":
                PROFICIENCIES_LIST[i] = base.PROFICIENCIES_LIST[i]
            if PROFICIENCIES_LIST[i] == "":
                PROFICIENCIES_LIST[i] = self.PROFICIENCIES_LIST[i]
        self.PROFICIENCIES_LIST = PROFICIENCIES_LIST

        for i in range(len(self.SUBCLASSES_LIST)):
            if SUBCLASSES_LIST[i] == "RESET":
                SUBCLASSES_LIST[i] = base.SUBCLASSES_LIST[i]
            if SUBCLASSES_LIST[i] == "":
                SUBCLASSES_LIST[i] = self.SUBCLASSES_LIST[i]
        self.SUBCLASSES_LIST = SUBCLASSES_LIST

        return self.id


def READ_LIST(kingdom):
    """Connect to civilizations.db and grab all civ_names, parsing through the
    returned data and stored for easier use.
    If a Kingdom has been provided, only search for civilizations under that
    Kingdom

    :param kingdom: A specific to pull entries from (default is None)
    :type kingdom: str, optional

    """
    if kingdom == "":
        sql = "select id,civ_name,kingdom from civilizations;"
    else:
        sql = f"select id,civ_name,kingdom from civilizations where kingdom like '{kingdom}';"
    with civdb:
        civ_list = civdb.execute(sql)

    civ_name_list = []
    for i in civ_list:
        civ_name_list.append(f"({i[0]}) {i[1]} in {i[2]}")

    return civ_name_list


def Import_DB(db):
    """In order to use the Import and Export functions from manage_db,
    I need to close the current connection to the DB and then reopen afterwards.

    :param db: The database that should be updated.
    :type db: str, required

    """
    global civdb, resources
    civdb.close()
    resources.close()
    result = manage_db.Import_DB(db)
    civdb = sl.connect(civdbdb)
    resources = sl.connect(resourcesdb)
    return result


def Export_DB(db):
    """In order to use the Import and Export functions from manage_db,
    I need to close the current connection to the DB and then reopen afterwards.

    :param db: The database that should be updated.
    :type db: str, required

    """
    global civdb, resources
    civdb.close()
    resources.close()
    result = manage_db.Export_DB(db)
    civdb = sl.connect(civdbdb)
    resources = sl.connect(resourcesdb)
    return result


def dbrollback(db):
    """In order to use the Rollback function from manage_db,
    I need to close the current connection to the DB and then reopen afterwards.

    :param db: The database that should be updated.
    :type db: str, required

    """
    global civdb, resources
    civdb.close()
    resources.close()
    result = manage_db.dbrollback(db)
    civdb = sl.connect(civdbdb)
    resources = sl.connect(resourcesdb)
    return result


if __name__ == "__main__":
    # Parse the CLI for manually entered entities
    parser = (
        argparse.ArgumentParser()
    )  # formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-r",
        "--read",
        action="store_true",
        help="If set, prints out existing Civs and enables Generation Looping",
        default=False,
    )
    parser.add_argument(
        "-c", "--civ_name", help="Set Civilization Name. *REQUIRED*", default="NULL"
    )
    parser.add_argument(
        "-k", "--kingdom", help="Set Kingdom Name. *REQUIRED*", default="NULL"
    )
    parser.add_argument("--community_size", help="Set Community Size", default="")
    parser.add_argument("--sperm", help="Set Focus", default="")
    parser.add_argument("--social", help="Set Social", default="")
    parser.add_argument("--political", help="Set Political", default="")
    parser.add_argument("--economic", help="Set Economy", default="")
    parser.add_argument("--religion", help="Set Religion", default="")
    parser.add_argument("--military", help="Set Military", default="")
    parser.add_argument(
        "--racial_feature_list", action="append", help="Add Racial Feature", default=[]
    )
    parser.add_argument(
        "--proficiencies_list", action="append", help="Add Proficiency", default=[]
    )
    parser.add_argument(
        "--subclasses_list", action="append", help="Add SubClass", default=[]
    )
    args = parser.parse_args()

    # Append nothing to the lists in order to match desired length
    while len(args.racial_feature_list) < 4:
        args.racial_feature_list.append("")
    while len(args.proficiencies_list) < 4:
        args.proficiencies_list.append("")
    while len(args.subclasses_list) < 4:
        args.subclasses_list.append("")

    # If args.read==True, display saved Civs and do nothing, else generate
    if args.read:
        print(READ_LIST(args.kingdom))
    else:
        # Create object with CLI Arguments and Build
        civ = Civilization(
            CIV_NAME=args.civ_name,
            KINGDOM=args.kingdom,
            COMMUNITY_SIZE=args.community_size,
            SPERM=args.sperm,
            POLITICAL=args.social,
            ECONOMIC=args.political,
            MILITARY=args.economic,
            SOCIAL=args.religion,
            RELIGION=args.military,
            RACIAL_FEATURE_LIST=args.racial_feature_list,
            PROFICIENCIES_LIST=args.proficiencies_list,
            SUBCLASSES_LIST=args.subclasses_list,
        )
        id = civ.BUILD_CIVILIZATION()

        # Print out results and ask to save/update
        civ.PRINT_CIV()
        print("")
        print("Do you want to save this Civilization? (Y\\N)")
        save = input("> ")
        if save.lower() == "y":
            if id == -1:
                civ.SAVE_DB()
            else:
                civ.UPDATE_DB()
