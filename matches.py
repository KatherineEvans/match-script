from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import pandas as pd

#path to your CSV file
file_path = 'sample_data.csv'
#decode and store CSV file
df = pd.read_csv(file_path, encoding='latin1')

#create a new column to store matched percentages
df['Match Percentage'] = None

#loop through data table and run fuzzywuzzy comparison
for index, row in df.iterrows():
    match_value = fuzz.token_sort_ratio(row['SKU Short Description (SAP)'], row['New SKU Marketing Name'])
    #add match percentage to new column
    df.at[index, 'Match Percentage'] = match_value

#create/shovel data into new CSV file
matched_file = 'matched_data.csv'  # Specify your new file path here
df.to_csv(matched_file, index=False)