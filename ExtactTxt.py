import pandas as pd
import os

csv_directory = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2')

all_texts = []

for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(file_path)
        concatenated_text = df.apply(lambda row: ' '.join([str(val) for val in row]), axis=1)
        all_texts.extend(concatenated_text.tolist())

concatenated_text = '\n'.join(all_texts)

allTxtFilePath = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2', 'combined_text.txt')

with open(allTxtFilePath, 'w') as file:
    file.write(concatenated_text)

print('Text extracted from all CSV files and saved to', allTxtFilePath)
