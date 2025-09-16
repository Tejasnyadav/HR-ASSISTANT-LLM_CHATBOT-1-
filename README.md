# HR Assistant (Local LLM Chatbot)

## Overview
This is a **local HR Assistant chatbot** that helps employees get answers to HR-related questions such as leave policies, benefits, and company information.  
It uses a **Python Flask backend**, **HTML + JS frontend**, and a **local LLM (e.g., Ollama's Llama3/Gemma models)** for natural language understanding.  

Employees can ask questions like:
- "How many sick leaves do I get?"
- "What are the paid leave policies?"
- "How can I apply for a benefit?"

---

## Key Features
- Local AI assistant: No need for external API calls (except optional OpenAI API).  
- HR policies stored in text files (`policies/` folder).  
- Uses **sentence embeddings (SentenceTransformer)** + FAISS for policy search.  
- Clean, chat-style frontend for asking HR questions.  
- Supports casual, paid, and sick leave queries.
- Sick leave requires medical certificate after 2 days.  
- Optional: Integrate local LLM for smarter answers.

---

## Limitations
- Requires sufficient RAM for local LLM models.  
- Only answers based on the policies provided in the `policies/` folder.  
- Vector store (`vector_store.pkl`) must be generated on first run if missing.

---

## Tools & Libraries
- Python 3.x  
- Flask  
- SentenceTransformers (`all-MiniLM-L6-v2`)  
- FAISS  
- Ollama (local LLM)  
- HTML, CSS, JS for frontend  

---

## Project Structure

HR-ASSISTANT2/
│
├─ app.py # Flask backend
├─ .gitignore # Ignore large files
├─ vector_store.pkl # FAISS index (generated locally)
├─ policies/ # HR policy text files
│ ├─ leave_policy.txt
│ └─ benefits.txt
└─ static/
├─ index.html # Frontend HTML
└─ app.js # JS for chat

---

## Setup Instructions


```bash
git clone https://github.com/yourusername/HR-Assistant-Local-LLM.git
cd HR-Assistant-Local-LLM
python -m venv hrv
hrv\Scripts\activate     # Windows
# OR
source hrv/bin/activate  # Mac/Linux
pip install flask sentence-transformers faiss-cpu
ollama pull llama3    # Or gemma:2b
python app.py
http://127.0.0.1:5000

![Chat Screenshot](images/chat_screenshot.png)
