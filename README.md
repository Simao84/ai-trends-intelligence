#  AI Trends Intelligence Platform

An end-to-end NLP-powered system for tracking, analyzing, and exploring AI trends using text mining, embeddings, knowledge graphs, and retrieval-augmented generation (RAG).

---

##  Overview

This project analyzes over 16,000 AI-related media articles to uncover trends, sentiment, key entities, and relationships in the rapidly evolving AI landscape.

It combines:

- Advanced NLP techniques
- Embedding models (Word2Vec, FastText, MiniLM, DistilBERT)
- Knowledge graph construction
- Retrieval-Augmented Generation (RAG)
- Interactive Streamlit application

 The result is a **fully integrated AI Trend Intelligence System**.

---

##  Project Pipeline

###  Stage 1 – NLP & Knowledge Extraction
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Sentiment analysis
- Named Entity Recognition (NER)
- Knowledge graph construction
- Topic modeling (BERTopic, LDA)

---

###  Stage 2 – Embeddings & Model Analysis
- Classical embeddings (Word2Vec, FastText)
- Transformer-based models (MiniLM, DistilBERT)
- Model comparison and evaluation
- Insight extraction from semantic representations

---

###  Stage 3 – RAG System
- Q&A dataset generation
- Semantic retrieval
- Knowledge graph integration
- Evaluation (faithfulness, relevance, grounding)

---

###  Application Layer – Streamlit App
An interactive interface that allows users to:

- Ask questions about AI trends
- Explore topics
- Analyze entities
- Navigate the knowledge graph

 **Note:** The Streamlit application is currently under active development and will be further improved with enhanced RAG capabilities and visualization features.

---

## System Architecture
Data → NLP Processing → Embeddings → RAG → Streamlit Interface
---

##  Key Features

-  Semantic search using MiniLM embeddings
-  Topic modeling with BERTopic
-  Knowledge graph of AI ecosystem
-  Retrieval-based question answering
-  AI trend and sentiment analysis
-  Interactive dashboard (Streamlit)

---

##  Use Cases

- **Business Intelligence**  
  Identify emerging AI technologies and market trends

- **Investment Analysis**  
  Track dominant players and innovation areas

- **Research & Policy**  
  Analyze ethical debates and AI regulation trends

---

## Dataset

This project uses the AI Media Dataset (2024–2025):

https://www.kaggle.com/datasets/jannalipenkova/ai-media-dataset

Due to file size limitations, the dataset is not included in this repository.
Please download it manually and place it in the /data folder.

---

## Large Files Notice

Some files are not included due to GitHub size limitations:

- cleaned_ai_media_dataset.parquet
- documents.pkl

To reproduce the full pipeline:

Download the dataset from Kaggle
Run the notebooks in order:
 - Stage 1 → Data processing
 - Stage 2 → Embeddings
 - Stage 3 → RAG system

---

##  Security Note

API keys and sensitive credentials are not included in this repository.  
Environment variables should be used instead.

---

##  Installation
git clone https://github.com/Simao84/ai-trends-intelligence.git
cd ai-trends-intelligence

pip install -r requirements.txt

---


##  Run the App
streamlit run app.py

---

##  Final Note

This project demonstrates how modern NLP, embeddings, and knowledge graphs can be combined into a scalable AI intelligence system.
The current version already provides strong analytical capabilities, while future iterations will focus on improving the intelligence and reasoning capabilities of the system.

---

##  Author

Simao Diavita Garcia


---
