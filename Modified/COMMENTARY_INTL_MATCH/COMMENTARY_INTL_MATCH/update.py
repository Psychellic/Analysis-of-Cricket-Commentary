import os
import pandas as pd

# Get the current directory
current_dir = os.getcwd()

# Loop through all files in the directory
for file_name in os.listdir(current_dir):
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_name)

        # Select the 'Commentary' column
        df = df['Commentary']

        # Write the updated DataFrame back to the file
        df.to_csv(file_name, index=False, header=False)

        print(f"File {file_name} has been updated with only the 'Commentary' column.")
