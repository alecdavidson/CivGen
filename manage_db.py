# Import Modules
import csv, os, pandas as pd, re, shutil, sqlite3 as sl, sys

##functions
# Check for the database files and CivGen folder in AppDatta
# Create anything missing
def Create_DB():
    # Temp folder if EXE, else point to current locaiton
    try:
        local_path = sys._MEIPASS
    except:
        local_path = os.path.abspath(".")

    # Establish local db files
    resources_local = os.path.join(local_path, "resources.db")
    civilizations_local = os.path.join(local_path, "civilizations.db")

    # Establish path to permanent folder
    db_path = os.path.join(os.environ["APPDATA"], "CivGen")
    # Create fodler if missing
    if not os.path.exists(db_path):
        os.mkdir(db_path)
    # Establish path to final db location
    resources_path = os.path.join(db_path, "resources.db")
    civilizations_path = os.path.join(db_path, "civilizations.db")

    # If Database files are missing, copy from local to final path
    if not os.path.exists(resources_path):
        shutil.copy2(resources_local, resources_path)
    if not os.path.exists(civilizations_path):
        shutil.copy2(civilizations_local, civilizations_path)

    return 1


# Export Databases by converting to CSV files in a Database Folder at the same location as the EXE
def Export_DB(database):
    # Establish path to database files
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    # Check for a local folder named after the database, create it if missing
    path_exists = os.path.exists(os.path.join(dir_path, database.replace(".db", "")))
    local_path = os.path.join(os.getcwd(), database.replace(".db", ""))
    try:
        os.mkdir(local_path)
    except:
        pass

    # Connect to Database
    conn = sl.connect(db_path, isolation_level=None, detect_types=sl.PARSE_COLNAMES)
    # Read all the table names from sqlite_sequence an dformat
    db_all_tables = pd.read_sql_query("SELECT name FROM sqlite_sequence", conn)
    db_all_table_names = db_all_tables.values.tolist()
    # Iterate over each table, pull all data, convert to CSV and save in folder
    for i in db_all_table_names:
        db_tables = pd.read_sql_query(f"SELECT * FROM {i[0]}", conn)
        db_tables.to_csv(
            f"{database.replace('.db','')}/{i[0]}.csv", sep="\t", index=False
        )
    # Close connection
    conn.close()

    return f"Exported {database} to {local_path}."


# Backup current DB, delete it, and Convert CSVs to a new DB
def Import_DB(database, backup=True):
    # Establish path to database files
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    # Establish path to local directory
    csv_path = os.path.join(os.getcwd(), database.replace(".db", ""))
    # Check if there are files to import
    if not os.path.exists(csv_path):
        return "Local Files Not Found."
    # Backup current DB by creating a duplicate with .bak extension
    if backup == True:
        shutil.copy2(db_path, f"{db_path}.bak")
    # Delete current db file
    os.remove(db_path)
    # Connect to Database
    conn = sl.connect(db_path, isolation_level=None, detect_types=sl.PARSE_COLNAMES)
    cursor = conn.cursor()

    # Create a list of all the files in the Folder
    file_list = []
    for i in os.walk(csv_path):
        for j in i[2]:
            file_list.append(j)

    # Iterate over each one, grabbing the headers and the content
    # Format into SQL queries to create table in the db and insert into it.
    for k in file_list:
        with open(f"{csv_path}\{k}", "r") as table_file:
            count = 0
            table_name = k.replace(".csv", "")
            columns = ""
            rows = []
            for l in table_file:
                # The first row contains the headers needed to create the table
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
                    # print(f"create table {table_name} ({col_string})")
                    cursor.execute(f"create table {table_name} ({col_string})")
                # The remaining rows will use the headers from before to format the insert command
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
                    # print(f"insert into {table_name} ({col_string}) VALUES ({row_string})")
                    cursor.execute(
                        f"insert into {table_name} ({col_string}) VALUES ({row_string})"
                    )
                count += 1
    return "Import Complete."


# Rollback DB by deleting active database and renaming backup file
def dbrollback(database):
    # Establish path to database files
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    bak_path = db_path + ".bak"
    # Check that a backup exists before deleting
    if not os.path.exists(bak_path):
        return "No backup file found."
    # Delete current DB and rename Backup
    os.remove(db_path)
    shutil.copy2(bak_path, db_path)

    return f"{database} rolledback to previous saved version."


if __name__ == "__main__":
    pass
