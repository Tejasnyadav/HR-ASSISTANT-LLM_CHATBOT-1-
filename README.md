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

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/HR-Assistant-Local-LLM.git
cd HR-Assistant-Local-LLM

2.**Create a virtual environment and activate it**:

python -m venv hrv
hrv\Scripts\activate     # Windows
# OR
source hrv/bin/activate  # Mac/Linux

Install required Python packages:

pip install flask sentence-transformers faiss-cpu


Install Ollama and download a local LLM (optional for local AI responses):

ollama pull llama3    # Or gemma:2b


Make sure your policies/ folder has policy text files like leave_policy.txt and benefits.txt.


How to Run the Project

Start the Flask server:

python app.py


Open a browser and go to:

http://127.0.0.1:5000


Type your HR questions in the chat box and press Send.


![Chat Screenshot](images/chat_screenshot.png)
![Chat Screenshot](images/chat_screenshot.png)
