# 🏥 Healthcare NLP Pipelines
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-yellow?logo=huggingface&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

This repository demonstrates transformer-based NLP models applied to healthcare records. It includes preprocessing scripts, embeddings, and retrieval workflows using PyTorch, Hugging Face, LangChain, and FAISS/Pinecone.

---

## 🚀 Features
- Transformer-based NLP models (BERT, ClinicalBERT, etc.)
- Preprocessing of structured & semi-structured healthcare records
- Embedding generation with Hugging Face & LangChain
- Retrieval-Augmented Generation (RAG) pipelines
- Vector search using FAISS/Pinecone
- Deployment-ready FastAPI endpoints

---

## 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** PyTorch, Hugging Face Transformers, LangChain
- **Vector DBs:** FAISS, Pinecone
- **Deployment:** FastAPI, Docker
- **Cloud:** AWS SageMaker (optional)

---

## 📂 Repository Structure
---

## ⚡ Quickstart

Clone the repo and install dependencies:
```bash
git clone https://github.com/melessemenelik/healthcare-nlp-pipelines.git
cd healthcare-nlp-pipelines
pip install -r requirements.txt
uvicorn src.api:app --reload
curl -X POST "http://127.0.0.1:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"text":"Patient diagnosed with diabetes"}'
## 🌟 Example Use Case
- **Input:** "Patient diagnosed with diabetes, prescribed metformin"
- **Output:** Retrieved relevant medical context + generated summary

