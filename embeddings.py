from transformers import AutoModel
import torch

model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

def get_embeddings(text_tokens):
    with torch.no_grad():
        outputs = model(**text_tokens)
    return outputs.last_hidden_state.mean(dim=1)
