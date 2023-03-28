'''
This Python script reads the data from usage-data and creates a new csv
file called "usage-data-new-dates.csv" which replaces the date format
from dd/mm/yyyy to yyyy-mm-dd. This is so it follows the SQL DATE format
.
'''

import pandas as pd

df = pd.read_csv('./csv-files/usage-data.csv')

df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')

df.to_csv('usage-data-new-dates.csv', index=False)