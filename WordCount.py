import collections
import csv
import os

input_directory = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2')

input_file_name = 'combined_text.txt'  

input_file_path = os.path.join(input_directory, input_file_name)
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

word_counts = collections.Counter(words)

top_30_words = word_counts.most_common(30)

output_directory = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2')
output_file_path = os.path.join(output_directory, 'top_30_words.csv')

with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count']) 
    writer.writerows(top_30_words)  

print('Top 30 most common words and their counts saved to', output_file_path)
