"""
by Alec Davidson
"""
import csv, os, pandas as pd, re, shutil, sqlite3 as sl, sys


def Create_DB():
    """Check for the database files and CivGen folder in AppDatta and create
    anything missing.


    """
    try:
        local_path = sys._MEIPASS
    except:
        local_path = os.path.abspath(".")

    resources_local = os.path.join(local_path, "resources.db")
    civilizations_local = os.path.join(local_path, "civilizations.db")

    db_path = os.path.join(os.environ["APPDATA"], "CivGen")
    if not os.path.exists(db_path):
        os.mkdir(db_path)
    resources_path = os.path.join(db_path, "resources.db")
    civilizations_path = os.path.join(db_path, "civilizations.db")

    if not os.path.exists(resources_path):
        shutil.copy2(resources_local, resources_path)
    if not os.path.exists(civilizations_path):
        shutil.copy2(civilizations_local, civilizations_path)

    return


def Export_DB(database):
    """Export Databases by converting to CSV files in a Database Folder at the same
    location as the EXE.

    Establish path to database files, check for a local folder named after
    the database, and create filepath if missing. Read all the table names from
    sqlite_sequence and format. Iterate over each table, pull all data, convert
    to CSV and save in folder

    :param database:

    """
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    path_exists = os.path.exists(os.path.join(dir_path, database.replace(".db", "")))
    local_path = os.path.join(os.getcwd(), database.replace(".db", ""))
    try:
        os.mkdir(local_path)
    except:
        pass

    conn = sl.connect(db_path, isolation_level=None, detect_types=sl.PARSE_COLNAMES)
    db_all_tables = pd.read_sql_query("SELECT name FROM sqlite_sequence", conn)
    db_all_table_names = db_all_tables.values.tolist()
    for i in db_all_table_names:
        db_tables = pd.read_sql_query(f"SELECT * FROM {i[0]}", conn)
        db_tables.to_csv(
            f"{database.replace('.db','')}/{i[0]}.csv", sep="\t", index=False
        )
    conn.close()

    return f"Exported {database} to {local_path}."


def Import_DB(database, backup=True):
    """Backup current DB, delete it, and Convert CSVs to a new DB.

    Establish path to database files and local directory and confirm files to
    import are present.

    Backup current DB by creating a duplicate with .bak extension and then
    delete current db file

    Create a list of all the files in the Folder, iterating over each one, and
    grabbing the headers and the content.

    Format into SQL queries to create table in the db and insert into it.

    :param database:
    :param backup:  (Default value = True)

    """
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    csv_path = os.path.join(os.getcwd(), database.replace(".db", ""))
    if not os.path.exists(csv_path):
        return "Local Files Not Found."
    if backup == True:
        shutil.copy2(db_path, f"{db_path}.bak")
    os.remove(db_path)
    conn = sl.connect(db_path, isolation_level=None, detect_types=sl.PARSE_COLNAMES)
    cursor = conn.cursor()

    file_list = []
    for i in os.walk(csv_path):
        for j in i[2]:
            file_list.append(j)

    for k in file_list:
        with open(f"{csv_path}\{k}", "r") as table_file:
            count = 0
            table_name = k.replace(".csv", "")
            columns = ""
            rows = []
            for l in table_file:
                if count == 0:
                    columns = l.replace("\n", "").split("\t")
                    col_string = ""
                    for m in columns:
                        if col_string == "":
                            col_string += (
                                f"{m} INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT"
                            )
                        else:
                            col_string += f", {m} varchar(255) NOT NULL"
                    cursor.execute(f"create table {table_name} ({col_string})")
                else:
                    row = l.replace("\n", "").split("\t")
                    row_string = ""
                    rows.append(row)
                    col_string = ""
                    for m in columns:
                        if col_string == "":
                            col_string += f"{m}"
                        else:
                            col_string += f", {m}"
                    for n in row:
                        if row_string == "":
                            int(n)
                            row_string += n
                        else:
                            n = n.replace("'", "`")
                            row_string += f", '{n}'"
                    cursor.execute(
                        f"insert into {table_name} ({col_string}) VALUES ({row_string})"
                    )
                count += 1
    return "Import Complete."


def dbrollback(database):
    """Rollback DB by deleting active database and renaming backup file

    :param database:

    """
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    bak_path = db_path + ".bak"
    if not os.path.exists(bak_path):
        return "No backup file found."
    os.remove(db_path)
    shutil.copy2(bak_path, db_path)

    return f"{database} rolledback to previous saved version."
