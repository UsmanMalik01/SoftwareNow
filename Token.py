from transformers import AutoTokenizer
from collections import Counter
import os

def count_unique_tokens(text_file_path, model_name_or_path, top_n=30):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    # Read the text from the .txt file
    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using the tokenizer
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top n most common tokens
    top_n_tokens = token_counts.most_common(top_n)

    return top_n_tokens

# Example usage:
text_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2', 'combine.txt')
model_name_or_path = "bert-base-uncased"  # Replace with the name or path of the model you want to use
top_30_tokens = count_unique_tokens(text_file_path, model_name_or_path)

print('Top 30 most common tokens:', top_30_tokens)
