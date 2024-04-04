import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('final.csv')

# Store the number of rows before cleaning
rows_before = len(df)

# Drop rows with NaN or blank cells in specified columns
columns_to_check = ['Calories', 'FatContent', 'CholesterolContent', 'SodiumContent', 
                    'CarbohydrateContent', 'FiberContent', 'SugarContent', 'ProteinContent']
df_cleaned = df.dropna(subset=columns_to_check, how='any')

# Calculate the number of rows deleted
rows_deleted = rows_before - len(df_cleaned)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('finalss.csv', index=False)

# Print confirmation message and number of rows deleted
print("New CSV file 'cleaned_final.csv' has been created with rows containing NaN or blank cells removed.")
print(f"Number of rows deleted: {rows_deleted}")
