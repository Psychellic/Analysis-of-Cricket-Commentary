import os
import pandas as pd

# Set the relative paths
data_dir = '../Data/COMMENTARY_INTL_MATCH/'
input_dir = '../Data/Input/'

# Create the input directory if it doesn't exist
os.makedirs(input_dir, exist_ok=True)

# Read the CSV file
csv_file = os.path.join(data_dir, '1244025_COMMENTARY.csv')
df = pd.read_csv(csv_file)

# Extract the desired columns
columns_to_extract = ['Commentary', 'Over_complete']
extracted_df = df[columns_to_extract]

# Write the extracted columns to a new CSV file
output_file = os.path.join(input_dir, 'input.csv')
extracted_df.to_csv(output_file, index=False)

print(f"Extracted columns written to: {output_file}")
