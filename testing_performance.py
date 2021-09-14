import numpy as np
import pandas as pd
from faker.providers.person.en import Provider
from random import randint
import timeit
import sqlite3
import os

# "Pandas vs SQLite3 Performance": the following performance tests were used in my Work Report (WKRPT) 200 submitted
# at the University of Waterloo


def random_names(name_type, size):
    """
    Generates ndarray of random names
    @param name_type: Options include 'first_names' or 'last_names'
    @param size: Number of names to generate
    @return: Returns ndarray of randomized names
    """
    names = getattr(Provider, name_type)
    return np.random.choice(names, size=size)


def random_ID(size):
    """
    Generates ndarray of random ID values
    @param size: Number of ID values to generate
    @return: Returns ndarray of randomized names
    """
    return np.random.choice(randint(0, 10000), size=size)


def gen_data_structures(conn):
    """
    Generates a dataframe containing first name, last name and ID. Converts said dataframe to an SQL database
    @param conn: connection to SQLite3 database
    @return: Returns dataframe containing first name, last name and ID
    """
    print("Starting Generation")
    size = 80000000  # 80 000 000, change to the number records you wish to test
    df_main = pd.DataFrame(columns=['First', 'Last', 'ID'])

    # Generates the random names and ID values
    col1 = random_names('first_names', size)
    col2 = random_names('last_names', size)
    col3 = random_ID(size)

    # Insert columns into dataframe
    df_main['First'] = col1
    df_main['Last'] = col2
    df_main['ID'] = col3

    # Convert dataframe to an SQLite database
    df_main.to_sql('Names', con=conn)
    print("Completed Generation")

    return df_main

def find_in_df(df):
    """
    Queries the dataframe for a specific ID value and returns matching records
    @param df: dataframe containing first name, last name and ID
    """
    # Query for a specific ID value
    x = df.loc[df['ID'] == 12]  # Change to the ID value you wish to query
    if not x.empty:
        print("found DF")
        print("Rows:", x.shape[0])

    return


def test_df_time(conn):
    """
    Queries the dataframe for a specific ID value and records runtime
    @param conn: connection to SQLite3 database
    """
    # Generate the datastructures (Pandas DF and SQLite3 DB)
    main_df = gen_data_structures(conn)

    # Records the runtime to query the dataframe
    start1 = timeit.default_timer()
    find_in_df(main_df)
    stop1 = timeit.default_timer()

    print('Pandas Time (s): ', stop1 - start1)
    del main_df

def find_in_sql(conn):
    """
    Queries the SQLite3 database for a specific ID value and returns matching records
    @param conn: connection to SQLite3 database
    """
    # Query for a specific ID value
    results_df = pd.read_sql("SELECT FIRST, LAST, ID FROM names WHERE ID=12", conn) # Change to the ID value you wish to query
    if not results_df.empty:
        print("found SQL")
        print("Rows:", results_df.shape[0])

    return


def test_sql_time(conn):
    """
    Queries the SQLite3 database for a specific ID value and records runtime
    @param conn: connection to SQLite3 database
    """

    # Records the runtime to query the dataframe
    start2 = timeit.default_timer()
    find_in_sql(conn)
    stop2 = timeit.default_timer()

    print('SQL Time (s): ', stop2 - start2)


if __name__ == '__main__':
    # connects to database object this object is what allows the execution of SQL statements through python
    conn = sqlite3.connect('names.db')
    cursor = conn.cursor()

    # test query times of pandas and SQLite3
    test_df_time(conn)
    test_sql_time(conn)

    # Get rid of the database file
    conn.commit()
    conn.close()
    os.remove('names.db')
