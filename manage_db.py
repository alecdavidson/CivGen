import csv, os, pandas as pd, re, shutil, sqlite3 as sl, sys


def Create_DB():
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

    shutil.copy2(resources_local, resources_path)
    shutil.copy2(civilizations_local, civilizations_path)

    return 1


def Export_DB(database):
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    path_exists = os.path.exists(os.path.join(dir_path, database.replace(".db", "")))
    try:
        os.mkdir(f"{os.getcwd()}\{database.replace('.db','')}")
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

    return 1


def Import_DB(database, backup=True):
    dir_path = os.path.join(os.environ["APPDATA"], "CivGen")
    db_path = os.path.join(dir_path, database)
    if backup == True:
        shutil.copy2(db_path, f"{db_path}.bak")
    os.remove(db_path)
    csv_path = os.path.join(os.getcwd(), database.replace(".db", ""))
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
                    # print(f"create table {table_name} ({col_string})")
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
                        try:
                            int(n)
                            row_string += n
                        except:
                            n = n.replace("'", "`")
                            row_string += f", '{n}'"
                    # print(f"insert into {table_name} ({col_string}) VALUES ({row_string})")
                    cursor.execute(
                        f"insert into {table_name} ({col_string}) VALUES ({row_string})"
                    )
                count += 1
    return 1


if __name__ == "__main__":
    Create_DB()
