import pandas as pd 

from sqlalchemy import create_engine
from getpass import getpass 

def get_table_from_shelter(table_name):
    password = getpass()
    # prepare the engine 
    db_connection_string = 'mysql+pymysql://root:'+password+'@localhost/shelter'
    # connect to server 
    engine = create_engine(db_connection_string)
    # read table shelter_climate from the shelter database
    table_name = pd.read_sql_table(table_name, con=engine)
    # dispose of engine, closing all connections
    engine.dispose()
    return table_name