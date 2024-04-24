import os

import pandas as pd
from nltk.stem import WordNetLemmatizer

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the input file relative to the script directory
input_file = os.path.join(script_dir, "..", "Data", "FrequencyWithFiles.csv")

# Construct the path to the output directory relative to the script directory
output_dir = os.path.join(script_dir, "..", "Data")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Read the input file
df = pd.read_csv(input_file)

# Apply lemmatization to each word in the 'Word' column
df["Word"] = df["Word"].astype(str).apply(lemmatizer.lemmatize)

# Group the DataFrame by the lemmatized 'Word' and sum the 'Frequency'
lemma_freq = df.groupby("Word")["Frequency"].sum().reset_index()

# Rename the columns appropriately
lemma_freq.columns = ["Lemma", "Frequency"]

# Sort the DataFrame by 'Frequency' in descending order
lemma_freq = lemma_freq.sort_values(by="Frequency", ascending=False)

# Save the DataFrame to a CSV file in the specified output directory
output_file = os.path.join(output_dir, "Lemma.csv")
lemma_freq.to_csv(output_file, index=False)
