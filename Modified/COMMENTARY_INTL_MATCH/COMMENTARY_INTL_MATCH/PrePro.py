import os
import csv
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Get the current directory
current_dir = os.getcwd()

# Load English stopwords from NLTK
stop_words = set(stopwords.words('english'))

# Initialize a dictionary to store tokens and their frequencies
token_freq = {}

# Loop through all files in the directory
for file_name in os.listdir(current_dir):
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        # Open the CSV file for reading
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Process each row in the CSV file
            for row in csv_reader:
                # Tokenize the text
                word_tokens = word_tokenize(row[0])

                # Normalize tokens (remove punctuation and make lowercase)
                normalized_tokens = [token.lower().translate(str.maketrans('', '', string.punctuation)) for token in word_tokens]

                # Remove stopwords and remove digits from tokens
                filtered_tokens = [''.join(char for char in token if not char.isdigit()) for token in normalized_tokens if token not in stop_words]

                # Update token frequencies
                for token in filtered_tokens:
                    if token in token_freq:
                        token_freq[token].add(file_name)
                    else:
                        token_freq[token] = {file_name}

# Write tokens and their frequencies to the file 'tokens.txt'
with open('tokens.txt', 'w', newline='') as tokens_file:
    csv_writer = csv.writer(tokens_file, delimiter='\t')
    for token, files in sorted(token_freq.items()):
        csv_writer.writerow([token, len(files)])

print("Tokens and their frequencies have been written to 'tokens.txt'.")