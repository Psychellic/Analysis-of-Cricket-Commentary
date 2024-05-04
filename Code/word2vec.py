import os
import csv
from gensim.models import Word2Vec

# Input and output directories
input_dir = "../Data/Commentary"
output_file = "../Data/commentary_word2vec.txt"

# Collect all the commentary text from the CSV files
commentary_text = []

for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                commentary = row[0]
                words = commentary.split()
                commentary_text.append(words)

# Train the Word2Vec model
model = Word2Vec(commentary_text, vector_size=100, window=5, min_count=1, workers=4)

# Save the word vectors to a file
with open(output_file, "w", encoding="utf-8") as file:
    for word in model.wv.key_to_index:
        vector = model.wv[word]
        file.write(f"{word} {' '.join(map(str, vector))}\n")
