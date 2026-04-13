import pandas as pd
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

def preprocess_text(text: str):
    tokens = tokenizer(text, truncation=True, padding="max_length", max_length=128)
    return tokens
