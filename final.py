import os
import csv
import pickle
from Code.vAnds import v_and_s
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load the trained model
with open("Code/Pickles/trained_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the input data
input_data = pd.read_csv("Data/Input/input.csv")

# Get the commentary and over completion data
commentary = input_data["Commentary"].astype(str).values
over_complete = input_data["Over_complete"].values

# Tokenize the commentary
tokenizer = Tokenizer()
tokenizer.fit_on_texts(commentary)
sequences = tokenizer.texts_to_sequences(commentary)

# Pad the sequences
max_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_length)

# Initialize variables
over_num = 1
total_runs = 0
total_wickets = 0
over_stats = {}

# Process each commentary line
for padded_sequence, complete in zip(padded_sequences, over_complete):
    # Reshape the padded sequence to match the model's input shape
    padded_sequence = padded_sequence.reshape(1, max_length)

    # Predict runs and wickets for the commentary line
    prediction = model.predict(padded_sequence)
    predicted_runs = int(round(prediction[0][0]))
    predicted_wickets = int(round(prediction[0][1]))

    # Update total runs and wickets
    total_runs += predicted_runs
    total_wickets += predicted_wickets

    # Check if the over is complete
    if complete:
        over_stats[over_num] = [total_runs, total_wickets]
        over_num += 1
        total_runs = 0
        total_wickets = 0

# Sort overs by runs
sorted_overs_runs = sorted(over_stats.items(), key=lambda x: x[1][0], reverse=True)

# Print the top 10 overs with highest runs
print("\nTop 10 Overs with Highest Runs:")
for i, (over, stats) in enumerate(sorted_overs_runs[:10], start=1):
    print(f"{i}. Over {over}: Runs = {stats[0]}, Wickets = {stats[1]}")

# Sort overs by wickets
sorted_overs_wickets = sorted(over_stats.items(), key=lambda x: x[1][1], reverse=True)

# Print the top 10 overs with highest wickets
print("\nTop 10 Overs with Highest Wickets:")
for i, (over, stats) in enumerate(sorted_overs_wickets[:10], start=1):
    print(f"{i}. Over {over}: Runs = {stats[0]}, Wickets = {stats[1]}")

text_lines = []
current_over = []

with open('Data/Input/input.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        commentary = row[0]
        over_complete = row[1].lower() == 'true'

        current_over.append(commentary)

        if over_complete:
            text_lines.append(current_over)
            current_over = []

# If there are any remaining balls in the current over, add it to the text_lines list
if current_over:
    text_lines.append(current_over)

v_and_s(text_lines, 10)
