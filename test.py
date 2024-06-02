import csv
from Code.vAnds import v_and_s

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

# Print the text_lines list
v_and_s(text_lines, 10)
