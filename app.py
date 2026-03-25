import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open("models/embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

with open("models/documents.pkl", "rb") as f:
    documents = pickle.load(f)

topics = pd.read_csv("models/bertopic_doc_topics.csv")
entities = pd.read_csv("models/extracted_entities.csv")
nodes = pd.read_csv("models/knowledge_graph_nodes.csv")
edges = pd.read_csv("models/knowledge_graph_edges.csv")

# Retrieval
def retrieve(query, top_k=3):
    query_embedding = model.encode([query])
    scores = np.dot(embeddings, query_embedding.T).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]
    return [documents[i] for i in top_indices]

# UI
st.title("AI Trends Intelligence Platform 🚀")

menu = st.sidebar.selectbox("Select Feature", [
    "Ask AI",
    "Topic Explorer",
    "Entity Explorer",
    "Knowledge Graph"
])

# ------------------------
# ASK AI
# ------------------------
if menu == "Ask AI":
    st.header("Ask about AI Trends")

    query = st.text_input("Enter your question:")

    if query:
        results = retrieve(query)

        for i, res in enumerate(results):
            st.write(f"### Result {i+1}")
            st.write(res)

# ------------------------
# TOPIC EXPLORER
# ------------------------
elif menu == "Topic Explorer":
    st.header("Topic Exploration")

    st.write("Sample Topics:")
    st.dataframe(topics.head(20))

# ------------------------
# ENTITY EXPLORER
# ------------------------
elif menu == "Entity Explorer":
    st.header("Entities")

    entity_input = st.text_input("Search entity:")

    if entity_input:
        filtered = entities[entities.astype(str).apply(lambda x: x.str.contains(entity_input, case=False)).any(axis=1)]
        st.dataframe(filtered.head(20))

# ------------------------
# KNOWLEDGE GRAPH
# ------------------------
elif menu == "Knowledge Graph":
    st.header("Knowledge Graph")

    st.write("Nodes:")
    st.dataframe(nodes.head(20))

    st.write("Edges:")
    st.dataframe(edges.head(20))