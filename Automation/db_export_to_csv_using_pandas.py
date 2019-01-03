''' This script is to export data from database to csv file using pandas dataframe'''

import datetime
import pandas as pd
import cx_oracle


# Setting data file path and name i.e 'sdis_outgoing_26-12-18.csv'
current_date = datetime.datetime.strftime(datetime.datetime.today(), "%d-%m-%y")
folder_loc = r'G:\data_exports'
file_name =  r'\sdis_outgoing' + '_' + str(current_date) + '.csv'
file_path = str(folder_loc) + str(file_name)

# Sql statement to retrive data
sql = 'select * from table_name;'

# database connection string
connection  =  cx_oracle.connect('username/password@sid')

# moving to panda data frame from database
data_frame = pd.read_sql(sql=sql, con=connection)

# writing data into csv file from data_frame
data_frame.to_csv(file_path, index = None, header=True)

# Close the database connection
connection.close()
