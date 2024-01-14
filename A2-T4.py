import os
import spacy
from spacy.tokens import Doc
import torch
from transformers import BertTokenizer, BertModel

# Load spaCy models
nlp_sci_sm = spacy.load('en_core_sci_sm')
nlp_bc5cdr_md = spacy.load('en_ner_bc5cdr_md')

# Load BioBERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('monologg/biobert_v1.1_pubmed')
model = BertModel.from_pretrained('monologg/biobert_v1.1_pubmed')

def load_text_file(file_path):
    """
    Load text from a file.

    Args:
    - file_path (str): Path to the text file.

    Returns:
    - str: Contents of the text file.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    else:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

def extract_entities_spacy(text, nlp_model, entity_type):
    doc = nlp_model(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_type]
    return entities

def extract_entities_biobert(text, tokenizer, model):
    inputs = tokenizer.encode_plus(text, return_tensors='pt', add_special_tokens=True)
    outputs = model(**inputs)
    last_hidden_states = outputs.last_hidden_state
    # Process the last hidden state to extract entities
    # ...
    return entities

def main():
    # Define the file path
    text_file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'assignment-2', 'combined_text.txt')

    # Load the text file
    text = load_text_file(text_file_path)

    # Extract entities using spaCy models
    diseases_sci_sm = extract_entities_spacy(text, nlp_sci_sm, 'DISEASE')
    drugs_sci_sm = extract_entities_spacy(text, nlp_sci_sm, 'CHEMICAL')
    diseases_bc5cdr_md = extract_entities_spacy(text, nlp_bc5cdr_md, 'DISEASE')
    drugs_bc5cdr_md = extract_entities_spacy(text, nlp_bc5cdr_md, 'CHEMICAL')

    # Extract entities using BioBERT
    diseases_biobert = extract_entities_biobert(text, tokenizer, model)
    drugs_biobert = extract_entities_biobert(text, tokenizer, model)

    # Compare the results and analyze differences
    # ...

if __name__ == "__main__":
    main()
