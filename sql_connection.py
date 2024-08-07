# This is a script for the MySQL connection. The name of the script is: sql_connection
# It can be called by writting: from sql_connection import connection_string
schema = 'sql_database_wbs_ds_29_project'
host = '127.0.0.1'
user = 'root'
MSQLP = 'MySQL_Password_comes_here' # Password
port = 3306
connection_string = f'mysql+pymysql://{user}:{MSQLP}@{host}:{port}/{schema}'