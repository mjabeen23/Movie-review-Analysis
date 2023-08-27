import os
import csv

# Define the paths to the pos and neg subfolders in train and test folders each
pos_folder = 'path-to-pos-folder'
neg_folder = 'path-to-neg-folder'

# Define the output CSV file path
output_csv = 'path-to-csv-folder.csv'

# Create or open the CSV file for writing
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Rating', 'Comment'])  # Write header row

    # Process the train folder
    for folder in [pos_folder, neg_folder]:
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder, filename)
                id_rating = filename.replace('.txt', '').split('_')
                if len(id_rating) == 2:
                    movie_id, rating = id_rating
                    with open(file_path, 'r', encoding='utf-8') as file:
                        comment = file.read().strip()
                        csv_writer.writerow([movie_id, rating, comment])

print("CSV file has been generated.")
