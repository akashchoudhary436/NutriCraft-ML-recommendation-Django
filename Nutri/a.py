import pandas as pd

# Reading the DataFrame from the CSV file
df = pd.read_csv("final.csv")

# Deleting all rows except the first 15,000
df = df.head(15000)

# Saving the modified DataFrame back to the same CSV file
df.to_csv("final.csv", index=False)

# Printing a message to confirm the save
print("Modified DataFrame saved to final.csv")
