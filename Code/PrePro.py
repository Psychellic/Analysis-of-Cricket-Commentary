import os
import re
from collections import Counter

import nltk
import pandas as pd
from nltk.corpus import stopwords

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the input directory relative to the script directory
input_dir = os.path.join(script_dir, "..", "Data", "Commentary")

# Construct the path to the output directory relative to the script directory
output_dir = os.path.join(script_dir, "..", "Data")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for word frequencies and a dictionary to store file information
word_freq = Counter()
word_files = {}

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)

    # Read the file content
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Normalize the text
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Update word frequencies and file information
    word_freq.update(filtered_tokens)
    for word in set(filtered_tokens):
        if word not in word_files:
            word_files[word] = [filename]
        else:
            word_files[word].append(filename)

# Create a list of tuples with (word, frequency, files)
data = [
    (word, freq, '{}'.format(', '.join(word_files[word])))
    for word, freq in word_freq.items()
]

# Convert the list of tuples to a pandas DataFrame
df = pd.DataFrame(data, columns=["Word", "Frequency", "Files"])

# Sort the DataFrame by frequency in descending order
df = df.sort_values(by="Frequency", ascending=False)

# Save the DataFrame to a CSV file
output_file = os.path.join(output_dir, "FrequencyWithFiles.csv")
df.to_csv(output_file, index=False)
