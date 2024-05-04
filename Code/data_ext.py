import csv
import os

# Input and output directories
input_dir = "../Data/COMMENTARY_INTL_MATCH"
output_dir = "../Data/Commentary"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Process each file in the input directory

for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.csv")

        with open(input_file, "r", encoding="utf-8") as file_in, open(
            output_file, "w", newline="", encoding="utf-8"
        ) as file_out:
            reader = csv.DictReader(file_in)
            fieldnames = ["Commentary", "Runs", "Wickets"]
            writer = csv.DictWriter(file_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                commentary = row["Commentary"]
                total_runs = row["Total_Runs_on_delivery"]
                play_type_desc = row["PlayType_description"]

                # Check if the word "out" is present in the "PlayType_description" column
                wickets = "1" if "out" in play_type_desc.lower() else "0"

                writer.writerow(
                    {
                        "Commentary": commentary,
                        "Runs": total_runs,
                        "Wickets": wickets,
                    }
                )
