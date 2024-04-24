import os

import pandas as pd

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the input directory relative to the script directory
input_dir = os.path.join(script_dir, '..' , "Data", "COMMENTARY_INTL_MATCH")

# Construct the path to the output directory relative to the script directory
output_dir = os.path.join(script_dir, '..', "Data", "Commentary")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all CSV files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        # Construct the input file path
        input_file = os.path.join(input_dir, filename)

        # Read the CSV file
        df = pd.read_csv(input_file)

        # Check if the 'Commentary' column exists
        if "Commentary" in df.columns:
            # Construct the output file path
            output_file = os.path.join(output_dir, filename)

            # Write the 'Commentary' column to the output file
            df["Commentary"].to_csv(output_file, index=False, header=False)
            print(f"Wrote commentary from {filename} to {output_file}")
        else:
            print(f"Warning: 'Commentary' column not found in {filename}")
